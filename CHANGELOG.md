# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Planned

- **NR1**: plan the move to `@companion-module/base` v2.x (Companion 4.3+ / 5.0+) to gain expression support and the latest module API.

## [1.0.2] - 2026-11-09

Fixes for the issues raised in the v1.0.1 review.

### Fixed

- **H2**: wrap the 16-bit packet index (and the 32-bit session id) so commands keep working after 65,535 packets.
- **Manual IP**: added a "Manual Device Model" switch (off by default, so the scan is always used). When enabled, the selected model always wins over the scan result; this fixes a typed Target IP that cannot be discovered falling back to the S6 PLUS (0617) protocol, which made every action fail silently on a SHARK H4K. A warning is logged when the switch is on without a model.
- **M1**: restart the heartbeat when the device comes back, so a later dropout is still detected.
- **L1**: keep the active scanner on the instance and abort a running scan (timers and sockets) from `destroy()` / `disconnect()`.
- **Scan timeout**: the 10 s safety timeout now aborts through `abortScan()` (sets the abort flag, clears round timers and closes sockets), and `sendScan()` catches synchronous `dgram` errors, so a late round can no longer send on a closed socket and crash the module.
- **L2**: register the short follow-up timers started by button presses and clear them in `destroy()`; stop the query loops once the instance is gone.
- **L3**: build the PIP1/2/3 Adjust and LUMA Adjust presets from the active protocol (H4K defaults to IN1 as the PIP source and Clip 0).
- **L4**: include the IP address in the Device dropdown labels so two units of the same model can be told apart.
- **L5**: list every supported model (S6, S6 PLUS, S5, H5, H4K, H4K PLUS) in HELP.md and the manifest keywords.
- **L6**: log `[Report 0x0110]`, `[Switch]`, `[Set]`, `[Report]`, `[Reply]` and `[Query Reply]` at debug level; H4K reports are no longer handled twice.
- **L7**: pass the action-flash key explicitly instead of keeping it in shared state, so concurrent actions flash the correct button.
- **Build errors**: `sendToDevice()` now catches `buildCommand()` failures and returns false instead of rejecting the action callback (same crash class as the v1.0.0 H1 fix).
- **N2**: the Last Action (Flash) key option now resolves variables.
- **N4**: removed unused code (`sendCommandWithCallback`, `send`, `hexOf`, the unused key-value tables, unused DeviceCommands entries and the unused preset `flashKey` field) and the remaining non-null assertion.

### Changed

- **M2**: action options now store device-independent key ids (`pgm1`, `cut`, `stream2`, `pip_on_air`, ...), mapped to the active protocol key map when sent. Presets use the same ids, so buttons keep pressing the same logical key after a profile change.
- **N1**: renamed the action id `audio_mic_pregate` to `audio_mic_pregain`, renamed "Transition MIX / DIP" to "Transition MIX / DIP / FREEZE", and made the LOGO Select labels 1-based.
- **N3**: PGM/PVW and WIPE feedback dropdowns are built from the protocol capabilities (input and wipe counts); action descriptions no longer show protocol hex codes or fixed ranges.
- **H1**: all code comments, action and feedback text, log messages, the CHANGELOG and HELP.md are now in English.

### Notes

- Outside the H4K family, behaviour is kept equivalent for `avm-0617` (SHARK S6 PLUS / S5 / H5) and `avm-0605` (SHARK S6).
- v1.0.0 N2 (zero-width characters ordering the preset categories) is intentionally kept.

## [1.0.1] - 2026-11-02

Fixes for the issues raised in the `companion-module-avmatrix-switcher v1.0.0` review (`review-avmatrix-switcher-v1.0.0-20261030-090507`).

### Security

- **C1**: added the template's supply-chain hardening to `.yarnrc.yml`: `enableScripts: false`, `npmMinimalAgeGate: 3d` and `npmPreapprovedPackages: ["@companion-module/*"]`, preventing install scripts and blocking versions published less than 3 days ago.

### Fixed

- **H1**: `sendCommand()` / `sendCommandWithCallback()` now `await this.udp.send(...)`; a failed send (link down / unreachable route) no longer becomes an unhandled rejection that crashes Node 22, but is caught and returns `false`.
- **H2**: with a manually typed Target IP (other subnet, not discovered), the heartbeat no longer skips sending; it keeps probing with the family `probeCommand` or the `0xFFFF` discovery packet and switches to Connection Failure after consecutive misses.
- **H3**: the start-up scan only auto-selects a device on first setup (Device and Target IP both empty); otherwise it only refreshes the device list and keeps the selected device / manually typed Target IP.
- **M1**: the UDP sockets created per network interface during a scan are tracked in `scanSockets` and closed on `disconnect()` and on timeout, fixing the post-destroy send/listen and the failed-scan leak.
- **M2**: added `connectedHost`; `configUpdated()` now compares against the actually connected host, fixing "changing Target IP back to the Device value still sends to the old address".
- **M3**: a failed heartbeat send also counts as a miss, so the status turns to Connection Failure when the Companion host loses the network instead of staying green.
- **M4**: an empty scan result no longer clears `discoveredDevices`, keeping the previous device list and MAC/model info.
- **M5**: with no device and no Target IP, the status becomes `BadConfig` (asking for a Target IP) instead of staying in Connecting forever.
- **M6**: presets stay registered after `init()` / `applyDeviceProfile()` and are no longer cleared with `setPresetDefinitions({})` on connection changes.
- **L1**: `destroy()` clears the 400 ms action-flash timer `flashTimer`.
- **L2**: reset the `blinkOn` phase on disconnect/reconnect and call `updateBlink()` when back online, fixing FTB/MUTE/Freeze no longer blinking after a reconnect.
- **L3**: call `updateBlink()` after locally toggling FTB/MUTE/Freeze, fixing "steady light, no blink".
- **L4**: AUTO is treated as a momentary action: it lights briefly and is released automatically, fixing the always-on and inverted state.
- **L5**: `moveTBar()` refuses to run while disconnected; a failed send rolls back the local base and does not update the display variables; `tbar_value` is written only after a successful send.
- **L6**: corrected the example key of the "Last Action (Flash)" feedback to the real format (`set_source|source=5`, and `key:NN` for reports).
- **L7**: PIP/LUMA/CHROMA/DSK/LOGO status feedbacks use readable names and have a `description`; `connection_status` is renamed to "Device Disconnected" and documents its meaning.
- **L8**: removed the ineffective `$(self:tbar_value)` static text from the T-Bar Move action and replaced it with an explanation.
- **L9**: translated the config tooltips (Device / Target IP) to English.
- **L10**: removed the unpublished `legacyIds: ["szavm"]` from `companion/manifest.json`.
- **L11**: lowered traffic logs such as `[Recv]`, `[Send]`, `[Heartbeat]` and `[Report]` to `debug`; `warn` is no longer downgraded to `info`, greatly reducing run-time log noise.

### Changed

- **N1**: tightened types: `handleDeviceReport(packet: ParsedPacket)`, `getDeviceState(): DeviceState` (new `DeviceState` interface), improving type safety of the report path.

### Notes

- **N2** (zero-width characters ordering preset categories): **intentionally kept**. Removing it would make the preset group order depend on Companion's rendering and risk a regression, so it is left unchanged.
- No network or lifecycle change touched the protocol command tables, key maps or state layouts of `avm-0617` (SHARK S6 PLUS / S5 / H5) or `avm-0605` (SHARK S6); the old families behave exactly as before.

### Review follow-up

| ID  | Fix                                                                            | Key change                                                          |
| --- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| C1  | `.yarnrc.yml` supply-chain hardening                                           | `enableScripts` / `npmMinimalAgeGate` / `npmPreapprovedPackages`    |
| H1  | a failed send no longer crashes the process                                    | `await udp.send()` inside `try/catch`                               |
| H2  | a manual IP can connect                                                        | probe is still sent (and counted as a miss) without a target device |
| H3  | the start-up scan no longer takes over the connection / overwrites a manual IP | only first setup auto-selects a device                              |
| M1  | scan socket leak                                                               | `scanSockets` closed together                                       |
| M2  | Target IP change still sent to the old address                                 | reconnect decided by `connectedHost`                                |
| M3  | status stayed green without a network                                          | a failed send also counts as a miss                                 |
| M4  | an empty scan cleared the device list                                          | only overwrite when non-empty                                       |
| M5  | no device and no IP stayed in Connecting                                       | `BadConfig` status is reported                                      |
| M6  | presets vanished with the online state                                         | no more `setPresetDefinitions({})`                                  |
| L1  | flash timer was not released                                                   | `destroy()` clears `flashTimer`                                     |
| L2  | blinking stopped after a reconnect                                             | reset `blinkOn` + `updateBlink()`                                   |
| L3  | local press stayed solid                                                       | `updateBlink()` after the flip                                      |
| L4  | AUTO stayed on / state inverted                                                | momentary highlight, released automatically                         |
| L5  | T-Bar variable changed before sending                                          | variable written only on success, rolled back on failure            |
| L6  | wrong example key in the flash feedback                                        | real key format                                                     |
| L7  | feedbacks shown by internal id                                                 | readable names + `description`                                      |
| L8  | literal `$(self:tbar_value)` shown                                             | replaced with an explanation                                        |
| L9  | config tooltips were in Chinese                                                | translated to English                                               |
| L10 | legacyId declared on first release                                             | `szavm` removed                                                     |
| L11 | packet/heartbeat info noise and duplicate handling                             | lowered to `debug`, `warn` passes through                           |
| N1  | loose typing                                                                   | `ParsedPacket` / `DeviceState`                                      |
| N2  | zero-width ordering                                                            | intentionally kept (avoids category reordering)                     |
| NR1 | base v2.x migration                                                            | planned for a later release                                         |

## [1.0.0] - 2026-10-30

### Added

- First release.
- Control Avmatrix switchers over UDP (port 7000).
- Support for SHARK S6 (VS0605) and SHARK S6 PLUS (VS0617), plus other models using the same UDP protocol.
- Automatic device discovery via UDP broadcast, with a manually typed Target IP for other subnets.
- Actions, feedbacks and presets for PGM / PVW sources, CUT / AUTO / FTB / MUTE, PIP / LUMA / CHROMA / DSK / LOGO, transitions (WIPE) and T-Bar.
- State follows the device reports, so button feedback also updates when the hardware panel is used.

### Notes

- This release was reviewed by Bitfocus with the verdict "Changes Required"; the fixes are in [1.0.1].
