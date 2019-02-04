from subprocess import call
from re import search
from random import sample, choice
from csv import reader
from os import popen

'''
The strings, input and output of this program is in lowercase. => case-insensitive

List of standard OUI:
http://standards-oui.ieee.org/oui/oui.txt
http://standards-oui.ieee.org/oui/oui.csv
'''

# Validating mac address
def mac_validation(mac):
    if search(string=mac, pattern=r"^([0-9a-f]{2}:){5}[0-9a-f]{2}$"):
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

hex_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

# Checking if user wants to choose new mac address randomly or not
random_or_not = input("Do you want your mac address to change randomly? [(Y)es or (N)o]\nOr\nDo you want to choose first part of your mac address based on other manufacturers mac address? [(O)UI]\nOr\nDo you want your mac address back to original one? [(R)everse]\nYour answer: ").lower()
interface = input("Please insert name of the interface you want to change its mac: [wlan* or eth*] ").lower()
interface_validation(interface)

if random_or_not == "y" or random_or_not == "yes":
    # random mac
    random_mac = []
    for i in range(6):
        random_mac.append("".join(sample(hex_characters, 2)))
    random_mac = ":".join(random_mac)
    print("Your new mac address will be {0}".format(random_mac))
elif random_or_not == "n" or random_or_not == "no":
    # user's new mac
    mac = input("Please insert your new mac: ").lower()
    mac_validation(mac)
elif random_or_not == "r" or random_or_not == "reverse":
    # back to normal
    if search(string=interface, pattern=r"^eth\d{1}$"):
        with open(file="/tmp/eth-old-mac.txt", mode="r", encoding="utf-8") as old_mac:
            mac = old_mac.readline()
    elif search(string=interface, pattern=r"^wlan\d{1}$"):
        with open(file="/tmp/wlan-old-mac.txt", mode="r", encoding="utf-8") as old_mac:
            mac = old_mac.readline()
elif random_or_not == "o" or random_or_not == "oui":
    oui = {}
    # Creating Template of our dictionary (OUI)
    with open(file="oui.csv", mode="r", encoding="utf-8") as csvfile:
        csvreader = reader(csvfile)
        next(csvreader) # ignore first row of csv which is header
        for row in csvreader:
            oui[str(row[2])] = []

    # Fill values of dictionary (OUI)
    with open(file="oui.csv", mode="r", encoding="utf-8") as csvfile:
        csvreader = reader(csvfile)
        next(csvreader) # ignore first row of csv which is header
        for row in csvreader:
            value = oui[str(row[2])]
            if len(str(row[1])) > 6:
                continue
            else:
                value.append(str(row[1]))
                oui[str(row[2])] = value

    # Deleting keys with empty values []
    # 273 keys were deleted from list.
    for key, value in list(oui.items()):
        if value == []:
            del oui[key]

    organization = choice(list(oui.keys()))
    print("You will be using mac address of '{0}' organization.".format(organization))
    random_oui = choice(oui.get("{0}".format(organization)))
    character_need = 12 - len(random_oui)
    mac_without_colon = random_oui + str("".join(sample(hex_characters, character_need)))
    mac = mac_without_colon[0:2] + ":" + mac_without_colon[2:4] + ":" + mac_without_colon[4:6] + ":" + mac_without_colon[6:8] + ":" + mac_without_colon[8:10] + ":" + mac_without_colon[10:12]
    mac = mac.lower()
    print("Your new mac address will be {0}".format(mac))
else:
    print("Please check your answer!")
    quit()

# Saving old mac addresses | delete text files in reverse mode
if random_or_not == "r" or random_or_not == "reverse":
    delete = input("Do you want to delete files related to your old mac address? [(Y)es or (N)o] ").lower()
    if delete == "y" or delete =="yes":
        call("rm /tmp/eth-old-mac.txt /tmp/wlan-old-mac.txt", shell=True)
    elif delete == "n" or delete =="no":
        pass
    else:
        print("Please check your answer! What do you want to do with old mac address text files?!")
        quit()
else:
    call("ip addr | grep -E 'ether' | cut --delimiter=' ' -f 6 | sed -n '1p' > /tmp/eth-old-mac.txt", shell=True)
    call("ip addr | grep -E 'ether' | cut --delimiter=' ' -f 6 | sed -n '2p' > /tmp/wlan-old-mac.txt", shell=True)

# Checking kernel version to call different commands
kernel_version = popen("uname -r").read()
if int(search(string=kernel_version, pattern=r"^\d{1}\.\d{1,2}")) < 4.15:

    # Start changing mac address for kernel versions lower than 4.15
    call("ifconfig {0} down".format(interface), shell=True)
    call("ifconfig {0} hw ether {1}".format(interface, mac), shell=True)
    call("ifconfig {0} up".format(interface), shell=True)
else:

    # Start changing mac address for kernel versions higher than 4.15
    call("ip link set {0} down".format(interface), shell=True)
    call("ip link set {0} address {1}".format(interface, mac), shell=True)
    call("ip link set {0} up".format(interface), shell=True)

print("Done :)")
