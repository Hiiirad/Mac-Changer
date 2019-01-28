from subprocess import call
from re import search

# Validating mac address
mac = input("Please insert your new mac: ")
if search(string=mac, pattern=r"^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$"):
    print("Valid mac")
else:
    print("Invalid mac. Check it and try again")
    quit()

# Validating Interface
interface = input("Please insert name of the interface you want to change its mac: ")
if search(string=interface, pattern=r"^(eth|wlan)\d{1}$"):
    print("Valid interface")
else:
    print("Invalid Interface. Check it and try again")
    quit()

# Start changing mac address
call("ifconfig {0} down", shell=True)
call("ifconfig {0} hw ether {1}".format(interface, mac), shell=True)
call("ifconfig {0} up", shell=True)
