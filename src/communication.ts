import { UDPHelper, InstanceStatus } from '@companion-module/base'
import * as dgram from 'dgram'
import * as os from 'os'
import { getUdpModelIndex } from './devices/index.js'
import { LOG_RAW_PACKETS } from './debug.js'

export interface DeviceInfo {
	host: string
	port: number
	model: string
	name: string
	vendor: string
	mac: string
	sn: string
	productType: number
	/** Dev_Type used in heartbeat packets (mapped from the model, same as the host app get_udp_model_index) */
	udpType: number
	protocolVer: number
	lastSeen: number
}

/**
 * Meaning of the product type byte (byte offset 22, per the device protocol).
 * Reference host app: ["Unknow", "Switcher", "Encoder", "Chroma"]
 */
export const PRODUCT_TYPE_NAMES = ['Unknow', 'Switcher', 'Encoder', 'Chroma']

export function getProductTypeName(productType: number): string {
	// The H4K family identifies the exact product in the type field (0x06/0x07=H4K PLUS, 0x08=H4K)
	const extended: Record<number, string> = { 6: 'SHARK H4K PLUS', 7: 'SHARK H4K PLUS', 8: 'SHARK H4K' }
	return extended[productType] ?? PRODUCT_TYPE_NAMES[productType] ?? `Unknown(${productType})`
}

// Model -> heartbeat Dev_Type mapping now lives in src/devices/profiles.ts (per product profile);
// this re-export is kept for existing callers.
export { getUdpModelIndex }

/** Max scan duration; the scan is force-finished afterwards so a hung Promise never blocks later scans */
const SCAN_TIMEOUT_MS = 10000

/** Whether a MAC is valid (aa:bb:cc:dd:ee:ff and not all zero) */
export function isValidMac(mac: string | undefined): boolean {
	return /^([0-9a-f]{2}:){5}[0-9a-f]{2}$/i.test((mac ?? '').trim()) && !/^00:00:00:00:00:00$/i.test((mac ?? '').trim())
}

export interface ParsedPacket {
	version: number
	index: number
	type: number
	session: number
	cmd: number
	data: Buffer
}

export class UDPPacker {
	/** Packet type: 0x00 command from host, 0x01 device response, 0x02 device active report */
	static readonly TYPE_COMMAND = 0x00
	static readonly TYPE_RESPONSE = 0x01
	static readonly TYPE_REPORT = 0x02

	/**
	 * Build a discovery packet.
	 * Reference host app _gen_discover_packet: index=0x0001, session=0x00000001, cmd=0xFFFF, data=[0xFF]
	 */
	static packDiscover(): Buffer {
		const data = Buffer.from([0xff])
		return this.packCommand(0xffff, data, 0x0001, 0x0001)
	}

	/**
	 * Build a heartbeat packet: cmd=0xEEEE, data=[Dev_Type(1)] + MAC(6), 7 bytes in total.
	 * Identical to send_heartbeat_instruction in the host app avm_ccp.py:
	 *   _cmd = 0xEEEE; _data = [device_type] + mac_addr
	 * Note: heartbeat data only carries Dev_Type + MAC, no Param_Vaild (that is only used by data commands).
	 */
	static packHeartbeat(deviceType: number, mac: string, index: number = 1, session: number = 1): Buffer {
		const macBytes = Buffer.from(mac.split(':').map((b) => parseInt(b, 16)))
		const data = Buffer.concat([Buffer.from([deviceType]), macBytes])
		return this.packCommand(0xeeee, data, index, session)
	}

	/**
	 * Pack a packet following the AVMATRIX CCP protocol.
	 * Field order (same as avm_ccp.py command_data_packing):
	 * header(2) version(2) total length(2) index(2) padding(8) type(1) cmd(2) session(4) data length(2) data checksum(2) tail(2)
	 */
	static packCommand(
		cmd: number,
		data: Buffer,
		index: number = 0,
		session: number = 0,
		type: number = UDPPacker.TYPE_COMMAND,
	): Buffer {
		const headerLength = 25
		const checksumLength = 2
		const tailLength = 2
		const totalLength = headerLength + data.length + checksumLength + tailLength

		const packet = Buffer.alloc(totalLength)
		let offset = 0

		packet.writeUInt16BE(0xa55a, offset) // header
		offset += 2
		packet.writeUInt16BE(0x0100, offset) // version
		offset += 2
		packet.writeUInt16BE(totalLength, offset) // total length
		offset += 2
		packet.writeUInt16BE(index, offset) // packet index
		offset += 2
		offset += 8 // 8-byte padding
		packet.writeUInt8(type, offset) // packet type
		offset += 1
		packet.writeUInt16BE(cmd, offset) // command code
		offset += 2
		packet.writeUInt32BE(session, offset) // session
		offset += 4
		packet.writeUInt16BE(data.length, offset) // data length
		offset += 2
		data.copy(packet, offset)
		offset += data.length

		let checksum = 0
		for (let i = 0; i < offset; i++) {
			checksum += packet[i]
		}
		packet.writeUInt16BE(checksum & 0xffff, offset)
		offset += 2
		packet.writeUInt16BE(0xa66a, offset) // tail

		return packet
	}
}

export class UDPParser {
	/**
	 * Reference host app parsing (avm_ccp.py packet_parser):
	 * - the host app does not validate the header, it parses directly
	 * - the device reply header is 0x5AA5 while we send 0xA55A
	 * - checks: total length == actual length, data length == total length - 29, then compare the checksum
	 */
	static parse(data: Buffer): ParsedPacket | null {
		if (data.length < 29) {
			return null
		}

		// The device reply header is 0x5AA5, so the header is not validated
		const packetLength = data.readUInt16BE(4)
		if (packetLength !== data.length) {
			return null
		}

		const version = data.readUInt16BE(2)
		const index = data.readUInt16BE(6)
		const type = data.readUInt8(16)
		const cmd = data.readUInt16BE(17)
		const session = data.readUInt32BE(19)
		const dataLength = data.readUInt16BE(23)

		// Same as the host app: data length must be exactly total length minus 29
		if (dataLength !== packetLength - 29) {
			return null
		}

		const payloadData = data.slice(25, 25 + dataLength)

		const checksumOffset = 25 + dataLength
		const checksum = data.readUInt16BE(checksumOffset)
		let calculatedChecksum = 0
		for (let i = 0; i < checksumOffset; i++) {
			calculatedChecksum += data[i]
		}

		if (checksum !== (calculatedChecksum & 0xffff)) {
			return null
		}

		return {
			version,
			index,
			type,
			session,
			cmd,
			data: payloadData,
		}
	}

	static parseDeviceInfo(data: Buffer): Partial<DeviceInfo> {
		const info: Partial<DeviceInfo> = {}
		if (data.length < 53) return info

		// Field offsets match the reference host app (avm_ccp.py)
		info.vendor = data.slice(0, 6).toString('ascii').replace(/\0/g, '')
		const productName = data.slice(6, 22).toString('ascii').replace(/\0/g, '')
		info.productType = data.readUInt8(22)
		info.model = data.slice(23, 33).toString('ascii').replace(/\0/g, '')
		data.readUInt32BE(33)
		info.sn = data.slice(37, 45).toString('ascii').replace(/\0/g, '')

		const macBytes = data.slice(45, 51)
		info.mac = Array.from(macBytes)
			.map((b) => b.toString(16).padStart(2, '0'))
			.join(':')

		if (data.length >= 53) {
			info.protocolVer = data.readUInt16BE(51)
		}

		info.name = productName || info.model || 'Unknown'
		return info
	}

	/**
	 * Parse the data of a heartbeat (0xEEEE) reply (see PSV0617 doc 3.3.3):
	 *   vendor(6) + Product_name(16) + MAC(6)
	 */
	static parseHeartbeatReply(data: Buffer): { vendor: string; productName: string; mac: string } | null {
		if (data.length < 28) return null
		const vendor = data.slice(0, 6).toString('ascii').replace(/\0/g, '')
		const productName = data.slice(6, 22).toString('ascii').replace(/\0/g, '')
		const mac = Array.from(data.slice(22, 28))
			.map((b) => b.toString(16).padStart(2, '0'))
			.join(':')
		return { vendor, productName, mac }
	}
}

export interface CommunicationOptions {
	host: string
	port: number
	timeout?: number
	scanPort?: number
	heartbeatInterval?: number
	/** Liveness probe command for families without a heartbeat (empty Data), e.g. H4K 0x0001 */
	probeCommand?: number
	/** Report packets (Pack_Type=2) are already handled by onReport; skip the generic onData path (H4K) */
	skipReportDataCallback?: boolean
	onLog?: (level: 'info' | 'error' | 'debug' | 'warn', message: string) => void
}

export interface DeviceCallback {
	session: number
	cmd: number
	callback: (data: Buffer) => void
}

export class CommunicationManager {
	private udp: UDPHelper | undefined
	private discoverySocket: dgram.Socket | undefined
	/** Sockets created per interface during a scan, closed together on disconnect/timeout */
	private scanSockets: dgram.Socket[] = []
	/** Set once disconnect() aborts a scan, so pending rounds never send on closed sockets */
	private scanAborted = false
	/** Timers created by a scan (round interval / finish delay / timeout) */
	private scanTimers: NodeJS.Timeout[] = []
	/** Resolve callback of the scan in progress, used to end it early */
	private scanFinish: (() => void) | undefined
	private options: CommunicationOptions
	private isConnected = false
	private discoveredDevices: Map<string, DeviceInfo> = new Map()
	/** Target device of the current connection */
	private connectedDevice: DeviceInfo | undefined
	private callbacks: DeviceCallback[] = []
	private sessionCounter = 1
	/** Packet index (reference: host app `_index`); incremented per command, wrapped to 1..0xffff */
	private indexCounter = 0
	private heartbeatTimer: NodeJS.Timeout | undefined
	private heartbeatMissed = 0
	private maxHeartbeatMissed = 3
	private onStatusChangeCallback: ((status: InstanceStatus, message?: string) => void) | undefined
	private onDataCallback:
		| ((data: Buffer, host: string, port: number, cmd?: number, session?: number) => void)
		| undefined
	private onErrorCallback: ((error: Error) => void) | undefined
	private onLogCallback: ((level: 'info' | 'error' | 'debug' | 'warn', message: string) => void) | undefined
	private reportCallback: ((packet: ParsedPacket) => void) | undefined

	constructor(options: CommunicationOptions) {
		this.options = {
			timeout: 5000,
			scanPort: 7000,
			heartbeatInterval: 5000,
			...options,
		}
		this.onLogCallback = options.onLog
	}

	public setCallbacks(callbacks: {
		onStatusChange?: (status: InstanceStatus, message?: string) => void
		onData?: (data: Buffer, host: string, port: number, cmd?: number, session?: number) => void
		onError?: (error: Error) => void
		onReport?: (packet: ParsedPacket) => void
	}): void {
		this.onStatusChangeCallback = callbacks.onStatusChange
		this.onDataCallback = callbacks.onData
		this.onErrorCallback = callbacks.onError
		this.reportCallback = callbacks.onReport
	}

	public async connect(): Promise<void> {
		this.log('debug', '========================================')
		this.log('debug', 'Starting UDP connection to device')
		this.log('debug', `Host: ${this.options.host}`)
		this.log('debug', `Port: ${this.options.port}`)
		this.log('debug', '========================================')
		this.disconnect()
		this.setupUDP()
	}

	public disconnect(): void {
		this.log('debug', 'Disconnecting from device')
		this.stopHeartbeat()
		if (this.udp) {
			this.udp.destroy()
			this.udp = undefined
		}
		// L1: stop a running scan (timers + sockets) so disabling the connection
		// during discovery does not leave broadcast sockets alive.
		this.abortScan()
		this.isConnected = false
		this.callbacks = []
	}

	/** Track a timer created by a scan so disconnect() can cancel it. */
	private scanLater(fn: () => void, ms: number): void {
		this.scanTimers.push(setTimeout(fn, ms))
	}

	/** Close every socket owned by the scan. */
	private closeScanSockets(): void {
		if (this.discoverySocket) {
			try {
				this.discoverySocket.close()
			} catch {
				/* ignore */
			}
			this.discoverySocket = undefined
		}
		for (const sock of this.scanSockets) {
			try {
				sock.close()
			} catch {
				/* ignore */
			}
		}
		this.scanSockets = []
	}

	/**
	 * Stop a running scan: cancel pending rounds, close all scan sockets and
	 * resolve scanNetwork() early. Safe to call when no scan is running.
	 */
	private abortScan(): void {
		this.scanAborted = true
		for (const t of this.scanTimers) clearTimeout(t)
		this.scanTimers = []
		this.closeScanSockets()
		const finish = this.scanFinish
		this.scanFinish = undefined
		finish?.()
	}

	/**
	 * Next packet index. The field is 16-bit, so it must wrap: otherwise the
	 * 65,536th command throws ERR_OUT_OF_RANGE and every later send fails.
	 */
	private nextIndex(): number {
		this.indexCounter = (this.indexCounter % 0xffff) + 1
		return this.indexCounter
	}

	/** Next session id, wrapped as an unsigned 32-bit value (first value stays 1). */
	private nextSession(): number {
		const session = this.sessionCounter
		this.sessionCounter = (this.sessionCounter + 1) >>> 0
		return session
	}

	public async sendCommand(cmd: number, data: Buffer): Promise<boolean> {
		if (!this.isConnected) {
			const error = new Error('Not connected')
			this.log('error', error.message)
			this.onErrorCallback?.(error)
			return false
		}

		try {
			const session = this.nextSession()
			const packet = UDPPacker.packCommand(cmd, data, this.nextIndex(), session)

			if (this.udp) {
				this.log(
					'debug',
					`[Send] Command: 0x${cmd.toString(16).padStart(4, '0')}, Session: ${session}, Length: ${packet.length} bytes`,
				)
				// Print the whole outgoing packet (hex) only when local debugging is enabled (AVM_LOG_RAW_PACKETS=1)
				if (LOG_RAW_PACKETS) this.log('debug', `[Send] Packet hex: ${packet.toString('hex')}`)
				this.log('debug', `[Send] Target: ${this.options.host}:${this.options.port}`)
				// Use await so a failed send is handled by try/catch instead of becoming an
				// unhandled rejection that kills the module process on Node 22 (link down / no route).
				await this.udp.send(packet)
				return true
			}
			return false
		} catch (error) {
			this.log('error', `Send failed: ${(error as Error).message}`)
			this.onErrorCallback?.(error as Error)
			return false
		}
	}

	/**
	 * Collect the broadcast address of every IPv4 interface.
	 * Reference host app:
	 * socket.getaddrinfo(hostname, None) is used to get the IP of each IPv4 interface,
	 * then one AvmScannerPhy is created per interface, bound to that IP with a system-assigned port,
	 * and every interface broadcasts to 255.255.255.255:7000.
	 *
	 * In Node.js os.networkInterfaces() provides the interface list.
	 * Key point: bind to the interface IP instead of 0.0.0.0 so Windows uses the correct NIC.
	 */
	private getInterfaceAddresses(): { iface: string; address: string }[] {
		const results: { iface: string; address: string }[] = []
		const interfaces = os.networkInterfaces()

		for (const [name, addrs] of Object.entries(interfaces)) {
			if (!addrs) continue
			for (const addr of addrs) {
				if (addr.family !== 'IPv4' || addr.internal) continue
				results.push({ iface: name, address: addr.address })
			}
		}
		return results
	}

	/**
	 * Discover devices on the network.
	 * Reference host app: one socket per network interface, bound to the interface IP, broadcasting to 255.255.255.255.
	 */
	public async scanNetwork(): Promise<void> {
		this.scanAborted = false
		this.scanTimers = []
		const scanPort = this.options.scanPort || 7000
		const interfaceAddrs = this.getInterfaceAddresses()

		this.log('debug', '========================================')
		this.log('debug', '[Scan] Starting device discovery')
		this.log('debug', `[Scan] Scan port: ${scanPort}`)
		this.log('debug', `[Scan] Detected ${interfaceAddrs.length} IPv4 interface(s):`)
		for (const iface of interfaceAddrs) {
			this.log('debug', `[Scan]   [${iface.iface}] ${iface.address}`)
		}
		if (interfaceAddrs.length === 0) {
			this.log('error', '[Scan] No valid IPv4 network interfaces found!')
		}
		this.log('debug', '========================================')

		this.discoveredDevices.clear()

		// Reference host app: one socket per interface, bound to the interface IP with a system-assigned port;
		// every socket broadcasts to 255.255.255.255:7000
		return new Promise((resolve) => {
			// Safety timeout: a bind callback that never fires must not leave the Promise pending forever
			let settled = false
			const finish = () => {
				if (settled) return
				settled = true
				clearTimeout(timeoutHandle)
				this.scanFinish = undefined
				resolve()
			}
			this.scanFinish = finish
			const timeoutHandle = setTimeout(() => {
				this.log('warn', `[Scan] Discovery timed out after ${SCAN_TIMEOUT_MS}ms`)
				// Abort through the same path as disconnect(): sets scanAborted, clears pending round
				// timers and closes every socket, so no later round can send on a closed socket.
				this.abortScan()
			}, SCAN_TIMEOUT_MS)
			this.scanTimers.push(timeoutHandle)

			try {
				const broadcastTarget = '255.255.255.255'
				const discoverPacket = UDPPacker.packDiscover()
				this.log('debug', `[Scan] Scan packet size: ${discoverPacket.length} bytes`)
				this.log('debug', `[Scan] Send discovery packet (cmd=0xFFFF, data=[FF]) -> ${broadcastTarget}:${scanPort}`)
				if (LOG_RAW_PACKETS) this.log('debug', `[Scan] Packet hex: ${discoverPacket.toString('hex')}`)

				// Create one socket per network interface and register it in this.scanSockets,
				// so disconnect/timeout can close them together
				this.scanSockets = []
				const sockets: dgram.Socket[] = this.scanSockets

				const onMessage = (msg: Buffer, rinfo: dgram.RemoteInfo) => {
					this.log('debug', `[Scan] Discovery response from ${rinfo.address}:${rinfo.port}, size=${msg.length} bytes`)
					if (LOG_RAW_PACKETS) this.log('debug', `[Scan] Response hex: ${msg.toString('hex')}`)

					const parsed = UDPParser.parse(msg)
					if (!parsed) {
						this.log('warn', '[Scan] Invalid discovery response - parse failed')
						return
					}

					this.log(
						'debug',
						`[Scan] Parsed header - type: 0x${parsed.type.toString(16)}, cmd: 0x${parsed.cmd.toString(16)}, session: ${parsed.session}, dataLen: ${parsed.data.length}`,
					)

					// A discovery response must be a cmd=0xFFFF reply
					if (parsed.cmd !== 0xffff) {
						this.log('debug', `[Scan] Ignoring non-discovery response cmd=0x${parsed.cmd.toString(16)}`)
						return
					}

					// Log every parsed field to make model identification issues easier to diagnose
					const deviceInfo = UDPParser.parseDeviceInfo(parsed.data)
					this.log('debug', `[Scan] Parsed device info (payload ${parsed.data.length} bytes):`)
					this.log('debug', `[Scan]   vendor      = "${deviceInfo.vendor ?? ''}"`)
					this.log('debug', `[Scan]   productName = "${deviceInfo.name ?? ''}"`)
					this.log('debug', `[Scan]   model       = "${deviceInfo.model ?? ''}"`)
					this.log(
						'debug',
						`[Scan]   productType = ${deviceInfo.productType ?? 0} (${getProductTypeName(deviceInfo.productType ?? 0)})`,
					)
					this.log('debug', `[Scan]   sn          = "${deviceInfo.sn ?? ''}"`)
					this.log('debug', `[Scan]   mac         = "${deviceInfo.mac ?? ''}"`)
					this.log('debug', `[Scan]   protocolVer = ${deviceInfo.protocolVer ?? 0}`)

					if (!deviceInfo.model) {
						this.log('warn', '[Scan] Model field is empty, cannot map to a device list entry')
					}

					// Match model + device type together (the H4K 6/7/8 ids are more reliable)
					const modelIndex = getUdpModelIndex(deviceInfo.model, deviceInfo.productType)
					const device: DeviceInfo = {
						host: rinfo.address,
						port: rinfo.port,
						model: deviceInfo.model || 'Unknown',
						name: deviceInfo.name || 'Unknown Device',
						vendor: deviceInfo.vendor || '',
						mac: deviceInfo.mac || '00:00:00:00:00:00',
						sn: deviceInfo.sn || '',
						productType: deviceInfo.productType || 0,
						udpType: modelIndex !== 0xff ? modelIndex : deviceInfo.productType || 0xff,
						protocolVer: deviceInfo.protocolVer || 0,
						lastSeen: Date.now(),
					}

					const deviceKey = device.sn || rinfo.address
					if (!this.discoveredDevices.has(deviceKey)) {
						// Log only on first discovery, so repeated replies do not flood the log
						this.log(
							'debug',
							`[Scan] Device discovered: host=${device.host}, model=${device.model}, name=${device.name}, sn=${device.sn}, mac=${device.mac}`,
						)
					} else {
						this.log('debug', `[Scan] Duplicate discovery response ignored: host=${device.host}, sn=${device.sn}`)
					}
					this.discoveredDevices.set(deviceKey, device)
				}

				const onError = (err: Error) => {
					this.log('error', `Discovery socket error: ${err.message}`)
				}

				if (interfaceAddrs.length === 0) {
					// No interface detected: fall back to 0.0.0.0
					this.log('warn', 'No interfaces detected, falling back to 0.0.0.0')
					const sock = dgram.createSocket({ type: 'udp4', reuseAddr: true })
					this.discoverySocket = sock
					sock.on('message', onMessage)
					sock.on('error', onError)
					sock.bind(0, '0.0.0.0', () => {
						this.sendDiscoveryScans([sock], discoverPacket, scanPort, broadcastTarget, finish)
					})
				} else {
					// Create one socket per network interface
					let boundCount = 0
					for (const iface of interfaceAddrs) {
						const sock = dgram.createSocket({ type: 'udp4', reuseAddr: true })
						// Register on creation, so a socket whose bind fails is still closed on timeout/abort
						sockets.push(sock)
						sock.on('message', onMessage)
						sock.on('error', onError)

						// Bind to the interface IP with a system-assigned port (same as the host app)
						sock.bind(0, iface.address, () => {
							const addr = sock.address()
							this.log('debug', `Socket bound to [${iface.iface}] ${addr.address}:${addr.port}`)
							sock.setBroadcast(true)
							boundCount++

							// All sockets are bound, start sending
							if (boundCount === interfaceAddrs.length) {
								this.sendDiscoveryScans(sockets, discoverPacket, scanPort, broadcastTarget, finish)
							}
						})
					}
				}
			} catch (error) {
				this.log('error', `Discovery failed: ${(error as Error).message}`)
				finish()
			}
		})
	}

	/**
	 * Send the scan packets (4 rounds, 1 s apart).
	 * @param finish end callback that clears the safety timeout and resolves
	 */
	private sendDiscoveryScans(
		sockets: dgram.Socket[],
		packet: Buffer,
		scanPort: number,
		broadcastTarget: string,
		finish: () => void,
	): void {
		const maxScans = 4 // Same as the host app Scanner._MAX_TIMES, improving discovery reliability
		let scanCount = 0

		const sendScan = () => {
			if (this.scanAborted) return
			if (scanCount >= maxScans) return
			scanCount++
			const currentScan = scanCount

			// Every socket sends the broadcast packet
			let sentCount = 0
			for (const sock of sockets) {
				try {
					sock.send(packet, 0, packet.length, scanPort, broadcastTarget, (err) => {
						if (err) {
							this.log('error', `Scan ${currentScan}/${maxScans} failed: ${err.message}`)
						} else {
							// The socket may be closed between send() and this callback; address() throws
							// synchronously (ERR_SOCKET_DGRAM_NOT_RUNNING), so keep it guarded and let the round continue.
							try {
								const addr = sock.address()
								this.log(
									'debug',
									`Scan ${currentScan}/${maxScans} sent from ${addr.address}:${addr.port} -> ${broadcastTarget}:${scanPort}`,
								)
							} catch (error) {
								this.log(
									'debug',
									`Scan ${currentScan}/${maxScans} sent (socket already closed: ${(error as Error).message})`,
								)
							}
						}
						sentCount++
						// All sockets have sent; schedule the next round in 1 s
						if (sentCount >= sockets.length && currentScan < maxScans) {
							this.scanLater(sendScan, 1000)
						}
						// Last round sent; wait for replies before finishing
						if (sentCount >= sockets.length && currentScan === maxScans) {
							this.scanLater(() => {
								this.log('debug', '========================================')
								this.log('debug', `[Scan] Discovery complete - Found ${this.discoveredDevices.size} device(s)`)
								for (const [key, dev] of this.discoveredDevices) {
									this.log(
										'debug',
										`[Scan]   [${key}] model="${dev.model}" type=${getProductTypeName(dev.productType)} name="${dev.name}" at ${dev.host}:${dev.port}`,
									)
								}
								this.log('debug', '========================================')

								for (const s of sockets) {
									try {
										s.close()
									} catch {
										/* ignore */
									}
								}
								this.discoverySocket = undefined
								this.scanSockets = []
								finish()
							}, 1500)
						}
					})
				} catch (error) {
					// dgram throws synchronously (ERR_SOCKET_DGRAM_NOT_RUNNING) if the socket is already closed
					this.log('debug', `Scan ${currentScan}/${maxScans} skipped on a closed socket: ${(error as Error).message}`)
				}
			}
		}

		sendScan()
	}

	public startHeartbeat(): void {
		this.stopHeartbeat()
		this.heartbeatMissed = 0

		// Probe immediately, so the device state is known without waiting a full interval
		void this.sendHeartbeat()

		this.heartbeatTimer = setInterval(() => {
			void this.sendHeartbeat()
		}, this.options.heartbeatInterval)

		this.log('debug', `Heartbeat started - Interval: ${this.options.heartbeatInterval}ms`)
	}

	public stopHeartbeat(): void {
		if (this.heartbeatTimer) {
			clearInterval(this.heartbeatTimer)
			this.heartbeatTimer = undefined
		}
	}

	/**
	 * Liveness probe (heartbeat), following the host app UDP flow:
	 * heartbeat command 0xEEEE, data = [Dev_Type(1)] + MAC(6), increasing index and a random session,
	 * sent unicast directly to the target device (the host app DevicePhy).
	 *
	 * UDP is connectionless: a ready socket does not mean the device is online; any valid packet marks it alive.
	 */
	private async sendHeartbeat(): Promise<void> {
		const device = this.connectedDevice
		// Note: with a manually typed IP, device is undefined but the configured host must still be probed,
		// otherwise the device never becomes online (returning early here used to break manual IPs).

		try {
			if (!this.udp) return

			const useHeartbeat = device !== undefined && isValidMac(device.mac)
			const probeCommand = this.options.probeCommand
			// Priority: MAC present -> 0xEEEE heartbeat; family probe command -> that command; else the 0xFFFF discovery packet
			let packet: Buffer
			let probeLabel: string
			if (useHeartbeat && device) {
				// Reference sample: heartbeat index=1, session=1 fixed
				packet = UDPPacker.packHeartbeat(device.udpType ?? 0xff, device.mac, 1, 1)
				probeLabel = '0xEEEE'
			} else if (probeCommand !== undefined) {
				packet = UDPPacker.packCommand(probeCommand, Buffer.alloc(0), 1, 1)
				probeLabel = `0x${probeCommand.toString(16).padStart(4, '0')}`
			} else {
				packet = UDPPacker.packCommand(0xffff, Buffer.from([0xff]), 1, 1)
				probeLabel = '0xFFFF'
			}

			this.log(
				'debug',
				`[Heartbeat] Probe -> ${this.options.host}:${this.options.port} (${probeLabel}), misses=${this.heartbeatMissed}`,
			)

			// Record failed probes (raw packets only when local debugging is enabled)
			if (this.heartbeatMissed > 0) {
				const raw = LOG_RAW_PACKETS ? ` - sent packet: ${packet.toString('hex')}` : ''
				this.log('debug', `[Heartbeat] No response (misses=${this.heartbeatMissed})${raw}`)
			}

			// A failed send (link down / no route) counts as a miss just like no reply,
			// so the status cannot stay green when the network is gone.
			try {
				await this.udp.send(packet)
			} catch (sendErr) {
				this.log('error', `Heartbeat send failed: ${(sendErr as Error).message}`)
			}
			this.heartbeatMissed++

			if (this.heartbeatMissed >= this.maxHeartbeatMissed) {
				const totalTimeout = this.heartbeatMissed * (this.options.heartbeatInterval || 3000)
				this.log(
					'error',
					`[Heartbeat] Device ${this.options.host} not responding - ${this.heartbeatMissed} consecutive misses (~${totalTimeout}ms), marking disconnected`,
				)
				this.isConnected = false
				this.stopHeartbeat()
				this.onStatusChangeCallback?.(
					InstanceStatus.ConnectionFailure,
					`No response from device after ${totalTimeout}ms`,
				)
			}
		} catch (error) {
			this.log('error', `Heartbeat unexpected failure: ${(error as Error).message}`)
		}
	}

	/**
	 * Any valid packet from the device marks it alive:
	 * reset the miss counter and recover the status from Connecting / Disconnected to online.
	 */
	private markDeviceAlive(): void {
		const wasMissed = this.heartbeatMissed
		this.heartbeatMissed = 0

		if (!this.isConnected) {
			this.isConnected = true
			this.log('info', `[Heartbeat] Device ${this.options.host} responded, connection online`)
			this.onStatusChangeCallback?.(InstanceStatus.Ok, 'Device responded')
			// M1: the heartbeat stops itself after `maxHeartbeatMissed`, so restart it here.
			// Otherwise the status can turn green again with the heartbeat still stopped,
			// and the next dropout is never detected.
			if (!this.heartbeatTimer) this.startHeartbeat()
		} else if (wasMissed > 0) {
			this.log('debug', `[Heartbeat] Device responded, miss counter reset (was ${wasMissed})`)
		}
	}

	public getDiscoveredDevices(): DeviceInfo[] {
		return Array.from(this.discoveredDevices.values())
	}

	/**
	 * Set the target device of the current connection (used for logs and protocol parameters).
	 * The miss counter is reset so a new target starts from a clean count.
	 */
	public setTargetDevice(device: DeviceInfo | undefined): void {
		this.connectedDevice = device
		this.heartbeatMissed = 0

		if (device) {
			this.log(
				'info',
				`[Heartbeat] Target device: model=${device.model}, mac=${device.mac || 'N/A'}, ip=${device.host}`,
			)
		}
	}

	public getStatus(): boolean {
		return this.isConnected
	}

	private setupUDP(): void {
		this.log('debug', 'Initializing UDP Helper...')
		this.udp = new UDPHelper(this.options.host, this.options.port)
		this.log('debug', `UDP Helper created for ${this.options.host}:${this.options.port}`)

		this.udp.on('status_change', (status, message) => {
			this.log('debug', `UDP status_change - Status: ${status}, Message: ${message || 'none'}`)

			if (status === InstanceStatus.Ok) {
				// UDP is connectionless: a ready socket only means the local port is bound,
				// not that the device is online. Report "Connecting" first and wait for a
				// reply (markDeviceAlive) before going online.
				this.log('debug', `Socket ready for ${this.options.host}:${this.options.port}, probing device...`)
				this.isConnected = false
				this.onStatusChangeCallback?.(InstanceStatus.Connecting, 'Waiting for device response...')
				this.startHeartbeat()
			} else {
				this.log('debug', `Connection status: ${status} - ${message}`)
				if (this.isConnected) {
					this.log('error', 'Connection was established but now lost')
				}
				this.isConnected = false
				this.stopHeartbeat()
				this.onStatusChangeCallback?.(status, message)
			}
		})

		this.udp.on('data', (data) => {
			// Packet length/summary; raw hex only when local debugging is enabled (packaged builds never expose packet contents)
			const recvRaw = LOG_RAW_PACKETS ? `: ${data.toString('hex')}` : ''
			this.log('debug', `[Recv] ${data.length}B${recvRaw}`)
			this.log('debug', '========== RECEIVED DATA START ==========')
			this.log('debug', `Raw data length: ${data.length} bytes`)

			const parsed = UDPParser.parse(data)
			if (parsed) {
				// Any valid packet marks the device alive (heartbeat liveness and disconnect recovery)
				this.markDeviceAlive()

				// Heartbeat (0xEEEE) reply: parse vendor / Product_name / MAC and log them
				if (parsed.cmd === 0xeeee) {
					const hb = UDPParser.parseHeartbeatReply(parsed.data)
					if (hb) {
						this.log('debug', `[Heartbeat] Reply - vendor="${hb.vendor}", name="${hb.productName}", mac=${hb.mac}`)
					} else if (LOG_RAW_PACKETS) {
						this.log('debug', `[Heartbeat] Reply (raw ${parsed.data.length}B): ${parsed.data.toString('hex')}`)
					}
				}

				this.log(
					'debug',
					`Type: 0x${parsed.type.toString(16)}, Cmd: 0x${parsed.cmd.toString(16)}, Session: ${parsed.session}`,
				)
				this.log('debug', `Data length: ${parsed.data.length} bytes`)

				const matchedCallback = this.callbacks.find((cb) => cb.session === parsed.session && cb.cmd === parsed.cmd)
				if (matchedCallback) {
					matchedCallback.callback(data)
					this.callbacks = this.callbacks.filter((cb) => cb !== matchedCallback)
					this.log('debug', 'Callback executed and removed')
				}

				if (parsed.type === 0x02) {
					this.log(
						'debug',
						`[Report] Device active report - Cmd: 0x${parsed.cmd.toString(16).padStart(4, '0')}, Session: ${parsed.session}, Data: ${parsed.data.length} bytes`,
					)
					if (LOG_RAW_PACKETS) this.log('debug', `[Report] Data hex: ${parsed.data.toString('hex')}`)
					this.reportCallback?.(parsed)
					this.log('debug', 'Device report handled')
				}

				// L6: report packets are already handled by onReport; running the generic
				// data path again processed every H4K report twice.
				if (!(parsed.type === 0x02 && this.options.skipReportDataCallback)) {
					this.onDataCallback?.(parsed.data, this.options.host, this.options.port, parsed.cmd, parsed.session)
				}
			} else {
				this.log('warn', 'Invalid packet - checksum or format error')
			}

			this.log('debug', '========== RECEIVED DATA END ==========')
		})

		this.udp.on('error', (err) => {
			this.log('error', '************************************')
			this.log('error', 'UDP ERROR OCCURRED')
			this.log('error', `Error: ${err.message}`)
			this.log('error', '************************************')
			this.onErrorCallback?.(err)
		})

		this.log('debug', 'UDP event listeners registered')
	}

	private log(level: 'info' | 'error' | 'debug' | 'warn', message: string): void {
		this.onLogCallback?.(level, message)
	}
}
