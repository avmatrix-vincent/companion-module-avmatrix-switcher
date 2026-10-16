from src.avm_stack.usb_stack.packet.data_checker import DataChecker


class Packer(object):
    __packet_head = [0xa5, 0x6c]
    __packet_unknow = [0x81, 0x01, 0x03]
    __packet_data_max_len = 512
    __packet_tail = 0xae

    @staticmethod
    def paging_packet(page, cmd, data, datalen):
        """
        :param page: 分页序号
        :param cmd: 指令值
        :param data: 数据
        :param datalen: 数据长度
        :return: 返回封装好的报文
        """
        packet_data_len = 17 + datalen + 3
        zero_fill_len = 576 - packet_data_len
        packet = []
        packet += Packer.__packet_head
        packet += packet_data_len.to_bytes(2, "little")
        packet += Packer.__packet_unknow
        packet += page.to_bytes(2, "little")
        packet += ([0x00] * 7)
        packet += cmd.to_bytes(1, "little")
        packet += data
        packet += DataChecker.calc_sum(packet, packet_data_len - 3)
        packet += Packer.__packet_tail.to_bytes(1, "little")
        packet += [0x00] * zero_fill_len


        return packet

    @staticmethod
    def command_packet(cmd):
        page = 0
        data = [0x00] * Packer.__packet_data_max_len
        packet = Packer.paging_packet(page, cmd, data, Packer.__packet_data_max_len)

        return packet