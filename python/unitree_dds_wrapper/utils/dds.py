import os

def set_dds_network(address = "192.168.123"):
    """
    Search for the network adapter on the current device and obtain the network adapter 
    that starts with a specific network segment. address First three digits of IPv4    
    """
    for i in os.listdir('/sys/class/net'):
        # en: Ethernet
        # eth: Ethernet Centos 6 Previous system
        # wl: Wireless network
        if i.startswith('en') or i.startswith('eth') or i.startswith('wl'):
            for j in os.popen('ip addr show ' + i).readlines():
                if 'inet ' in j and address in j:
                    CYCLONEDDS_URI = f"<CycloneDDS><Domain><General><NetworkInterfaceAddress>{i}</NetworkInterfaceAddress></General></Domain></CycloneDDS>"
                    os.environ["CYCLONEDDS_URI"] = CYCLONEDDS_URI
                    return