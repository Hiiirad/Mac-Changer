from subprocess import call

mac = input("Please insert your new mac: ")
# 00:11:22:33:44:55
call("ifconfig eth0 down", shell=True)
call("ifconfig eth0 hw ether {0}".format(mac), shell=True)
call("ifconfig eth0 up", shell=True)