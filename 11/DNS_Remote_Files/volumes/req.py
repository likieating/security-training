#!/bin/env python3
from scapy.all import *

srcIP = '10.0.0.5'  
dstIP = '10.9.0.53'  # Local DNS Server
ip  = IP (dst=dstIP, src=srcIP)
udp = UDP(dport=53, sport=50945, chksum=0)

# The C code will modify the qname field
Qdsec = DNSQR(qname='austi.example.com')
dns   = DNS(id=0xAAAA, qr=0, qdcount=1, qd=Qdsec)

pkt = ip/udp/dns
with open('ip_req.bin', 'wb') as f:
    f.write(bytes(pkt))

