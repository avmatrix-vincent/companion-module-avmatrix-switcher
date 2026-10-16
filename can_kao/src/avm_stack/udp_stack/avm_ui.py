import logging

from avm_stack.avm_app import AvmApp


class AvmUi(object):
    def __init__(self, app:AvmApp) -> None:
        self._app = app
        self._dev_info_list = None
        self._app.add_async_callback(self.async_callback)
        self._app.add_device_status_listener(self.device_status_listener)
        self._app.add_report_listener(self.report_listener)

    """
    由于该回调是由其他线程发起的，因此不能直接去更新UI，在QT中，需要通过信号去触发UI线程来更新UI
    """
    def async_callback(self, dev_sn, args):
        print("async_callback dev_sn:", dev_sn)
        print("async_callback args:", args)

    def device_status_listener(self, args):
        print("device_status_listener args:", args)

    def report_listener(self, dev_sn, args):
        print("report_listener dev_sn:", dev_sn)
        print("report_listener args:", args)

    def start_scan(self):
        self._app.start_scan()

    def stop_scan(self):
        self._app.stop_scan()

    def close(self):
        self._app.remove_async_callback(self.async_callback)
        self._app.remove_device_status_listener(self.device_status_listener)
        self._app.remove_report_listener(self.report_listener)

    def get_device_info_list(self):
        self._dev_info_list = self._app.get_device_info_list()
        logging.debug("dev_info_list:")
        for info in self._dev_info_list:
            logging.debug(info)

    def get_version(self, dev_sn):
        self._app.async_get_version(dev_sn)

    def get_version_by_index(self, index):
        dev_sn = self._dev_info_list[index]["sn"]
        self._app.async_get_version(dev_sn)
