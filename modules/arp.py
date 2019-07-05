if  __name__ == "__main__":
    pass

import scapy.all as scapy
import pprint
import requests


def ArpScan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    target_list = []

    for item in answered:
        target_item = {
            "ip": item[1].psrc,
            "mac":item[1].hwsrc
        }
        target_list.append(target_item)
    return target_list

def ShowArpScan(target_list):
     MAC_URL = 'http://macvendors.co/api/%s' 
     print("IP\t\t\tMAC Address\t\t\tVendor\n-----------------------------------------------------------------------------------------")
     for target in target_list:
         vendor_list = requests.get(MAC_URL % target["mac"])
         vendor = vendor_list.json()["result"]["company"]
         print(target["ip"] + "\t\t"  + target["mac"] + "\t\t" + vendor)

   
     