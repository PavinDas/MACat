# MACat

A Python script to change the MAC address of a network interface on a Linux system. This tool is useful for network testing, privacy, or troubleshooting.

<img src="https://socialify.git.ci/PavinDas/WiFried/image?description=1&font=KoHo&language=1&name=1&owner=1&pattern=Solid&theme=Dark" alt="Socket" width="640" height="320" />

---

## Features

- Retrieve the current MAC address of a network interface.
- Change the MAC address to a user-specified or predefined value.
- Supports multiple MAC addresses from a file (`addresses.txt`).
- Colorful terminal output for better readability.
- Graceful handling of interruptions (e.g., `Ctrl+C`).

---

## Prerequisites

- Python 3.x
- Linux-based operating system (tested on Ubuntu/Debian)
- `ifconfig` utility installed
- `colorama` library for colored terminal output

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PavinDas/MACat.git
   cd MACat
   ```
2. Install the required Python library:
    ```bash
    pip install colorama
    ```
3. Ensure ifconfig is installed:
    ```bash
    sudo apt install net-tools
    ```

---

## Usage

1. change permission
    ```bash
    chmod +x macat.py
    ```
2. Run the script:
    ```bash
    python macat.py
    ```
3. Follow the prompts:
    * Enter the network interface (e.g., eth0, wlan0, wlo1).
    * The script will cycle through the MAC addresses in addresses.txt, changing the MAC address every 5 seconds.
    * To stop the script, press Ctrl+C

---

## Example 

```bash 
$ python mac_changer.py

██████   ██████   █████████     █████████             █████   
░░██████ ██████   ███░░░░░███   ███░░░░░███           ░░███    
░███░█████░███  ░███    ░███  ███     ░░░   ██████   ███████  
░███░░███ ░███  ░███████████ ░███          ░░░░░███ ░░░███░   
░███ ░░░  ░███  ░███░░░░░███ ░███           ███████   ░███    
░███      ░███  ░███    ░███ ░░███     ███ ███░░███   ░███ ███
█████     █████ █████   █████ ░░█████████ ░░████████  ░░█████ 
░░░░░     ░░░░░ ░░░░░   ░░░░░   ░░░░░░░░░   ░░░░░░░░    ░░░░░  

[+] Creator    :  Pavin Das
[+] GitHub     :  PavinDas
[+] Instagram  :  pavin__das

Enter Interface: wlan0

[+] Current MAC Address: 00:11:22:33:44:55
[+] Changing MAC Address to: 66:77:88:99:AA:BB
[+] Changing MAC Address...

[+] New MAC Address: 66:77:88:99:AA:BB
[+] Done!
```
---

## Notes 

* This script requires root privileges to change the MAC address. Run it with sudo if necessary.
* Ensure the MAC address format is valid (e.g., 00:11:22:33:44:55).
* Use this tool responsibly and in compliance with local laws and regulations.

---

## Disclaimer 

This tool is intended for educational and ethical purposes only. The author is not responsible for any misuse or damage caused by this software.

--- 

## How to Use This README

1. Save the content above as `README.md` in your project directory.
2. Customize the sections (e.g., author details, license) as needed.
3. Push the file to your GitHub repository or include it in your project distribution.

This README provides a professional and comprehensive overview of your project, making it easier for users to understand and use your tool.
```