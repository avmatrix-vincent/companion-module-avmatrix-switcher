import { UDPHelper, InstanceStatus } from '@companion-module/base'
import * as dgram from 'dgram'
import * as os from 'os'

export interface DeviceInfo {
	host: string
	port: number
	model: string
	name: string
	vendor: string
	mac: string
	sn: string
	productType: number
	/** 心跳报文用的 Dev_Type（按型号映射，与上位机 get_udp_model_index 一致） */
	udpType: number
	protocolVer: number
	lastSeen: number
}

/**
 * 产品类型字节含义（与设备协议一致，字节偏移 22）
 * 参考上位机实现：["Unknow", "Switcher", "Encoder", "Chroma"]
 */
export const PRODUCT_TYPE_NAMES = ['Unknow', 'Switcher', 'Encoder', 'Chroma']

export function getProductTypeName(productType: number): string {
	return PRODUCT_TYPE_NAMES[productType] ?? `Unknown(${productType})`
}

/**
 * 设备型号 -> 心跳报文 Dev_Type 映射
 * 与上位机 ModelPreferences.get_udp_model_index 一致。
 * 注意：心跳的 Dev_Type 不是广播发现里的 productType 字节，而是按型号查表得到。
 */
const UDP_MODEL_INDEX_MAP: Array<{ models: string[]; index: number }> = [
	{ models: ['VS0605'], index: 1 },
	{ models: ['SE2017'], index: 2 },
	{ models: ['CUE01', 'KM32-4K'], index: 3 },
	{ models: ['HVS041E'], index: 4 },
	{ models: ['VS0617', 'PSV0617'], index: 9 },
]

export function getUdpModelIndex(rawModel: string | undefined): number {
	const model = (rawModel ?? '').trim().toUpperCase()
	for (const item of UDP_MODEL_INDEX_MAP) {
		for (const m of item.models) {
			if (model.startsWith(m.toUpperCase())) return item.index
		}
	}
	return 0xff
}

/** 扫描总时长上限，超出后强制结束，避免 Promise 悬挂导致后续扫描被互斥锁卡死 */
const SCAN_TIMEOUT_MS = 10000

/** MAC 是否有效（形如 aa:bb:cc:dd:ee:ff 且非全零） */
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
	/** 报文头类型：0x00 主机下发指令，0x01 设备响应，0x02 设备主动上报 */
	static readonly TYPE_COMMAND = 0x00
	static readonly TYPE_RESPONSE = 0x01
	static readonly TYPE_REPORT = 0x02

	/**
	 * 生成扫描（发现）报文
	 * 参考上位机 _gen_discover_packet：index=0x0001, session=0x00000001, cmd=0xFFFF, data=[0xFF]
	 */
	static packDiscover(): Buffer {
		const data = Buffer.from([0xff])
		return this.packCommand(0xffff, data, 0x0001, 0x0001)
	}

	/**
	 * 生成心跳报文：cmd=0xEEEE, data=[Dev_Type(1)] + MAC(6)，共 7 字节。
	 * 与上位机 avm_ccp.py 的 send_heartbeat_instruction 完全一致：
	 *   _cmd = 0xEEEE; _data = [device_type] + mac_addr
	 * 注意：心跳数据只有 Dev_Type + MAC，不含 Param_Vaild（Param_Vaild 仅数据指令用）。
	 */
	static packHeartbeat(deviceType: number, mac: string, index: number = 1, session: number = 1): Buffer {
		const macBytes = Buffer.from(mac.split(':').map((b) => parseInt(b, 16)))
		const data = Buffer.concat([Buffer.from([deviceType]), macBytes])
		return this.packCommand(0xeeee, data, index, session)
	}

	/**
	 * 按 AVMATRIX CCP 协议封包
	 * 字段顺序（与 avm_ccp.py command_data_packing 一致）：
	 * 包头(2) 版本(2) 总长(2) 序号index(2) 填充(8) 类型(1) cmd(2) session(4) 数据长度(2) 数据 校验和(2) 包尾(2)
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

		packet.writeUInt16BE(0xa55a, offset) // 包头
		offset += 2
		packet.writeUInt16BE(0x0100, offset) // 版本
		offset += 2
		packet.writeUInt16BE(totalLength, offset) // 总长度
		offset += 2
		packet.writeUInt16BE(index, offset) // 数据包序号
		offset += 2
		offset += 8 // 8字节填充
		packet.writeUInt8(type, offset) // 报文类型
		offset += 1
		packet.writeUInt16BE(cmd, offset) // 指令值
		offset += 2
		packet.writeUInt32BE(session, offset) // session
		offset += 4
		packet.writeUInt16BE(data.length, offset) // 数据长度
		offset += 2
		data.copy(packet, offset)
		offset += data.length

		let checksum = 0
		for (let i = 0; i < offset; i++) {
			checksum += packet[i]
		}
		packet.writeUInt16BE(checksum & 0xffff, offset)
		offset += 2
		packet.writeUInt16BE(0xa66a, offset) // 包尾

		return packet
	}
}

export class UDPParser {
	/**
	 * 参考上位机解析逻辑（avm_ccp.py packet_parser）：
	 * - 上位机不校验包头，直接解析
	 * - 设备返回的响应包头是 0x5AA5，而我们发送的是 0xA55A
	 * - 校验：总长度 == 实际长度，且数据长度 == 总长度 - 29，最后比对校验和
	 */
	static parse(data: Buffer): ParsedPacket | null {
		if (data.length < 29) {
			return null
		}

		// 设备响应包头是 0x5AA5，不强制校验包头
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

		// 与上位机一致：数据长度必须严格等于总长度减 29
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

		// 字段偏移与参考上位机 (avm_ccp.py) 一致
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
	 * 解析心跳(0xEEEE)回包的数据（参考 PSV0617 文档 3.3.3）：
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
	onLog?: (level: 'info' | 'error' | 'debug', message: string) => void
}

export interface DeviceCallback {
	session: number
	cmd: number
	callback: (data: Buffer) => void
}

export class CommunicationManager {
	private udp: UDPHelper | undefined
	private discoverySocket: dgram.Socket | undefined
	private options: CommunicationOptions
	private isConnected = false
	private discoveredDevices: Map<string, DeviceInfo> = new Map()
	/** 当前连接的目标设备信息 */
	private connectedDevice: DeviceInfo | undefined
	private callbacks: DeviceCallback[] = []
	private sessionCounter = 1
	/** 报文序号，参考上位机 _index，每发一条指令自增 */
	private indexCounter = 0
	private heartbeatTimer: NodeJS.Timeout | undefined
	private heartbeatMissed = 0
	private maxHeartbeatMissed = 3
	private onStatusChangeCallback: ((status: InstanceStatus, message?: string) => void) | undefined
	private onDataCallback:
		| ((data: Buffer, host: string, port: number, cmd?: number, session?: number) => void)
		| undefined
	private onErrorCallback: ((error: Error) => void) | undefined
	private onLogCallback: ((level: 'info' | 'error' | 'debug', message: string) => void) | undefined
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
		this.log('info', '========================================')
		this.log('info', 'Starting UDP connection to device')
		this.log('info', `Host: ${this.options.host}`)
		this.log('info', `Port: ${this.options.port}`)
		this.log('info', '========================================')
		this.disconnect()
		this.setupUDP()
	}

	public disconnect(): void {
		this.log('info', 'Disconnecting from device')
		this.stopHeartbeat()
		if (this.udp) {
			this.udp.destroy()
			this.udp = undefined
		}
		if (this.discoverySocket) {
			this.discoverySocket.close()
			this.discoverySocket = undefined
		}
		this.isConnected = false
		this.callbacks = []
	}

	public async sendCommand(cmd: number, data: Buffer): Promise<boolean> {
		if (!this.isConnected) {
			const error = new Error('Not connected')
			this.log('error', error.message)
			this.onErrorCallback?.(error)
			return false
		}

		try {
			const session = this.sessionCounter++
			const packet = UDPPacker.packCommand(cmd, data, ++this.indexCounter, session)

			if (this.udp) {
				this.log(
					'info',
					`[Send] Command: 0x${cmd.toString(16).padStart(4, '0')}, Session: ${session}, Length: ${packet.length} bytes`,
				)
				// 打印发出的整包数据（hex），便于排查设备无响应的问题
				this.log('info', `[Send] Packet hex: ${packet.toString('hex')}`)
				this.log('debug', `[Send] Target: ${this.options.host}:${this.options.port}`)
				void this.udp.send(packet)
				return true
			}
			return false
		} catch (error) {
			this.log('error', `Send failed: ${(error as Error).message}`)
			this.onErrorCallback?.(error as Error)
			return false
		}
	}

	public async sendCommandWithCallback(
		cmd: number,
		data: Buffer,
		callback: (response: ParsedPacket) => void,
	): Promise<boolean> {
		if (!this.isConnected) {
			this.log('error', 'Not connected')
			return false
		}

		const session = this.sessionCounter++
		const packet = UDPPacker.packCommand(cmd, data, ++this.indexCounter, session)

		this.callbacks.push({
			session,
			cmd,
			callback: (rawData) => {
				const parsed = UDPParser.parse(rawData)
				if (parsed) {
					callback(parsed)
				}
			},
		})

		try {
			if (this.udp) {
				void this.udp.send(packet)
				this.log('info', `Sent command with callback: 0x${cmd.toString(16).padStart(4, '0')}, session: ${session}`)
				return true
			}
			return false
		} catch (error) {
			this.log('error', `Send failed: ${(error as Error).message}`)
			return false
		}
	}

	public async send(data: string | Buffer): Promise<boolean> {
		const buffer = typeof data === 'string' ? Buffer.from(data) : data
		return this.sendCommand(0x0001, buffer)
	}

	/**
	 * 获取所有 IPv4 网络接口的子网广播地址
	 * 与上位机一致：为每个接口计算正确的广播地址
	 */
	/**
	 * 参考上位机实现：
	 * 上位机使用 socket.getaddrinfo(hostname, None) 获取每个IPv4接口的IP地址
	 * 然后为每个接口创建独立的 AvmScannerPhy，绑定到该接口IP并系统分配端口
	 * 所有接口都向 255.255.255.255:7000 发送广播
	 *
	 * Node.js中我们使用 os.networkInterfaces() 获取接口信息
	 * 关键：绑定到接口IP而不是0.0.0.0，这样Windows会走正确的网卡
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
	 * 扫描网络发现设备
	 * 参考上位机实现：为每个网络接口创建独立的socket，绑定到接口IP，向255.255.255.255广播
	 */
	public async scanNetwork(): Promise<void> {
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

		// 参考上位机：每个接口创建独立socket，绑定到接口IP，系统分配端口
		// 所有socket都向 255.255.255.255:7000 发送广播
		return new Promise((resolve) => {
			// 兜底超时：避免 socket bind 回调未触发等原因导致 Promise 永不结束
			let settled = false
			const finish = () => {
				if (settled) return
				settled = true
				clearTimeout(timeoutHandle)
				resolve()
			}
			const timeoutHandle = setTimeout(() => {
				this.log('warn', `[Scan] Discovery timed out after ${SCAN_TIMEOUT_MS}ms`)
				if (this.discoverySocket) {
					this.discoverySocket.close()
					this.discoverySocket = undefined
				}
				finish()
			}, SCAN_TIMEOUT_MS)

			try {
				const broadcastTarget = '255.255.255.255'
				const discoverPacket = UDPPacker.packDiscover()
				this.log('debug', `[Scan] Scan packet size: ${discoverPacket.length} bytes`)
				this.log('debug', `[Scan] Send discovery packet (cmd=0xFFFF, data=[FF]) -> ${broadcastTarget}:${scanPort}`)
				this.log('debug', `[Scan] Packet hex: ${discoverPacket.toString('hex')}`)

				// 为每个网络接口创建独立的socket
				const sockets: dgram.Socket[] = []

				const onMessage = (msg: Buffer, rinfo: dgram.RemoteInfo) => {
					this.log('debug', `[Scan] Discovery response from ${rinfo.address}:${rinfo.port}, size=${msg.length} bytes`)
					this.log('debug', `[Scan] Response hex: ${msg.toString('hex')}`)

					const parsed = UDPParser.parse(msg)
					if (!parsed) {
						this.log('warn', '[Scan] Invalid discovery response - parse failed')
						return
					}

					this.log(
						'debug',
						`[Scan] Parsed header - type: 0x${parsed.type.toString(16)}, cmd: 0x${parsed.cmd.toString(16)}, session: ${parsed.session}, dataLen: ${parsed.data.length}`,
					)

					// 发现响应应该是 cmd=0xFFFF 的响应
					if (parsed.cmd !== 0xffff) {
						this.log('debug', `[Scan] Ignoring non-discovery response cmd=0x${parsed.cmd.toString(16)}`)
						return
					}

					// 逐字段打印设备信息解析过程，便于排查型号识别问题
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

					const modelIndex = getUdpModelIndex(deviceInfo.model)
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
						// 仅首次发现时打印，避免同一设备被重复响应时刷屏（看起来像重复扫描）
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
					// 没有检测到接口，使用0.0.0.0兜底
					this.log('warn', 'No interfaces detected, falling back to 0.0.0.0')
					this.discoverySocket = dgram.createSocket({ type: 'udp4', reuseAddr: true })
					this.discoverySocket.on('message', onMessage)
					this.discoverySocket.on('error', onError)
					this.discoverySocket.bind(0, '0.0.0.0', () => {
						this.sendDiscoveryScans([this.discoverySocket!], discoverPacket, scanPort, broadcastTarget, finish)
					})
				} else {
					// 为每个接口创建socket
					let boundCount = 0
					for (const iface of interfaceAddrs) {
						const sock = dgram.createSocket({ type: 'udp4', reuseAddr: true })
						sock.on('message', onMessage)
						sock.on('error', onError)

						// 绑定到接口IP，系统自动分配端口（与上位机一致）
						sock.bind(0, iface.address, () => {
							const addr = sock.address()
							this.log('debug', `Socket bound to [${iface.iface}] ${addr.address}:${addr.port}`)
							sock.setBroadcast(true)
							sockets.push(sock)
							boundCount++

							// 所有socket绑定完成后开始发送
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
	 * 发送扫描包（2轮，间隔1秒）
	 * @param finish 结束回调，负责清理兜底超时并 resolve
	 */
	private sendDiscoveryScans(
		sockets: dgram.Socket[],
		packet: Buffer,
		scanPort: number,
		broadcastTarget: string,
		finish: () => void,
	): void {
		const maxScans = 4 // 与上位机 Scanner._MAX_TIMES 一致，提高发现可靠性
		let scanCount = 0

		const sendScan = () => {
			if (scanCount >= maxScans) return
			scanCount++
			const currentScan = scanCount

			// 每个socket都发送广播包
			let sentCount = 0
			for (const sock of sockets) {
				sock.send(packet, 0, packet.length, scanPort, broadcastTarget, (err) => {
					if (err) {
						this.log('error', `Scan ${currentScan}/${maxScans} failed: ${err.message}`)
					} else {
						const addr = sock.address()
						this.log(
							'debug',
							`Scan ${currentScan}/${maxScans} sent from ${addr.address}:${addr.port} -> ${broadcastTarget}:${scanPort}`,
						)
					}
					sentCount++
					// 所有socket发送完毕，1秒后发下一轮
					if (sentCount >= sockets.length && currentScan < maxScans) {
						setTimeout(sendScan, 1000)
					}
					// 最后一轮发送完毕，等待响应后结束
					if (sentCount >= sockets.length && currentScan === maxScans) {
						setTimeout(() => {
							this.log('debug', '========================================')
							this.log('info', `[Scan] Discovery complete - Found ${this.discoveredDevices.size} device(s)`)
							for (const [key, dev] of this.discoveredDevices) {
								this.log(
									'debug',
									`[Scan]   [${key}] model="${dev.model}" type=${getProductTypeName(dev.productType)} name="${dev.name}" at ${dev.host}:${dev.port}`,
								)
							}
							this.log('debug', '========================================')

							for (const sock of sockets) {
								sock.close()
							}
							this.discoverySocket = undefined
							finish()
						}, 1500)
					}
				})
			}
		}

		sendScan()
	}

	public startHeartbeat(): void {
		this.stopHeartbeat()
		this.heartbeatMissed = 0

		// 立即探测一次，避免等待一个完整周期才知道设备是否在线
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
	 * 存活探测（心跳）——参考上位机 UDP 流程：
	 * 心跳指令 0xEEEE，数据 = [Dev_Type(1)] + MAC(6)，序号自增、session 随机，
	 * 单播直接发给当前目标设备（对应上位机的 DevicePhy）。
	 *
	 * 连接是 UDP（无连接），socket 就绪不代表在线：收到任意合法报文即视为在线。
	 */
	private async sendHeartbeat(): Promise<void> {
		const device = this.connectedDevice
		if (!device) {
			this.log('debug', 'Heartbeat skipped - no target device selected')
			return
		}

		try {
			if (!this.udp) return

			const useHeartbeat = isValidMac(device.mac)
			// 参考样例：心跳 index=1、session=1 固定
			const packet = useHeartbeat
				? UDPPacker.packHeartbeat(device.udpType ?? 0xff, device.mac, 1, 1)
				: UDPPacker.packCommand(0xffff, Buffer.from([0xff]), 1, 1)

			this.log(
				'info',
				`[Heartbeat] Probe -> ${this.options.host}:${this.options.port} (${useHeartbeat ? '0xEEEE' : '0xFFFF'}), misses=${this.heartbeatMissed}`,
			)

			// 设备无响应时，打印本次发送的完整报文（hex），便于排查
			if (this.heartbeatMissed > 0) {
				this.log(
					'info',
					`[Heartbeat] No response (misses=${this.heartbeatMissed}) - sent packet: ${packet.toString('hex')}`,
				)
			}

			await this.udp.send(packet)
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
			this.log('error', `Heartbeat send failed: ${(error as Error).message}`)
		}
	}

	/**
	 * 收到设备的任意合法报文即认定设备在线：
	 * 清零失败计数，并把状态从「连接中 / 已断开」恢复为在线。
	 */
	private markDeviceAlive(): void {
		const wasMissed = this.heartbeatMissed
		this.heartbeatMissed = 0

		if (!this.isConnected) {
			this.isConnected = true
			this.log('info', `[Heartbeat] Device ${this.options.host} responded, connection online`)
			this.onStatusChangeCallback?.(InstanceStatus.Ok, 'Device responded')
		} else if (wasMissed > 0) {
			this.log('debug', `[Heartbeat] Device responded, miss counter reset (was ${wasMissed})`)
		}
	}

	public getDiscoveredDevices(): DeviceInfo[] {
		return Array.from(this.discoveredDevices.values())
	}

	/**
	 * 设置当前连接的目标设备（用于日志展示与协议参数）。
	 * 同时重置探测计数，让新目标从干净的计数开始。
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
		this.log('info', 'Initializing UDP Helper...')
		this.udp = new UDPHelper(this.options.host, this.options.port)
		this.log('info', `UDP Helper created for ${this.options.host}:${this.options.port}`)

		this.udp.on('status_change', (status, message) => {
			this.log('info', `UDP status_change - Status: ${status}, Message: ${message || 'none'}`)

			if (status === InstanceStatus.Ok) {
				// UDP 是「无连接」协议：socket 就绪只代表本机端口已绑定，
				// 不代表设备在线。这里先报「连接中」，等设备回包
				// （markDeviceAlive）才真正置为在线。
				this.log('info', `Socket ready for ${this.options.host}:${this.options.port}, probing device...`)
				this.isConnected = false
				this.onStatusChangeCallback?.(InstanceStatus.Connecting, 'Waiting for device response...')
				this.startHeartbeat()
			} else {
				this.log('info', `Connection status: ${status} - ${message}`)
				if (this.isConnected) {
					this.log('error', 'Connection was established but now lost')
				}
				this.isConnected = false
				this.stopHeartbeat()
				this.onStatusChangeCallback?.(status, message)
			}
		})

		this.udp.on('data', (data) => {
			// info 级别打印收到的原始报文，便于确认设备“到底有没有上报”以及上报内容
			this.log('info', `[Recv] ${data.length}B: ${data.toString('hex')}`)
			this.log('debug', '========== RECEIVED DATA START ==========')
			this.log('debug', `Raw data length: ${data.length} bytes`)

			const parsed = UDPParser.parse(data)
			if (parsed) {
				// 收到设备的合法报文即视为在线，用于心跳存活判定与断线恢复
				this.markDeviceAlive()

				// 心跳(0xEEEE)回包：按协议解析 vendor / Product_name / MAC 并打印
				if (parsed.cmd === 0xeeee) {
					const hb = UDPParser.parseHeartbeatReply(parsed.data)
					if (hb) {
						this.log('info', `[Heartbeat] Reply - vendor="${hb.vendor}", name="${hb.productName}", mac=${hb.mac}`)
					} else {
						this.log('info', `[Heartbeat] Reply (raw ${parsed.data.length}B): ${parsed.data.toString('hex')}`)
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
						'info',
						`[Report] Device active report - Cmd: 0x${parsed.cmd.toString(16).padStart(4, '0')}, Session: ${parsed.session}, Data: ${parsed.data.length} bytes`,
					)
					this.log('debug', `[Report] Data hex: ${parsed.data.toString('hex')}`)
					this.reportCallback?.(parsed)
					this.log('debug', 'Device report handled')
				}

				this.onDataCallback?.(parsed.data, this.options.host, this.options.port, parsed.cmd, parsed.session)
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

		this.log('info', 'UDP event listeners registered')
	}

	private log(level: 'info' | 'error' | 'debug' | 'warn', message: string): void {
		this.onLogCallback?.(level === 'warn' ? 'info' : level, message)
	}
}
