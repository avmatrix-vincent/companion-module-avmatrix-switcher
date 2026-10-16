import logging
import os
import platform
import sys
import ctypes
import threading
import traceback
from globals import relative_path
from src.model.modelRticePreferences import ModelRticePreferences

_str_error_map = {
    0: 'ecOK: Everything is ok',
    1: 'ecInitFail: fail to init sdk',
    2: 'ecNoIoInstance: Missing or fail to create instance of io',
    3: 'ecUnkownConnect: connect type is not supported',
    4: 'ecNoFoundDevice: Can\'t find the device',
    5: 'ecOpenDevice: fail to open the device identified by given name',
    6: 'ecCloseDevice: fail to close the device',
    7: 'ecEnterDebugMode: fail to force chip entering debug mode',
    8: 'ecReadRBus: fail to read value at the given address in chip',
    9: 'ecWriteRBus: fail to write value to the given address in chip',
    10: 'ecATCommand0: fail to send at comf',
    11: 'ecBurnFail: fail to burn file to flash',
    12: 'ecBurnType: Unknown burn type',
    13: 'ecEdidToFlashFail: fail to burn edid to to flash',
    14: 'ecFileUnExisted: File doesn\'t exist',
    15: 'ecEmcuSendFail: At command send ok but emcu send error',
    16: 'ecAPPUnExisted: function doesn\'t exist',
    17: 'ecAlignmentError: Alignment is error',
    18: 'ecGPIOSendFail: At command send ok but gpio send error',
    19: 'ecLSADCSendFail: At command send ok but lasdc send error',
    20: 'ecPWMSendFail: At command send ok but pwm send error',
    21: 'ecRestoreToDefaultFail: ',
    22: 'ecUnknonwPCB: SDK doesn\'t match PCB',
    23: 'ecUnkown: Unknown error',
    24: 'ecAuxVoulumFail: At command send ok but Aux send error',
    25: 'ecBinFail: Read Bin Length is not enough',
    26: 'ecFWVersionUnMatched: FW Verison is not matched',
}

# check a library function call
def _check(ret):
    if hasattr(ret, 'value'):
        ret = ret.value

    return ret

def _error_args(error_code=-1, error_desc=""):
    _args = {
        "Result": False,
        "ErrorCode": error_code,
        "ErrorDescription": error_desc
    }
    return _args

def _setup_prototypes(lib):
    # int initialize()
    lib.initialize.argtypes = []

    # int uninitialize()
    lib.uninitialize.argtypes = []

    # int openPort()
    lib.openPort.argtypes = []

    #int setPort(ENUM_CONNECT_TYPE connect, const char ∗ name)
    lib.setPort.argtypes = [ctypes.c_uint8, ctypes.c_char_p]

    # int closePort()
    lib.closePort.argtypes = []

    #
    lib.AT2_Get_Customer_Ver_Example.argtypes = [ctypes.c_void_p]

    #
    lib.AT2_EDID_Flash_Get_Default_table_Example.argtypes = [ctypes.POINTER(ctypes.c_uint8)]

    lib.AT_Audio_Get_HdmiRX_AudioFormat.argtypes = [ctypes.POINTER(ctypes.c_uint8)]

    lib.AT_UVC_Get_Output_Timing.argtypes = [ctypes.c_void_p]

    lib.AT_USB_Get_SerialNum.argtypes = [ctypes.c_char_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32)]

class _lib_CustomerVersion_T2(ctypes.Structure):
    _fields_ = [("version", (ctypes.c_char*128))]

class _lib_Audio_Volume_T(ctypes.Structure):
    _fields_ = [("gain", ctypes.c_int16)]

class _lib_AT_UVC_Output_Timing_T(ctypes.Structure):
    _fields_ = [("weight", ctypes.c_uint32),
                ("height", ctypes.c_uint32),
                ("freq", ctypes.c_uint32)]

class _lib_AT_SQE_COLOR_CTRL_CMD_T(ctypes.Structure):
    _fields_ = [("TargetPos", ctypes.c_uint8),
                ("Value", ctypes.c_uint8)]

class _lib_AT_HDMI_TIMING_INFO_T(ctypes.Structure):
    """
    typedef struct {
        UINT8   is_interlace : 1;       ///< 0: progressive, 1: interlace
        UINT8   pixel_repeat : 3;
        UINT8   polarity : 2;
        UINT8   run_dsc : 2;            ///< 0: do not run dsc flow, 1: run dsc flow
        AT_VSYNC_MODE_T   run_vrr;      ///< 0: non VRR, 1: HDMI Forum VRR, 2: Freesync, 3: Adaptive sync
        UINT16  vTotal;                 ///< vTotal Vertical total
        UINT16  hTotal;                 ///< hTotal Horizon total
        UINT16  vActive;                ///< Active information ( x, y, w, h)
        UINT16  hActive;                ///< Active information ( x, y, w, h)
        UINT16  vStart;                 ///< v start point
        UINT16  hStart;                 ///< h start point
        UINT16  vFreq;                  ///< vFreq Vertical frequency
        UINT16  hFreq;                  ///< hFreq Horizon frequency
        AT_DR_MODE_T dr_mode;           ///< 0x0: SDR, 0x1: HDR10, 0x11: HLG; 0x20: HDR10PLUS ; 0x30: Dolby_Vision STD, 0x31: Dolby Vision Low Latency,  0x32: Dolby Vision VSEM.
        UINT16  IVSyncPulseCount;       ///< Input VSYNC High Period Measurement Result
        UINT16  IHSyncPulseCount;       ///< Input HSYNC High Period Measurement Result
        AT_DVI_MODE_T     mode;         ///< 0: DVI mode, 1: HDMI14/20 mode, 2: HDMI21 mode, 3: DRPX mode, 4: Unknow
        AT_COLOR_DEPTH_T colordepth;    ///< 0: 8bit, 1:10bit, 2:12bit, 3:16bit, 4: 6bit
        AT_COLOR_SPACE_T colorspace;    ///< 0: RGB, 1: YUV422, 2: YUV444, 3: YUV420, 4: YUV400(Y ONLY)
        AT_COLOR_RGB_YUV_RANGE_MODE_T colorrange; ///< 0: default, 1: limit, 2: full, 3: unknow
        AT_COLORIMETRY_T  colorimetry;
        UINT8  ext_colorimetry;
        AT_HDMI_HDCP_E  hdcpType;       ///< 0: no hdcp, 1: hdcp13/14, 2: hdcp22/23, 3: HDCP_OFF
        UINT16  tmds_clk_b;
        UINT32  pll_pixelclockx1024;
        UINT32 cur_sys_time;            ///< current system time, Unit is milliseconds
    } AT_HDMI_TIMING_INFO_T;
    """
    _pack_ = 1 # 强制1字节对齐
    _fields_ = [("union1", ctypes.c_uint8),  # bit0: 0: progressive, 1: interlace
                ("run_vrr", ctypes.c_uint8),
                ("vTotal", ctypes.c_uint16),
                ("hTotal", ctypes.c_uint16),
                ("vActive", ctypes.c_uint16),
                ("hActive", ctypes.c_uint16),
                ("vStart", ctypes.c_uint16),
                ("hStart", ctypes.c_uint16),
                ("vFreq", ctypes.c_uint16),
                ("hFreq", ctypes.c_uint16),
                ("dr_mode", ctypes.c_uint8),
                ("IVSyncPulseCount", ctypes.c_uint16),
                ("IHSyncPulseCount", ctypes.c_uint16),
                ("mode", ctypes.c_uint8),
                ("colordepth", ctypes.c_uint8),
                ("colorspace", ctypes.c_uint8), # 0: RGB, 1: YUV422, 2: YUV444, 3: YUV420, 4: YUV400(Y ONLY)
                ("colorrange", ctypes.c_uint8), # 0: default, 1: limit, 2: full, 3: unknow
                ("colorimetry", ctypes.c_uint8),
                ("ext_colorimetry", ctypes.c_uint8),
                ("hdcpType", ctypes.c_uint8), # 0: no hdcp, 1: hdcp13/14, 2: hdcp22/23, 3: HDCP_OFF
                ("tmds_clk_b", ctypes.c_uint16),
                ("pll_pixelclockx1024", ctypes.c_uint32),
                ("cur_sys_time", ctypes.c_uint32) # current system time, Unit is milliseconds
            ]


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
    报文打包的类定义
    """
    class ConfigPacker(object):
        @staticmethod
        def data_packing(data):
            """
            :param data: 数据
            :param datalen: 数据长度
            :return: 返回封装好的包
            """
            

            if len(data) > 27: # 总共32字节，除去包头识别码1个字节，版本2个字节，校验2个字节，剩下27个字节用于data
                raise ValueError("Data's length is more than 27, length=%d" % len(data))

            packet = []
            packet += RticeDevice.ConfigHeader._head
            packet += RticeDevice.ConfigHeader._version.to_bytes(2, "big")
            packet += data
            packet += [0]*(27 - len(data)) # 不足部分填充0
            packet += RticeDevice.Util.calc_sum(packet, 30)

            return packet

    """
    报文解析的类定义
    """
    class ConfigParser(object):
        @staticmethod
        def data_parser(packet):
            _packet_len = len(packet)
            if _packet_len != 32:
                raise ValueError("Packet's length is not equal to 32, length=%d" % _packet_len)

            _head = packet[0]
            if _head != RticeDevice.ConfigHeader._head[0]:
                raise ValueError(f"Packet's head is not {RticeDevice.ConfigHeader._head}, head={_head}")

            _version = int.from_bytes(packet[1:3], byteorder='big')
            _data = packet[3:30]
           
            _sum = int.from_bytes(packet[30:32], byteorder='big')
            _check_sum = int.from_bytes(RticeDevice.Util.calc_sum(packet, 30), byteorder='big')
            if _sum != _check_sum:
                raise ValueError("Check sum is error, _sum=0x%02X, _check_sum=0x%02X" % (_sum, _check_sum))

            _data_dict = {
                "version": _version,
                "data": _data
            }

            return _data_dict

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
                "Version": _version,
                "NameList": name_list
            }

            return _data_dict

    def __init__(self, dev_sn, libfile):
        self._dev_sn = dev_sn
        self._libfile = libfile
        self._dll = None

    def init_device(self):
        try:
            _dll = ctypes.CDLL(self._libfile)
            _setup_prototypes(_dll)

            ret = _check(_dll.initialize())
            if ret != 0:
                logging.error(f"initialize device:{self._dev_sn} fail: {_str_error_map[ret]}")
                return False
        
            name = ctypes.c_char_p(self._dev_sn.encode('utf-8'))
            ret = _check(_dll.setPort(2, name))
            if ret != 0:
                logging.error(f"setPort device:{self._dev_sn} fail: {_str_error_map[ret]}")
                _dll.uninitialize()
                return False

            ret = _check(_dll.openPort())
            if ret != 0:
                logging.error(f"openPort device:{self._dev_sn} fail: {_str_error_map[ret]}")
                _dll.uninitialize()
                return False

            logging.debug(f"Init device:{self._dev_sn} OK")
            self._dll = _dll
            return True
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())

        return False

    def deinit_device(self):
        _dll = self._dll

        try:
            ret = _check(_dll.closePort())
            if ret != 0:
                logging.error(f"closePort device:{self._dev_sn} fail: {_str_error_map[ret]}")
                return False

            _dll.uninitialize()
            logging.debug(f"Deinit device:{self._dev_sn} OK")
            return True
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
                
        return False

    def get_customer_version(self, args):
        _dll = self._dll

        try:
            cv = _lib_CustomerVersion_T2()
            ret = _check(_dll.AT2_Get_Customer_Ver_Example(ctypes.byref(cv)))
            if ret != 0:
                logging.error(f"Get device:{self._dev_sn} version fail: {_str_error_map[ret]}")
                return _error_args(ret, _str_error_map[ret])

            logging.debug(f"Device:{self._dev_sn} version: {cv.version}")
            _args = {
                "Result": True,
                "Version": cv.version.decode("ascii").rstrip('\x00')
            }
            return _args
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    def get_USB_iProduct(self, args):
        _dll = self._dll

        try:
            rd_buff = ctypes.create_string_buffer(64)
            ret = _check(_dll.AT_USB_Get_iProduct(rd_buff, len(rd_buff)))
            if ret == 0:
                logging.error(f"Get device:{self._dev_sn} iProduct fail: {_str_error_map[ret]}")
                return _error_args(ret, _str_error_map[ret])

            logging.debug(f"Device:{self._dev_sn} iProduct: {rd_buff.value}")
            _args = {
                "Result": True,
                "iProduct": rd_buff.value.decode("ascii").rstrip('\x00')
            }
            return _args
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    def get_UVC_Name(self, args):
        _dll = self._dll

        try:
            rd_buff = ctypes.create_string_buffer(64)
            result_len = ctypes.c_uint32()

            ret = _check(_dll.AT_Get_UVC_Name(rd_buff, len(rd_buff), ctypes.byref(result_len)))
            if ret != 0:
                logging.error(f"Get device:{self._dev_sn} UVC Name fail: {_str_error_map[ret]}")
                return _error_args(ret, _str_error_map[ret])

            logging.debug(f"Device:{self._dev_sn} UVC Name: {rd_buff.value}")
            _args = {
                "Result": True,
                "UVCName": rd_buff.value.decode("ascii").rstrip('\x00')
            }
            return _args
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()
    
    def get_UAC_Name(self, args):
        _dll = self._dll

        try:
            rd_buff = ctypes.create_string_buffer(64)
            result_len = ctypes.c_uint32()

            ret = _check(_dll.AT_Get_UAC_Name(rd_buff, len(rd_buff), ctypes.byref(result_len)))
            if ret != 0:
                logging.error(f"Get device:{self._dev_sn} UAC Name fail: {_str_error_map[ret]}")
                return _error_args(ret, _str_error_map[ret])

            logging.debug(f"Device:{self._dev_sn} UAC Name: {rd_buff.value}")
            _args = {
                "Result": True,
                "UACName": rd_buff.value.decode("ascii").rstrip('\x00')
            }
            return _args
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    def get_UAC_OUT2_Name(self, args):
        _dll = self._dll

        try:
            rd_buff = ctypes.create_string_buffer(64)

            ret = _check(_dll.AT_UAC_Get_UAC_OUT2_Name(rd_buff, len(rd_buff)))
            if ret == 0:
                logging.error(f"Get device:{self._dev_sn} UAC OUT2 Name fail: {_str_error_map[ret]}")
                return _error_args(ret, _str_error_map[ret])

            logging.debug(f"Device:{self._dev_sn} UAC OUT2 Name: {rd_buff.value}")
            _args = {
                "Result": True,
                "UACOut2Name": rd_buff.value.decode("ascii").rstrip('\x00')
            }
            return _args
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()
    
    def get_UAC_IN_Name(self, args):
        _dll = self._dll

        try:
            rd_buff = ctypes.create_string_buffer(64)

            ret = _check(_dll.AT_UAC_Get_UAC_IN_Name(rd_buff, len(rd_buff)))
            if ret == 0:
                logging.error(f"Get device:{self._dev_sn} UAC IN Name fail: {_str_error_map[ret]}")
                return _error_args(ret, _str_error_map[ret])

            logging.debug(f"Device:{self._dev_sn} UAC IN Name: {rd_buff.value}")
            _args = {
                "Result": True,
                "UACInName": rd_buff.value.decode("ascii").rstrip('\x00')
            }
            return _args
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    def get_HdmiRX_RawTimingInfo(self, args):
        _dll = self._dll

        try:
            hti = _lib_AT_HDMI_TIMING_INFO_T()

            ret = _check(_dll.AT_HdmiRX_GetRawTimingInfo(ctypes.byref(hti)))
            if ret != 0:
                logging.error(f"Get device:{self._dev_sn} HdmiRX Raw Timing Infor fail: {_str_error_map[ret]}")
                return _error_args(ret, _str_error_map[ret])

            logging.debug(f"Device:{self._dev_sn} HdmiRX Raw Timing Infor success!")
            _args = {
                "Result": True,
                "is_interlace": (hti.union1 & 0x01),
                "pixel_repeat": ((hti.union1 >> 1) & 0x07),
                "polarity": ((hti.union1 >> 4) & 0x03),
                "run_dsc": ((hti.union1 >> 6) & 0x03),
                "run_vrr": hti.run_vrr,
                "vTotal": hti.vTotal,
                "hTotal": hti.hTotal,
                "vActive": hti.vActive,
                "hActive": hti.hActive,
                "vStart": hti.vStart,
                "hStart": hti.hStart,
                "vFreq": hti.vFreq,
                "hFreq": hti.hFreq,
                "dr_mode": hti.dr_mode,
                "IVSyncPulseCount": hti.IVSyncPulseCount,
                "IHSyncPulseCount": hti.IHSyncPulseCount,
                "mode": hti.mode,
                "colordepth": hti.colordepth,
                "colorspace": hti.colorspace,
                "colorrange": hti.colorrange,
                "colorimetry": hti.colorimetry,
                "ext_colorimetry": hti.ext_colorimetry,
                "hdcpType": hti.hdcpType,
                "tmds_clk_b": hti.tmds_clk_b,
                "pll_pixelclockx1024": hti.pll_pixelclockx1024,
                "cur_sys_time": hti.cur_sys_time,
            }
            return _args
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()
    
    def get_Audio_HdmiDPRX_VolumeGain(self, args):
        volume = _lib_Audio_Volume_T()
        _dll = self._dll

        try:
            ret = _check(_dll.AT_Audio_Get_HdmiDPRX_VolumeGain(ctypes.byref(volume)))
            if ret != 0:
                logging.error(f"Get device:{self._dev_sn} HdmiDPRX Audio Volume Gain fail: {_str_error_map[ret]}")
                return _error_args(ret, _str_error_map[ret])

            logging.debug(f"Device:{self._dev_sn} HdmiDPRX Audio Volume Gain: {volume.gain}")
            _args = {
                "Result": True,
                "Gain": volume.gain
            }
            return _args
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    def set_Audio_HdmiDPRX_VolumeGain(self, args):
        _dll = self._dll

        try:
            if "Gain" in args:
                gain = args["Gain"]
                if not -72 <= gain <= 30:
                    logging.error("HdmiDPRX Audio Volume Gain Should be -72 ~ 30 db")
                    return _error_args()

                ret = _check(_dll.AT_Audio_Set_HdmiDPRX_VolumeGain(gain))
                if ret != 0:
                    logging.error(f"Set device:{self._dev_sn} HdmiDPRX Audio Volume Gain fail: {_str_error_map[ret]}")
                    return _error_args(ret, _str_error_map[ret])

                logging.debug(f"Set Device:{self._dev_sn} HdmiDPRX Audio Volume Gain: {gain}")
                _args = {
                    "Result": True,
                    "Gain": gain
                }
                return _args
            else:
                logging.error(f"Set device:{self._dev_sn} HdmiDPRX Audio Volume Gain fail: without Gain parameter in args.")
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()
    
    def get_Audio_UAC_VolumeGain(self, args):
        volume = _lib_Audio_Volume_T()
        _dll = self._dll

        try:
            ret = _check(_dll.AT_Audio_Get_UAC_VolumeGain(ctypes.byref(volume)))
            if ret != 0:
                logging.error(f"Get device:{self._dev_sn} Uac audio volume gain fail: {_str_error_map[ret]}")
                return _error_args(ret, _str_error_map[ret])

            logging.debug(f"Device:{self._dev_sn} Uac audio volume gain: {volume.gain}")
            _args = {
                "Result": True,
                "Gain": volume.gain
            }
            return _args
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    def set_Audio_UAC_VolumeGain(self, args):
        _dll = self._dll

        try:
            if "Gain" in args:
                gain = args["Gain"]
                if not -72 <= gain <= 30:
                    logging.error("Uac audio volume gain Should be -72 ~ 30 db")
                    return _error_args()

                ret = _check(_dll.AT_Audio_Set_UAC_VolumeGain(gain))
                if ret != 0:
                    logging.error(f"Set device:{self._dev_sn} Uac audio volume gain fail: {_str_error_map[ret]}")
                    return _error_args(ret, _str_error_map[ret])

                logging.debug(f"Set Device:{self._dev_sn} Uac audio volume gain: {gain}")
                _args = {
                    "Result": True,
                    "Gain": gain
                }
                return _args
            else:
                logging.error(f"Set device:{self._dev_sn} Uac audio volume gain fail: without Gain parameter in args.")
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    def get_Audio_I2SOut_MixerSource(self, args):
        _dll = self._dll

        try:
            mixer_src = ctypes.c_int16() # AT_IPT_FIFO1_ADC/AT_IPT_FIFO2_I2S_IN/AT_IPT_SPDIF/AT_IPT_UAC
            ret = _check(_dll.AT_Audio_Get_I2SOut_MixerSource(ctypes.byref(mixer_src)))
            if ret != 0:
                logging.error(f"Get device:{self._dev_sn} I2S Out Mixer Source fail: {_str_error_map[ret]}")
                return _error_args(ret, _str_error_map[ret])

            mixer_sources = []
            if (mixer_src.value & 0x0001) == 0x0001: mixer_sources.append(ModelRticePreferences._mixerSourceList[0])
            if (mixer_src.value & 0x0002) == 0x0002: mixer_sources.append(ModelRticePreferences._mixerSourceList[1])
            if (mixer_src.value & 0x0004) == 0x0004: mixer_sources.append(ModelRticePreferences._mixerSourceList[2])
            if (mixer_src.value & 0x0008) == 0x0008: mixer_sources.append(ModelRticePreferences._mixerSourceList[3])

            logging.debug(f"Device:{self._dev_sn} I2S Out Mixer Source: {mixer_sources}")
            _args = {
                "Result": True,
                "MixerSource": mixer_sources
            }
            return _args
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()
    
    def set_Audio_I2SOut_MixerSource(self, args):
        # AT_IPT_FIFO1_ADC/AT_IPT_FIFO2_I2S_IN/AT_IPT_SPDIF/AT_IPT_UAC
        # MixerSource = ["ADC", "I2S IN", "SPDIF", "UAC"]
        _dll = self._dll

        try:
            if "MixerSource" in args and all(x in ModelRticePreferences._mixerSourceList for x in args["MixerSource"]):
                mixer_sources = args["MixerSource"]

                src_value = 0x00
                if ModelRticePreferences._mixerSourceList[0] in mixer_sources: # "ADC"
                    src_value |= 0x01
                    
                if ModelRticePreferences._mixerSourceList[1] in mixer_sources: # "I2S IN"
                    src_value |= 0x02

                if ModelRticePreferences._mixerSourceList[2] in mixer_sources: # "SPDIF"
                    src_value |= 0x04
                    
                if ModelRticePreferences._mixerSourceList[3] in mixer_sources: # "UAC"
                    src_value |= 0x08

                _src_value = ctypes.c_int16(src_value)
                ret = _check(_dll.AT_Audio_Set_I2SOut_MixerSource(ctypes.byref(_src_value)))
                if ret != 0:
                    logging.error(f"Set device:{self._dev_sn} I2S Out Mixer Source fail: {_str_error_map[ret]}")
                    # _args = {
                    #     "Result": False,
                    #     "MixerSource": mixer_sources
                    # }
                    # return _args
                    return _error_args(ret, _str_error_map[ret])

                logging.debug(f"Set Device:{self._dev_sn} I2S Out Mixer Source: {mixer_sources}")
                _args = {
                    "Result": True,
                    "MixerSource": mixer_sources
                }
                return _args
            else:
                logging.error(f"Set device:{self._dev_sn} I2S Out Mixer Source fail: MixerSource in args is error.")
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    def get_Audio_UACOut2_MixerSource(self, args):
        _dll = self._dll

        try:
            mixer_src = ctypes.c_int16() # AT_IPT_FIFO1_ADC/AT_IPT_FIFO2_I2S_IN/AT_IPT_SPDIF/AT_IPT_UAC
            ret = _check(_dll.AT_Audio_Get_UacOut2_MixerSource(ctypes.byref(mixer_src)))
            if ret != 0:
                logging.error(f"Get device:{self._dev_sn} Uac Out2 Mixer Source fail: {_str_error_map[ret]}")
                return _error_args(ret, _str_error_map[ret])

            mixer_sources = []
            if (mixer_src.value & 0x0001) == 0x0001: mixer_sources.append(ModelRticePreferences._mixerSourceList[0])
            if (mixer_src.value & 0x0002) == 0x0002: mixer_sources.append(ModelRticePreferences._mixerSourceList[1])
            if (mixer_src.value & 0x0004) == 0x0004: mixer_sources.append(ModelRticePreferences._mixerSourceList[2])
            if (mixer_src.value & 0x0008) == 0x0008: mixer_sources.append(ModelRticePreferences._mixerSourceList[3])

            logging.debug(f"Device:{self._dev_sn} Uac Out2 Mixer Source: {mixer_sources}")
            _args = {
                "Result": True,
                "MixerSource": mixer_sources
            }
            return _args
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    def set_Audio_UACOut2_MixerSource(self, args):
        # AT_IPT_FIFO1_ADC/AT_IPT_FIFO2_I2S_IN/AT_IPT_SPDIF/AT_IPT_UAC
        # MixerSource = ["ADC", "I2S IN", "SPDIF", "UAC"]
        _dll = self._dll

        try:
            if "MixerSource" in args and all(x in ModelRticePreferences._mixerSourceList for x in args["MixerSource"]):
                mixer_sources = args["MixerSource"]

                src_value = 0x00
                if ModelRticePreferences._mixerSourceList[0] in mixer_sources: # "ADC"
                    src_value |= 0x01
                    
                if ModelRticePreferences._mixerSourceList[1] in mixer_sources: # "I2S IN"
                    src_value |= 0x02

                if ModelRticePreferences._mixerSourceList[2] in mixer_sources: # "SPDIF"
                    src_value |= 0x04
                    
                if ModelRticePreferences._mixerSourceList[3] in mixer_sources: # "UAC"
                    src_value |= 0x08

            
                _src_value = ctypes.c_int16(src_value)
                ret = _check(_dll.AT_Audio_Set_UacOut2_MixerSource(ctypes.byref(_src_value)))
                if ret != 0:
                    logging.error(f"Set device:{self._dev_sn} UAC Out2 Mixer Source fail: {_str_error_map[ret]}")
                    return _error_args(ret, _str_error_map[ret])

                logging.debug(f"Set Device:{self._dev_sn} UAC Out2 Mixer Source: {mixer_sources}")
                _args = {
                    "Result": True,
                    "MixerSource": mixer_sources
                }
                return _args
            else:
                logging.error(f"Set device:{self._dev_sn} UAC Out2 Mixer Source fail: MixerSource in args is error.")
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    def get_EDID_mode(self, args):
        _dll = self._dll

        try:
            mode = ctypes.c_uint32()
            ret = _check(_dll.AT_EDID_Get_EDID_mode(ctypes.byref(mode)))
            if ret != 0:
                logging.error(f"Get device:{self._dev_sn} EDID mode fail: {_str_error_map[ret]}")
                return _error_args(ret, _str_error_map[ret])

            logging.debug(f"Device:{self._dev_sn} EDID mode: {ModelRticePreferences._edidModeList[mode.value]}")
            _args = {
                "Result": True,
                "EdidMode": ModelRticePreferences._edidModeList[mode.value]
            }
            return _args
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())

        return _error_args()

    def set_EDID_mode(self, args):
        _dll = self._dll

        try:
            if "EdidMode" in args and args["EdidMode"] in ModelRticePreferences._edidModeList:
                edidMode = args["EdidMode"]
                mode = ModelRticePreferences._edidModeList.index(edidMode)

                ret = _check(_dll.AT_EDID_Set_EDID_mode(mode))
                if ret != 0:
                    logging.error(f"Set device:{self._dev_sn} EDID mode fail: {_str_error_map[ret]}")
                    return _error_args(ret, _str_error_map[ret])

                logging.debug(f"Set Device:{self._dev_sn} EDID mode: {edidMode}")
                _args = {
                    "Result": True,
                    "EdidMode": edidMode
                }
                return _args
            else:
                logging.error(f"Set device:{self._dev_sn} EDID mode fail: without EdidMode parameter in args.")
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())

        return _error_args()

    """
    in TargetPos : Target CSC position [0:RGB2YUV 1:YUV2RGB]
    out Value : Returned color range status [0:LIMIT, 1:FULL 2:EXPAND(YUV2RGB only) 3:SHRINK(YUV2RGB only)]
    """
    def get_ColorRange(self, args):
        _dll = self._dll

        try:
            colorRange = ctypes.c_uint8()
            pos = 0 # default is RGB2YUV
            if "TargetCSCPos" in args and args["TargetCSCPos"] in ModelRticePreferences._targetCSCPosList:
                targetCSCPos = args["TargetCSCPos"]
                pos = ModelRticePreferences._targetCSCPosList.index(targetCSCPos)

            ret = _check(_dll.AT_Get_ColorRange(pos, ctypes.byref(colorRange)))
            if ret != 0:
                logging.error(f"Get device:{self._dev_sn} Color Range fail: {_str_error_map[ret]}")
                return _error_args(ret, _str_error_map[ret])

            logging.debug(f"Device:{self._dev_sn} Color Range: {colorRange.value}")
            _args = {
                "Result": True,
                "TargetPos": ModelRticePreferences._targetCSCPosList[pos],
                "ColorRange": ModelRticePreferences._colorRangeList[colorRange.value]
            }
            return _args
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    """
    in Cmd : Target CSC position [0:RGB2YUV 1:YUV2RGB] and color range setting [0:AUTO 1:LIMIT 2:FULL 3:EXPAND(YUV2RGB only) 4:SHRINK(YUV2RGB only)]
    """
    def set_ColorRange(self, args):
        _dll = self._dll

        try:
            colorCtrlCmd = _lib_AT_SQE_COLOR_CTRL_CMD_T()
            # colorCtrlCmd.TargetPos = 0 # default is RGB2YUV
            # if "TargetCSCPos" in args and args["TargetCSCPos"] in ModelRticePreferences._targetCSCPosList:
            #     targetCSCPos = args["TargetCSCPos"]
            #     colorCtrlCmd.TargetPos = ModelRticePreferences._targetCSCPosList.index(targetCSCPos)

            if "ColorRange" in args and args["ColorRange"] in ModelRticePreferences._colorRangeModeList:
                colorRange = args["ColorRange"]
                colorCtrlCmd.Value = ModelRticePreferences._colorRangeModeList.index(colorRange)

                # 先设置RGB2YUV
                colorCtrlCmd.TargetPos = 0
                logging.debug(f"TargetCSCPos:{colorCtrlCmd.TargetPos}, colorRange:{colorCtrlCmd.Value}")

                ret = _check(_dll.AT_Set_ColorRange(ctypes.byref(colorCtrlCmd)))
                if ret != 0:
                    logging.error(f"Set device:{self._dev_sn} RGB2YUV Color Range fail: {_str_error_map[ret]}")
                    return _error_args(ret, _str_error_map[ret])

                # 再设置YUV2RGB
                colorCtrlCmd.TargetPos = 1
                logging.debug(f"TargetCSCPos:{colorCtrlCmd.TargetPos}, colorRange:{colorCtrlCmd.Value}")

                ret = _check(_dll.AT_Set_ColorRange(ctypes.byref(colorCtrlCmd)))
                if ret != 0:
                    logging.error(f"Set device:{self._dev_sn} YUV2RGB Color Range fail: {_str_error_map[ret]}")
                    return _error_args(ret, _str_error_map[ret])

                logging.debug(f"Set Device:{self._dev_sn} Color Range: {colorRange}")
                _args = {
                    "Result": True,
                    "ColorRange": colorRange
                }
                return _args
            else:
                logging.error(f"Set device:{self._dev_sn} Color Range fail: without ColorRange parameter in args.")
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
                
        return _error_args()

    """
    @brief AT_EDID_DDC_Get_RX_table: CMD:   88 	r/w:	Get one table of RX EDID from DDC
    @param [in] nSize : total read size
    @param [out] rd_buff :  read data from edid
    @return Returns error code defined in ENUM_ERROR_CODE
    """
    def get_EDID_DDC_RX_table(self, args):
        _dll = self._dll

        try:
            rd_buff = (ctypes.c_uint8 * 512)()

            ret = _check(_dll.AT_EDID_DDC_Get_RX_table(len(rd_buff), ctypes.byref(rd_buff)))
            if ret != 0:
                logging.error(f"Get device:{self._dev_sn} EDID DDC RX table fail: {_str_error_map[ret]}")
                return _error_args(ret, _str_error_map[ret])

            logging.debug(f"Get device:{self._dev_sn} EDID DDC RX table success")
            _args = {
                "Result": True,
                "EDIDTable": rd_buff
            }
            return _args
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    """
    @brief AT_EDID_DDC_Set_RX_table: CMD:   87   r/w:    w   set edid to ddc
    @param [in] nSize : total write size
    @param [in] wr_buff : write nSize data to edid
    @return Returns error code defined in ENUM_ERROR_CODE
    """
    def set_EDID_DDC_RX_table(self, args):
        _dll = self._dll

        try:
            if "EDIDTable" in args:
                data = args["EDIDTable"]
                data_len = len(data)

                if data_len in [128, 256, 384, 512]:
                    wr_buff = (ctypes.c_uint8 * len(data))(*data)

                    ret = _check(_dll.AT_EDID_DDC_Set_RX_table(data_len, ctypes.byref(wr_buff)))
                    if ret != 0:
                        logging.error(f"Set device:{self._dev_sn} DDC EDID table fail: {_str_error_map[ret]}")
                        return _error_args(ret, _str_error_map[ret])

                    logging.debug(f"Set Device:{self._dev_sn} DDC EDID table success!")
                    _args = {
                        "Result": True
                    }
                    return _args
                else:
                    logging.error(f"Set device:{self._dev_sn} DDC EDID table fail: EDIDTable's length error. data_len={data_len}")
            else:
                logging.error(f"Set device:{self._dev_sn} DDC EDID table fail: without EDIDTable parameter in args.")
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    """
    @brief AT_EDID_Flash_Get_table: CMD:	 84    r/w:    Get one table of EDID from flash
    @param [in] idx : Indicates which group of edid
    @param [out] rd_buff : buff data
    @param [in] nSize : Size of the given buffer
    @return Returns error code defined in ENUM_ERROR_CODE
    """
    def get_EDID_Flash_table(self, args):
        _dll = self._dll

        try:
            if "EDIDTableIndex" in args:
                index = args["EDIDTableIndex"]

                if 0 <= index <= 6:
                    rd_buff = (ctypes.c_uint8 * 512)()

                    ret = _check(_dll.AT_EDID_Flash_Get_table(index, ctypes.byref(rd_buff), len(rd_buff)))
                    if ret != 0:
                        logging.error(f"Get device:{self._dev_sn} EDID Flash table fail: {_str_error_map[ret]}")
                        return _error_args(ret, _str_error_map[ret])

                    logging.debug(f"Get device:{self._dev_sn} EDID Flash table success")
                    _args = {
                        "Result": True,
                        "EDIDTableIndex": index,
                        "EDIDTable": rd_buff
                    }
                    return _args
                else:
                    logging.error(f"Get device:{self._dev_sn} EDID Flash table fail: EDIDTable's index error. index={index}")
            else:
                logging.error(f"Get device:{self._dev_sn} EDID Flash table fail: without EDIDTable index in args.")
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    """
    @brief AT_EDID_Flash_Set_table: choose which group of edid data to burn flash
    @param [in] idx : Indicates which group of edid
    @param [in] wr_buff : buff data to write
    @param [in] nSize : Size of the given buffer
    @return Returns error code defined in  ENUM_ERROR_CODE
    """
    def set_EDID_Flash_table(self, args):
        _dll = self._dll

        try:
            if "EDIDTable" in args and "EDIDTableIndex" in args:
                index = args["EDIDTableIndex"]
                data = args["EDIDTable"]
                data_len = len(data)

                if data_len in [128, 256, 384, 512] and 0 <= index <= 6:
                    wr_buff = (ctypes.c_uint8 * len(data))(*data)

                    ret = _check(_dll.AT_EDID_Flash_Set_table(index, ctypes.byref(wr_buff), data_len))
                    if ret != 0:
                        logging.error(f"Set device:{self._dev_sn} EDID Flash table fail: {_str_error_map[ret]}")
                        return _error_args(ret, _str_error_map[ret])

                    logging.debug(f"Set Device:{self._dev_sn} EDID Flash table success!")
                    _args = {
                        "Result": True
                    }
                    return _args
                else:
                    logging.error(f"Set device:{self._dev_sn} EDID Flash table fail: EDIDTable's length or index error. data_len={data_len}, index={index}")
            else:
                logging.error(f"Set device:{self._dev_sn} EDID Flash table fail: without EDIDTable parameter in args.")
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    """
    用EDID Flash table的最后一个(第7个表)来存储table的名称列表
    """
    def get_EDID_Flash_Table_Name_List(self, args):
        _dll = self._dll

        try:
            rd_buff = (ctypes.c_uint8 * 384)()

            ret = _check(_dll.AT_EDID_Flash_Get_table(6, ctypes.byref(rd_buff), len(rd_buff)))
            if ret != 0:
                logging.error(f"Get device:{self._dev_sn} EDID Flash table name list fail: {_str_error_map[ret]}")
                return _error_args(ret, _str_error_map[ret])

            try:
                _data_dict = RticeDevice.EDIDFlashTableNameListParser.parse(list(rd_buff))
            except:
                _data_dict = {
                    "Result": True,
                    "Version": "1.0",
                    "NameList": [""]*6
                }

            logging.debug(f"Get device:{self._dev_sn} EDID Flash table name list success")
            _args = {
                "Result": True,
                "Version": _data_dict["Version"],
                "NameList": _data_dict["NameList"]
            }

            return _args
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    def set_EDID_Flash_Table_Name_List(self, args):
        _dll = self._dll

        try:
            if "NameList" in args:
                data = args["NameList"]
                packet = RticeDevice.EDIDFlashTableNameListPacker.pack(data)
                packet_len = len(packet)

                wr_buff = (ctypes.c_uint8 * packet_len)(*packet)

                if packet_len in [128, 256, 384, 512]:
                    ret = _check(_dll.AT_EDID_Flash_Set_table(6, ctypes.byref(wr_buff), packet_len))
                    if ret != 0:
                        logging.error(f"Set device:{self._dev_sn} EDID Flash table name list fail: {_str_error_map[ret]}")
                        return _error_args(ret, _str_error_map[ret])

                    logging.debug(f"Set Device:{self._dev_sn} EDID Flash table name list success!")
                    _args = {
                        "Result": True,
                        "NameList": list(data)
                    }
                    return _args
                else:
                    logging.error(f"Set device:{self._dev_sn} EDID Flash table name list fail: packet's length error. packet_len={packet_len}")
            else:
                logging.error(f"Set device:{self._dev_sn} EDID Flash table name list fail: without NameList parameter in args.")
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    """
    @brief AT_EDID_Flash_Set_Default_table: CMD:   85 	r/w:	Set default EDID to flash
    @param [in] edid_table_num :  set num
    @return Returns error code defined in ENUM_ERROR_CODE
    """
    def set_EDID_Flash_Default_table(self, args):
        _dll = self._dll

        try:
            if "EDIDTableIndex" in args:
                edidTableIndex = ctypes.c_uint8(args["EDIDTableIndex"])

                ret = _check(_dll.AT_EDID_Flash_Set_Default_table(edidTableIndex))
                if ret != 0:
                    logging.error(f"Set device:{self._dev_sn} default EDID to flash fail: {_str_error_map[ret]}")
                    return _error_args(ret, _str_error_map[ret])

                logging.debug(f"Set Device:{self._dev_sn} default EDID to flash success!")
                _args = {
                    "Result": True,
                    "EDIDTableIndex": edidTableIndex.value
                }
                return _args
            else:
                logging.error(f"Set device:{self._dev_sn} default EDID to flash fail: without EDIDTableIndex parameter in args.")
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    """
    @brief AT_EDID_Flash_Get_Default_table: CMD:   86 	r/w:	Get default EDID to flash
    @param [out] edid_table_num :  get num
    @return Returns error code defined in ENUM_ERROR_CODE
    """
    def get_EDID_Flash_Default_table(self, args):
        _dll = self._dll

        try:
            edidTableIndex = ctypes.c_uint8()

            ret = _check(_dll.AT_EDID_Flash_Get_Default_table(ctypes.byref(edidTableIndex)))
            if ret != 0:
                logging.error(f"Get device:{self._dev_sn} default EDID to flash fail: {_str_error_map[ret]}")
                return _error_args(ret, _str_error_map[ret])

            logging.debug(f"Get device:{self._dev_sn} default EDID to flash success")
            _args = {
                "Result": True,
                "EDIDTableIndex": edidTableIndex.value
            }
            return _args
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    """
    @brief AT_Flash_Get_CustomerProprietary: CMD:   82 	r/w:	r	Get customer proprietary data
    @param [in] customer_proprietary : Buffer for getting customer proprietary.
    @return Returns error code defined in ENUM_ERROR_CODE
    """
    def set_Flash_CustomerProprietary(self, args):
        _dll = self._dll

        try:
            if "CustomerProprietary" in args:
                data = args["CustomerProprietary"]
                wr_buff = (ctypes.c_uint8 * len(data))(*data)

                ret = _check(_dll.AT_Flash_Set_CustomerProprietary(ctypes.byref(wr_buff)))
                if ret != 0:
                    logging.error(f"Set device:{self._dev_sn} Flash Customer Proprietary fail: {_str_error_map[ret]}")
                    return _error_args(ret, _str_error_map[ret])

                logging.debug(f"Set Device:{self._dev_sn} Flash Customer Proprietary success!")
                _args = {
                    "Result": True,
                    "CustomerProprietary": data
                }
                return _args
            else:
                logging.error(f"Set device:{self._dev_sn} Flash Customer Proprietary fail: without CustomerProprietary parameter in args.")
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    """
    @brief AT_Flash_Get_CustomerProprietary: CMD:   82 	r/w:	r	Get customer proprietary data
    @param [in] customer_proprietary : Buffer for getting customer proprietary.
    @return Returns error code defined in ENUM_ERROR_CODE
    """
    def get_Flash_CustomerProprietary(self, args):
        _dll = self._dll

        try:
            rd_buff = (ctypes.c_uint8 * 32)()

            ret = _check(_dll.AT_Flash_Get_CustomerProprietary(ctypes.byref(rd_buff)))
            if ret != 0:
                logging.error(f"Get device:{self._dev_sn} Flash Customer Proprietary fail: {_str_error_map[ret]}")
                return _error_args(ret, _str_error_map[ret])

            logging.debug(f"Get device:{self._dev_sn} Flash Customer Proprietary success")
            _args = {
                "Result": True,
                "CustomerProprietary": list(rd_buff)
            }
            return _args
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    def get_ConfigData(self, args):
        _dll = self._dll

        try:
            rd_buff = (ctypes.c_uint8 * 32)()

            ret = _check(_dll.AT_Flash_Get_CustomerProprietary(ctypes.byref(rd_buff)))
            if ret != 0:
                logging.error(f"Get device:{self._dev_sn} Config Data fail: {_str_error_map[ret]}")
                return _error_args(ret, _str_error_map[ret])

            _data_dict = RticeDevice.ConfigParser.data_parser(list(rd_buff))

            logging.debug(f"Get device:{self._dev_sn} Config Data success")
            _args = {
                "Result": True,
                "Version": _data_dict["version"],
                "ConfigData": _data_dict["data"]
            }
            return _args
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    def set_ConfigData(self, args):
        _dll = self._dll

        try:
            if "ConfigData" in args:
                data = args["ConfigData"]
                packet = RticeDevice.ConfigPacker.data_packing(data)

                wr_buff = (ctypes.c_uint8 * len(packet))(*packet)

                ret = _check(_dll.AT_Flash_Set_CustomerProprietary(ctypes.byref(wr_buff)))
                if ret != 0:
                    logging.error(f"Set device:{self._dev_sn} Config Data fail: {_str_error_map[ret]}")
                    return _error_args(ret, _str_error_map[ret])

                logging.debug(f"Set Device:{self._dev_sn} Config Data success!")
                _args = {
                    "Result": True
                }
                return _args
            else:
                logging.error(f"Set device:{self._dev_sn} Config Data fail: without ConfigData parameter in args.")
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()

    """
    @brief AT_RestoreToDefault: CMD: 93 r/w:    w   Restore the userdata To Default
    @param none.
    @return result:1 success  0: fail ?? 说明文档有误? 0是成功
    """
    def set_RestoreToDefault(self, args):
        _dll = self._dll

        try:
            ret = _check(_dll.AT_RestoreToDefault())
            if ret != 0:
                logging.error(f"Set device:{self._dev_sn} to default fail: {_str_error_map[ret]}")
                return _error_args(ret, _str_error_map[ret])

            logging.debug(f"Device:{self._dev_sn} restore to default")
            _args = {
                "Result": True
            }
            return _args
        except Exception as e:
            logging.error(f"e:{e}")
            logging.error(traceback.format_exc())
        
        return _error_args()