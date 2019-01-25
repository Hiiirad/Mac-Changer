from subprocess import call
from re import search

# Validating mac address
mac = input("Please insert your new mac: ")
if search(string=mac, pattern=r"^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$"):
    print("Valid mac")
else:
    print("Invalid mac. Check it and try again")
    quit()

# Start changing mac address
call("ifconfig eth0 down", shell=True)
call("ifconfig eth0 hw ether {0}".format(mac), shell=True)
call("ifconfig eth0 up", shell=True)
