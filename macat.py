import subprocess
import re
import time
from colorama import init, Fore, Style

init()

class MacChanger:

    def getMac(iface):
        op = subprocess.run(f"ifconfig {iface}", shell=True, capture_output=True)
        result = op.stdout.decode()
        pattern  = r"ether\s[\da-fA-F]{2}:[\da-fA-F]{2}:[\da-fA-F]{2}:[\da-fA-F]{2}:[\da-fA-F]{2}:[\da-fA-F]{2}"
        regex = re.compile(pattern)
        mac = regex.search(result).group().split(" ")[1]
        return mac
    
    def changeMac(iface, new_mac):

        print(f"{Fore.CYAN}[+] Current MAC Address: {Fore.GREEN}" + MacChanger.getMac(iface) + f"{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] Changing MAC Address to: {Fore.YELLOW}" + new_mac + f"{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] Changing MAC Address...{Style.RESET_ALL}")
        print()
        subprocess.run(f"ifconfig {iface} down", shell=True)
        change_result = subprocess.run(f"ifconfig {iface} hw ether {new_mac}", shell=True, capture_output=True) 
        if change_result.returncode != 0:
            print(f"{Fore.RED}[!] Failed to change MAC Address. Possible issue with address format or interface.{Style.RESET_ALL}")
            subprocess.run(f"ifconfig {iface} up", shell=True)
            return
        subprocess.run(f"ifconfig {iface} up", shell=True)

        print(f"{Fore.CYAN}[+] New MAC Address: {Fore.GREEN}" + MacChanger.getMac(iface) + f"{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] Done!{Style.RESET_ALL}")
        print()
        print()


        
    def main():
        subprocess.run("ifconfig", shell=True)
        iface = input("Enter Interface: ")

        with open("addresses.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.split(" ")[-1]
                MacChanger.changeMac(iface, line)
                time.sleep(5)
        MacChanger.main();

if __name__ == "__main__":
    banner = """\
    ██████   ██████   █████████     █████████             █████   
    ░░██████ ██████   ███░░░░░███   ███░░░░░███           ░░███    
    ░███░█████░███  ░███    ░███  ███     ░░░   ██████   ███████  
    ░███░░███ ░███  ░███████████ ░███          ░░░░░███ ░░░███░   
    ░███ ░░░  ░███  ░███░░░░░███ ░███           ███████   ░███    
    ░███      ░███  ░███    ░███ ░░███     ███ ███░░███   ░███ ███
    █████     █████ █████   █████ ░░█████████ ░░████████  ░░█████ 
    ░░░░░     ░░░░░ ░░░░░   ░░░░░   ░░░░░░░░░   ░░░░░░░░    ░░░░░  
    """
    print(f"{Fore.LIGHTRED_EX}{banner}{Style.RESET_ALL}")
    print()
    print(f"{Fore.RED}{Style.BRIGHT}[+]  Creator    :  Pavin Das{Style.RESET_ALL}")
    print(f"{Fore.RED}{Style.BRIGHT}[+]  GitHub     :  PavinDas{Style.RESET_ALL}")
    print(f"{Fore.RED}{Style.BRIGHT}[+]  Instagram  :  pavin__das{Style.RESET_ALL}")
    print()
    print()
    MacChanger.main()