#!/usr/bin/env python3
import sys
from scapy.all import sniff, ARP

# Dictionary to store known IP to MAC address mappings
ip_mac_table = {}

def process_packet(packet):
    # Check if the packet is an ARP packet and a reply (op=2)
    if packet.haslayer(ARP) and packet[ARP].op == 2:
        ip = packet[ARP].psrc
        mac = packet[ARP].hwsrc

        # If the IP is already in our table, verify the MAC address
        if ip in ip_mac_table:
            if ip_mac_table[ip] != mac:
                print(f"\n[!] ALERT: Potential ARP Spoofing Detected!")
                print(f"    IP Address: {ip}")
                print(f"    Original MAC: {ip_mac_table[ip]}")
                print(f"    New MAC (Attacker?): {mac}\n")
        else:
            # First time seeing this IP, store its real MAC address
            ip_mac_table[ip] = mac
            print(f"[*] Learned: {ip} is at {mac}")

def main():
    # Determine network interface (default is eth0, change if using wlan0)
    interface = "eth0"
    if len(sys.argv) > 1:
        interface = sys.argv[1]

    print(f"[*] Starting ARP Detector on interface: {interface}")
    print("[*] Monitoring local network traffic... (Press Ctrl+C to exit)")
    
    # Sniff only ARP packets on the specified interface
    sniff(iface=interface, store=False, prn=process_packet, filter="arp")

if __name__ == "__main__":
    main()
