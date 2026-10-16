import logging
from src.avm_stack.usb_stack.packet.packer import Packer

class TransCore(object):
    def __init__(self, mphy):
        self.__phy = mphy

    def send_command(self, cmd, timeout=1000):
        packet = Packer.command_packet(cmd)
        return self.__phy.send(packet, timeout=timeout)

    def send_data(self, cmd, data, datalen, timeout=1000):
        packet = Packer.paging_packet(0, cmd, data, datalen)
        return self.__phy.send(packet, timeout=timeout)

    def send_paging_data(self, page, cmd, data, datalen, timeout=1000):
        packet = Packer.paging_packet(page, cmd, data, datalen)
        return self.__phy.send(packet, timeout=timeout)

    def receive(self, length=64, timeout=1000):
        return self.__phy.receive(length, timeout=timeout)
