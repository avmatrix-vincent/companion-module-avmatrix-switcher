import unittest

class RticeDevice(object):
    """
    配置封包与解析需要用到的工具
    """
    class Util(object):
        @staticmethod
        def calc_sum(data, num):
            sum = 0

            for i in range(num):
                sum += data[i]

            sum = 0xffff & sum
            return sum.to_bytes(2, "big")

    """
    配置包头的参数定义
    """
    class ConfigHeader(object):
        _head = [0xA5]
        _version = 0x0100
        _padding = [0x00] * 8
        _data_max_len = 32

    """
    EDID Flash表名称列表报文打包的类定义
    """
    class EDIDFlashTableNameListPacker(object):
        @staticmethod
        def pack(nameList):
            """
            :param data: 数据
            :param datalen: 数据长度
            :return: 返回封装好的包
            """
            
            # 最长384字节，除去包头识别码1个字节，版本2个字节，校验2个字节，剩下379个字节用于Name List
            # 一共有6个Name List需要存储，每个名称最大长度限定为64字节，共32x6=192，需要填充0的数量为379 - 192
            if not isinstance(nameList, list) or len(nameList) > 6:
                raise ValueError("Name list must be a list with max 6 items")

            for name in nameList:
                if not isinstance(name, str) or len(name.encode('utf-8')) > 32:
                    raise ValueError("Each name must be a string with max 32 bytes")

            data = []
            for name in nameList:
                data += list(name.encode('utf-8')) + [0]*(32 - len(name.encode('utf-8')))

            packet = []
            packet += RticeDevice.ConfigHeader._head
            packet += RticeDevice.ConfigHeader._version.to_bytes(2, "big")
            packet += data
            packet += [0]*(379 - len(data)) # 不足部分填充0
            packet += RticeDevice.Util.calc_sum(packet, 382)

            return packet

    """
    EDID Flash表名称列表报文解包的类定义
    """
    class EDIDFlashTableNameListParser(object):
        @staticmethod
        def parse(packet):
            _packet_len = len(packet)
            if _packet_len != 384:  # 384字节数据
                raise ValueError(f"Packet's length is not equal to 384, length={_packet_len}")

            _head = packet[0]
            if _head != RticeDevice.ConfigHeader._head[0]:
                raise ValueError(f"Packet's head is not {RticeDevice.ConfigHeader._head}, head={_head}")

            _version = int.from_bytes(packet[1:3], byteorder='big')
            _data = packet[3:382]  # 379字节数据

            _sum = int.from_bytes(packet[382:384], byteorder='big')
            _check_sum = int.from_bytes(RticeDevice.Util.calc_sum(packet, 382), byteorder='big')
            if _sum != _check_sum:
                raise ValueError(f"Check sum is error, _sum=0x{_sum:02X}, _check_sum=0x{_check_sum:02X}")

            # 解析6个32字节的名称
            name_list = []
            for i in range(6):
                name_bytes = _data[i*32:(i+1)*32]
                name = bytes(name_bytes).split(b'\x00')[0].decode('utf-8')
                if name:  # 只添加非空名称
                    name_list.append(name)
                else:
                    name_list.append("") # 空字符串用于应用端判断哪个位置有空位

            _data_dict = {
                "version": _version,
                "NameList": name_list
            }

            return _data_dict

class TestEDIDFlashTableNameList(unittest.TestCase):
    def test_pack_and_parse(self):
        # 测试数据：一个示例表名列表
        table_names = ["table1", "table2", "table3"]

        # 打包测试
        packer = RticeDevice.EDIDFlashTableNameListPacker()
        packed_data = packer.pack(table_names)

        print("packed_data:", packed_data)
        self.assertIsInstance(packed_data, list, "Packed data should be list")

        # 解析测试
        parser = RticeDevice.EDIDFlashTableNameListParser()
        parsed_names = parser.parse(packed_data)["NameList"]
        self.assertEqual(parsed_names, table_names + ['', '', ''], "Parsed names should match original names")

    def test_empty_list(self):
        # 测试空列表
        packer = RticeDevice.EDIDFlashTableNameListPacker()
        packed_data = packer.pack([])

        print("packed_data:", packed_data)
        
        parser = RticeDevice.EDIDFlashTableNameListParser()
        parsed_names = parser.parse(packed_data)["NameList"]
        self.assertEqual(parsed_names, ['', '', '', '', '', ''], "Parsed names should be 6 empty name list")

    def test_invalid_data(self):
        # 测试无效数据
        parser = RticeDevice.EDIDFlashTableNameListParser()
        with self.assertRaises(ValueError, msg="Invalid data should raise ValueError"):
            parser.parse(b"invalid_data")

if __name__ == "__main__":
    unittest.main()