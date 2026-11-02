/**
 * 原始报文（hex）日志开关。
 *
 * - 发布 / 打包：保持 false —— 收发的数据包内容不写入日志，避免协议细节外泄。
 * - 本地抓包调试：把下面的默认值改成 true，或启动前设置环境变量 AVM_LOG_RAW_PACKETS=1。
 *
 * 只影响“原始字节”的打印；命令码、长度、解析后的字段值等诊断日志不受影响。
 */
export const LOG_RAW_PACKETS = process.env?.AVM_LOG_RAW_PACKETS === '1'

/** 拼接原始报文（hex）；开关关闭时返回空字符串，调用方据此省略该段 */
export function hexOf(buf: Buffer | undefined): string {
	if (!LOG_RAW_PACKETS || !buf) return ''
	return buf.toString('hex')
}
