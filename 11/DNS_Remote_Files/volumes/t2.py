#!/usr/bin/python3
from scapy.all import *
import random
import string

# 目标 DNS 服务器的 IP 地址
TARGET_DNS_SERVER = "10.9.0.53"


# 生成随机事务 ID
def generate_random_id():
    return random.randint(0, 65535)  # 16 位随机数

# 构建 DNS 查询包
def build_dns_query_packet(src_ip, dst_ip, src_port, dst_port, domain):
    ip = IP(src=src_ip, dst=dst_ip)
    udp = UDP(sport=src_port, dport=dst_port, chksum=0)
    dns_qr = DNSQR(qname=domain)
    dns = DNS(id=generate_random_id(), qr=0, qdcount=1, qd=dns_qr)
    packet = ip / udp / dns
    return packet

# 发送多个 DNS 查询请求
def send_multiple_dns_queries(target_ip, num_queries):
    for _ in range(num_queries):
        random_subdomain = "djy2022141530010.example.com"
        random_src_ip = "1.2.3.4"  # 可以随机化或固定
        random_src_port = random.randint(1024, 65535)
        packet = build_dns_query_packet(random_src_ip, target_ip, random_src_port, 53, random_subdomain)
        send(packet, verbose=0)
        print(f"发送 DNS 查询请求：{random_subdomain} 到 {target_ip}")

if __name__ == "__main__":
    NUM_QUERIES = 100  # 发送查询的数量
    send_multiple_dns_queries(TARGET_DNS_SERVER, NUM_QUERIES)

