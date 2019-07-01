import scapy.all as scapy

def ArpRequest(ip):
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
     print("IP\t\t\tMAC Address\n--------------------------------")
     for target in target_list:
         print(target["ip"] + "\t\t"  + target["mac"])


arp_scan = ArpRequest("192.168.1.0/24")
ShowArpScan(arp_scan)