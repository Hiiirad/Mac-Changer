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
random_or_not = input("Do you want your mac address to change randomly? [(Y)es or (N)o]\nOr\nDo you want your mac address back to original one? [(R)everse]").lower()
interface = input("Please insert name of the interface you want to change its mac: [wlan* or eth*] ")
interface_validation(interface)
print("Your username is:")
call("echo $USER > /tmp/user.txt", shell=True)
with open(file="/tmp/user.txt", mode="r", encoding="utf-8") as username:
    user = username.readline()

if random_or_not == "y" or random_or_not == "yes":
    # random mac
    hex_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    random_mac = []
    for i in range(6):
        random_mac.append("".join(sample(hex_characters, 2)))
    random_mac = ":".join(random_mac)
    print("Your new mac address will be {0}".format(random_mac))
elif random_or_not == "n" or random_or_not == "no":
    # user's new mac
    mac = input("Please insert your new mac: ")
    mac_validation(mac)
elif random_or_not == "r" or random_or_not == "reverse":
    # back to normal
    if search(string=interface, pattern=r"^eth\d{1}$"):
        with open(file="/home/{0}/eth-old-mac.txt".format(user), mode="r", encoding="utf-8") as old_mac:
            mac = old_mac.readline()
    elif search(string=interface, pattern=r"^wlan\d{1}$"):
        with open(file="/home/{0}/wlan-old-mac.txt".format(user), mode="r", encoding="utf-8") as old_mac:
            mac = old_mac.readline()
else:
    print("Please check your answer!")
    quit()

# Saving old mac addresses
# 1st mac: Ethernet
# 2nd mac: Wireless
if random_or_not == "r" or random_or_not == "reverse":
    delete = print("Do you want to delete files related to your old mac address? [(Y)es or (N)o]").lower()
    if delete == "y" or delete =="yes":
        call("rm /home/{0}/eth-old-mac.txt /home/{1}/wlan-old-mac.txt".format(user, user), shell=True)
    elif delete == "n" or delete =="no":
        pass
    else:
        print("Please check your answer! What do you want to do with old mac address text files?!")
        quit()
else:
    call("ip addr | grep -E 'ether' | cut --delimiter=' ' -f 6 | sed -n '1p' > /home/{0}/eth-old-mac.txt".format(user), shell=True)
    call("ip addr | grep -E 'ether' | cut --delimiter=' ' -f 6 | sed -n '2p' > /home/{0}/wlan-old-mac.txt".format(user), shell=True)

# Removing unnecessary file
call("rm /tmp/user.txt", shell=True)

# Start changing mac address
call("ifconfig {0} down".format(interface), shell=True)
call("ifconfig {0} hw ether {1}".format(interface, mac), shell=True)
call("ifconfig {0} up".format(interface), shell=True)

print("\nDone :)")
