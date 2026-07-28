# Simple ARP Spoofing Detector

A lightweight Python script that monitors local network traffic for ARP spoofing or poisoning attacks using the Scapy library.

## Features
* Passively sniffs ARP traffic on a specified interface.
* Automatically maps network IP addresses to their hardware (MAC) addresses.
* Alerts the user in real-time if an IP address attempts to change its MAC mapping (potential MitM attack).

## Prerequisites
This script requires **Python 3** and the **Scapy** library. Scapy is pre-installed on Kali Linux. If you need to install it manually:

```bash
sudo apt update && sudo apt install python3-scapy -y
```

## Usage
Because Scapy interacts with network sockets at a low level, the script must be executed with **root privileges**.

1. Clone this repository (if running on a different machine):
   ```bash
   git clone https://github.com
   cd arp-detector
   ```

2. Make the script executable:
   ```bash
   chmod +x arp_detector.py
   ```

3. Run the script (defaults to `eth0`):
   ```bash
   sudo ./arp_detector.py
   ```

4. *(Optional)* Specify a different network interface (e.g., `wlan0`):
   ```bash
   sudo ./arp_detector.py wlan0
   ```

## License
This project is open-source and available under the MIT License.
