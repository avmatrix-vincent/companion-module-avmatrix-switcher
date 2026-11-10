## Avmatrix Switcher

Control Avmatrix switchers from Companion over UDP.

### Supported devices

- SHARK S6 (VS0605)
- SHARK S6 PLUS (VS0617)
- SHARK S5 (VS0405E)
- SHARK H5 (VS0405EH)
- SHARK H4K
- SHARK H4K PLUS
- Other Avmatrix models using the same UDP protocol may work as well

### Device differences

The SHARK H4K and H4K PLUS use a reduced feature set:

- 4 inputs and a single PIP layer (no PIP2 / PIP3)
- 3 wipes (no WIPE4)
- No streaming (Stream 1-3)
- No XLR / Line In inputs, no All AFV and no global Audio Reset

### Configuration

- **Device**: pick a switcher discovered automatically on the local network. Companion scans with UDP broadcast and lists every device that answers. If nothing is found the list shows `No supported device found`.
- **Target IP**: IP address of the switcher. It is filled in from the selected device, but can also be entered manually, which is useful when the device is on another subnet and cannot be discovered.
- **Manual Device Model**: off by default, so the model detected by the scan is always used. Turn it on to always use the model selected below, even when the device is found by the scan; this is needed when you type a Target IP for a device that cannot be discovered. Select the model that matches the hardware (for example SHARK H4K) so the correct protocol is used.

Device control always uses **UDP port 7000**; it is not configurable.

Companion and the switcher must be on the same network, and the host firewall must allow outgoing UDP traffic to port 7000 as well as the broadcast replies.

### Usage

1. Add the connection, select your device (or type its IP) and save.
2. The status turns green once the module receives a heartbeat from the device.
3. Use the bundled presets, or build your own actions and feedbacks. Feedbacks follow the state reported by the switcher, so buttons also update when changes are made on the hardware control panel.

### Troubleshooting

- **Status stays disconnected**: check the IP, make sure UDP port 7000 is not blocked, and confirm no other application is controlling the device on the same port.
- **Device list is empty**: broadcast traffic may be filtered by the network (VLAN/firewall). Enter the IP manually instead.
- **Button state does not update**: some firmware versions only report state after a change. Verify the device answers the periodic query commands in the Companion log.

For issues and feature requests, use the GitHub issue tracker of this repository.
