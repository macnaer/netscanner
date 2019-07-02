import argparse
from modules import arp



def get_arguments():
    parser = argparse.ArgumentParser(description= "Net Scanner usage ")
    #parser.add_argument("-a", "--arp", nargs="+",  help="Scan network using arp", "-t", "--target", dest="target", help="Scan network using arp/ Target IP (192.168.1.1) / IP range (192.168.1.0/24) ")
    parser.add_argument("-p", "--proto ",  default="arp", dest="proto",  help="Scan network using network protocols")
    parser.add_argument("-t", "--target", dest="target", help="Target IP (192.168.1.1) / IP range (192.168.1.0/24) ")
    options = parser.parse_args()
    return options



options = get_arguments()
print(options)
if options.proto == "arp":
    arp_scan = arp.ArpScan(options.target)
    arp.ShowArpScan(arp_scan)

    

