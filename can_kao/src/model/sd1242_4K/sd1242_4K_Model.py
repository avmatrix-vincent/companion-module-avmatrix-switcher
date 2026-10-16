import logging
from src.model.modelPreferences import ModelPreferences

class SD1242_4K_Model(object):
    def __init__(self, app) -> None:
        self._app = app

    def __get_version_info_callback(self, dev_sn, args):
        _args = ModelPreferences.sc_handle_version_info(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_version_info(self, dev_sn):
        _cmd = 0x16
        _data = []

        self._app.async_action_usb(dev_sn, _cmd, _data, self.__get_version_info_callback)

    @staticmethod
    def handle_get_device_edid_params(args):
        '''
        解析数据
        '''
        logging.debug("args:{}".format(args))

        _args = {
            "function": "get_device_edid",
            "args": {
                "edidData": args[64:]
            }
        }
        return _args

    def __get_device_edid_callback(self, dev_sn, args):
        _args = SD1242_4K_Model.handle_get_device_edid_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_device_edid(self, dev_sn):
        _cmd = 0xC0
        _data = []

        self._app.async_action_usb(dev_sn, _cmd, _data, self.__get_device_edid_callback)

    @staticmethod
    def handle_set_presaved_edid_data(args):
        '''
        解析数据
        '''
        logging.debug("args:{}".format(args))

        _args = {
            "function": "set_presaved_edid_data",
            "args": {
                "Position": args[8],
                "PresavedName": bytes(args[9:24])
            }
        }
        return _args

    def __set_presaved_edid_data_callback(self, dev_sn, args):
        _args = SD1242_4K_Model.handle_set_presaved_edid_data(args)
        self._app.async_callback(dev_sn, _args)

    def async_set_presaved_edid_data(self, dev_sn, args):
        _cmd = 0xC1
        _data = []

        name = list(bytes(args["PresavedName"], "utf-8"))
        if not 0 < len(name) <= 15:
            logging.error(f"PresavedName参数错误: {args['PresavedName']}")
            return
        
        edid_data = args["EdidData"]
        if len(edid_data) != 256:
            logging.error(f"EdidData参数错误: len={len(args['EdidData'])}")
            return
        
        name.extend([0]*(15 - len(name))) # 不足部分补0
        _data += name
        _data += edid_data

        self._app.async_action_usb(dev_sn, _cmd, _data, self.__set_presaved_edid_data_callback)

    @staticmethod
    def handle_get_selected_edid_data_params(args):
        '''
        解析数据
        '''
        logging.debug("args:{}".format(args))

        _args = {
            "function": "get_selected_edid_data",
            "args": {
                "EdidData": args[64:]
            }
        }
        return _args

    def __get_selected_edid_data_callback(self, dev_sn, args):
        _args = SD1242_4K_Model.handle_get_selected_edid_data_params(args)
        self._app.async_callback(dev_sn, _args)

    @staticmethod
    def handle_get_edid_list(args):
        '''
        解析数据
        '''
        logging.debug("args:{}".format(args))

        list_num = args[8]
        edid_mode = args[9]
        edid_list = []

        for i in range(list_num):
            edid_item = {
                "Id": args[64 + i*16],
                "ListName": bytes(args[65 + i*16: 64 + (i + 1)*16]).decode("utf-8")
            }
            edid_list.append(edid_item)

        _args = {
            "function": "get_edid_list",
            "args": {
                "EdidMode": edid_mode,
                "EdidList": edid_list
            }
        }
        return _args

    def __get_edid_list_callback(self, dev_sn, args):
        _args = SD1242_4K_Model.handle_get_edid_list(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_edid_list(self, dev_sn, args):
        _cmd = 0xC2
        _data = []

        edid_mode = args["EdidMode"]
        if edid_mode != 0x01 and edid_mode != 0x02:
            logging.error("设置的Edid Mode参数错误: ", edid_mode)
            return
        
        _data += edid_mode.to_bytes(1, "big")

        self._app.async_action_usb(dev_sn, _cmd, _data, self.__get_edid_list_callback)

    def async_get_selected_edid_data(self, dev_sn, args):
        _cmd = 0xC3
        _data = []

        edid_mode = args["EdidMode"]
        if edid_mode != 0x01 and edid_mode != 0x02:
            logging.error(f"Edid Mode参数错误: {edid_mode}")
            return

        position = args["Position"]
        if not 0x00 <= position <= 0x3F:
            logging.error(f"Edid Position参数错误: {position}")
            return
        
        _data += edid_mode.to_bytes(1, "big")
        _data += position.to_bytes(1, "big")

        self._app.async_action_usb(dev_sn, _cmd, _data, self.__get_selected_edid_data_callback)
    
    @staticmethod
    def handle_delete_selected_edid_params(args):
        '''
        解析数据
        '''
        logging.debug("args:{}".format(args))

        _args = {
            "function": "delete_selected_edid",
            "args": {
                "EdidMode": args[9],
                "Position": args[10]
            }
        }
        return _args

    def __delete_select_edid_data_callback(self, dev_sn, args):
        _args = SD1242_4K_Model.handle_delete_selected_edid_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_delete_selected_edid(self, dev_sn, args):
        _cmd = 0xC4
        _data = []

        edid_mode = args["EdidMode"]
        if edid_mode != 0x01 and edid_mode != 0x02:
            logging.error(f"Edid Mode参数错误: {edid_mode}")
            return

        position = args["Position"]
        if not 0x00 <= position <= 0x3F:
            logging.error(f"Edid Position参数错误: {position}")
            return
        
        _data += edid_mode.to_bytes(1, "big")
        _data += position.to_bytes(1, "big")

        self._app.async_action_usb(dev_sn, _cmd, _data, self.__delete_select_edid_data_callback)

    