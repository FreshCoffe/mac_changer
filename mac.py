import subprocess
import random
import sys
import string
import re
from time import sleep
import os

def slowprint(text):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		sleep(.003)

def get_rand_mac():
    upp_digits = ''.join(set(string.hexdigits.upper()))
    mac = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac += random.choice("02468ACE")
            else:
                mac += random.choice(upp_digits)
        mac += ":"
    return mac.strip(":")


def get_cur_mac(interface):

    output = subprocess.check_output(f"ifconfig {interface}", shell=True).decode()
    return re.search("ether (.+) ", output).group().split()[1].strip()
    

def change_mac(interface, new_mac_address):
    subprocess.check_output(f"ifconfig {interface} down", shell=True)
    subprocess.check_output(f"ifconfig {interface} hw ether {new_mac_address}", shell=True)
    subprocess.check_output(f"ifconfig {interface} up", shell=True)
    

if __name__ == "__main__":
    
    subprocess.call("clear", shell=True)
    slowprint(r"""
 ______   ______   ______   ______   _    _
| _____| |      | | _____| | _____| | |  | |
| |__    |  []  | | |__    | |___   | |__| |
|  _|    |  ____| |  _|     _____ | | ____ |
| |      | |\ \   | |____  |______| | |  | |
| |      | | \ \  |      | Loading  | |  | |
<---------------------------------------------->""")
    print("\n<|Copyright | FRESH | 2022                    |>")
    print("<|Tool: MAC CHANGER                           |>")
    print("<|Please report any bugs | on github          |>")
    print("<|github: github.com/FreshCoffe/mac_changer   |>")
    print("<|Only for educational purposes               |>")
    print("<---------------------------------------------->")
 
    if not 'SUDO_UID' in os.environ.keys():
	    print("Run this program with sudo")
	    exit()

    subprocess.run(["ifconfig"])
    
    interface = input("Interface Input: ")

    new_mac_address = get_rand_mac()
  
    old_mac_address = get_cur_mac(interface)
    print("[*] Old MAC :", old_mac_address)

    change_mac(interface, new_mac_address)

    new_mac_address = get_cur_mac(interface)
    print("[+] New MAC :", new_mac_address)
