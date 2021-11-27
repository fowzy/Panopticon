# Using subprocess and regex:
# https://www.youtube.com/watch?v=SzYKzAHsdMg 
# Using Scapy 
# https://www.thepythoncode.com/article/building-wifi-scanner-in-python-scapy 
# for Windows I have to do py2exe so Windows users can use it 
import subprocess # Allow us to use system commands
# import pywifi # to manipulating wireless interfacess [Windows/Linux]
import time # to run the scan everyonce in a while
import re   # Regular expressions
#import scapy 
wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
iface.scan()
time.sleep(0.5)
results = iface.scan_results()


for i in results:
    bssid = i.bssid
    ssid  = i.ssid
    print(f"{bssid}: {ssid}")