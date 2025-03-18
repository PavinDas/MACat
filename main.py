import subprocess
import re
import time

class MacChanger:

    def getMac(iface):
        op = subprocess.run(f"ifconfig {iface}", shell=True, capture_output=True)
        result = op.stdout.decode()
        pattern  = r"ether\s[\da-fA-F]{2}:[\da-fA-F]{2}:[\da-fA-F]{2}:[\da-fA-F]{2}:[\da-fA-F]{2}:[\da-fA-F]{2}"
        regex = re.compile(pattern)
        mac = regex.search(result).group().split(" ")[1]
        return mac
    
    def changeMac(iface, new_mac):

        print("[+] Current MAC Addres: " + MacChanger.getMac(iface))
        print("[+] Changing MAC Address to: " + new_mac)
        print("[+] Changing MAC Address...")

        subprocess.run(f"ifconfig {iface} down", shell=True)
        change_result = subprocess.run(f"ifconfig {iface} hw ether {new_mac}", shell=True, capture_output=True) 
        if change_result.returncode != 0:
            print("[!] Failed to change MAC Address. Possible issue with address format or interface.")
            subprocess.run(f"ifconfig {iface} up", shell=True)
            return
        subprocess.run(f"ifconfig {iface} up", shell=True)

        print("[+] New MAC Address: " + MacChanger.getMac(iface))
        print("[+] Done!")

        
    def main():
        subprocess.run("ifconfig", shell=True)
        iface = input("Enter Interface: ")
        new_mac = input("Enter New MAC Address: ")
        MacChanger.changeMac(iface, new_mac)
        MacChanger.main();

if __name__ == "__main__":
    MacChanger.main()