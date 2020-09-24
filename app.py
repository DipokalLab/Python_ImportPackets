from scapy.all import *
from scapy.arch.windows import IFACES

import time
n = 50
iface = "Intel(R) Ethernet Connection (7) I219-V"
IFACES.show()

def cap():
    for i in range(0, n):
        packet = sniff(iface=iface, count = 6)
        data = (packet[0].payload)

        #packet.show()

        src_ip = packet[0][1].src
        dst_ip = packet[0][1].dst
        nowtime = time.strftime('%c', time.localtime(time.time()))
        print('\033[95m'+'[ '+nowtime+' ] '+'\033[92m'+src_ip+'\033[94m'+" -> "+'\033[92m'+dst_ip+' \033[96m'+ str(data)) #data

cap()
