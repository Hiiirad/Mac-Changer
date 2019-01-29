from subprocess import call
from re import search
from random import sample

'''
List of standard OUI:
http://standards-oui.ieee.org/oui/oui.txt
http://standards-oui.ieee.org/oui/oui.csv
'''

# Validating mac address
def mac_validation(mac):
    if search(string=mac, pattern=r"^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$"):
        return "Valid mac"
    else:
        print("Invalid mac. Check it and try again")
        quit()

# Validating Interface
def interface_validation(interface):
    if search(string=interface, pattern=r"^(eth|wlan)\d{1}$"):
        return "Valid interface"
    else:
        print("Invalid Interface. Check it and try again")
        quit()

# Checking if user wants to choose new mac address randomly or not
random_or_not = input("Do you want your mac address to change randomly? [(Y)es or (N)o] ").lower()
if random_or_not == "y" or random_or_not == "yes":
    # random mac
    hex_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    random_mac = []
    for i in range(6):
        random_mac.append("".join(sample(hex_characters, 2)))
    random_mac = ":".join(random_mac)
    print("Your new mac will be {0}".format(random_mac))
elif random_or_not == "n" or random_or_not == "no":
    mac = input("Please insert your new mac: ")
    mac_validation(mac)
else:
    print("Please check your answer!")
    quit()

interface = input("Please insert name of the interface you want to change its mac: [wlan* or eth*] ")
interface_validation(interface)

# Start changing mac address
call("ifconfig {0} down", shell=True)
call("ifconfig {0} hw ether {1}".format(interface, mac), shell=True)
call("ifconfig {0} up", shell=True)
