import pythoncom
import wmi
import os
import re

w = wmi.WMI()

info = w.Win32_USBControllerDevice()
index = 0
for d in info:
    index += 1

    print(f">>>>>>>{index}:")
    print(f"Status: {d.Dependent.Status}")
    print(f"HardwareID: {d.Dependent.HardwareID}")
    print(f"Service: {d.Dependent.Service}")
