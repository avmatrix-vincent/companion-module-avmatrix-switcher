from src.avm_stack.avm_app import AvmApp
from src.avm_stack.avm_notice import AvmNotice


class AvmManager(object):
    def __init__(self) -> None:
        self._notice = AvmNotice()
        self._app = AvmApp(self._notice)

    def register_model_class(self, model_class_table):
        return self._app.register_model_class(model_class_table)
        
    def register_model(self, dev_sn, model_name):
        return self._app.register_model(dev_sn, model_name)

    def start_scan(self):
        self._app.start_scan()

    def stop_scan(self):
        self._app.stop_scan()

    def delete_device(self, dev_sn, interface):
        self._app.delete_device(dev_sn, interface)

    def get_device_info_list(self):
        return self._app.get_device_info_list()

    def register_notice(self, message_type, callback):  
        self._notice.register(message_type, callback) 
  
    def unregister_notice(self, message_type, callback):
        self._notice.unregister(message_type, callback)

    def dispatch(self, args):
        self._notice.dispatch(args)

    def send_heartbeat(self, args):
        self._app.send_heartbeat_packet(args)
    
    def rename_device(self, args, callback):
        self._app.rename_device(args, callback)

singletonManager = AvmManager()
