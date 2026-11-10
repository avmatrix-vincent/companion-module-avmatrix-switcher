/**
 * Raw packet (hex) logging switch.
 *
 * - Release / packaged build: keep false, so packet contents are never written to the log.
 * - Local debugging: set the default below to true, or set AVM_LOG_RAW_PACKETS=1 before start.
 *
 * Only raw bytes are affected; command codes, lengths and parsed field values are always logged.
 */
export const LOG_RAW_PACKETS = process.env?.AVM_LOG_RAW_PACKETS === '1'
