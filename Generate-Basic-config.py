#############################################################################################################
# Generate "Basic IP config" config file for Clavister 12.00.13                                             #
#                                                                                                           #
# Needed for this script:                                                                                   #
# - Physical config (G1, G2, GS, etc.)                                                                      #
# - IP Config for physical ports                                                                            #
#   - IP address                                                                                            #
#   - Gateway address (can be empty)                                                                        #
#   - Network                                                                                               #
#                                                                                                           #
# The generated script will edit the default objects for the interfaces.                                    #
#                                                                                                           #
# Contact: Roel van den Bussche (roel@moreteq.com)                                                          #
#############################################################################################################
from Clavister import Clavister

model = input("Enter model (E10, E20, E80, W20, W30, W40): ")

myClavister = Clavister(model)
interfaceFolder = "InterfaceAddresses"

interfaces = []
for interface in myClavister.interfaces():
    if_setting = []
    if_setting.append(interface)
    skip = input(interface + ": Skip this interface (y or n): ")
    if skip == "y":
        continue

    dhcp = input(interface + ": DHCP Client (y or n): ")

    if dhcp == "y":
        if_setting.append(True)
    else:
        if_setting.append(False)
        if_setting.append(input(interface + ": Enter IP (192.168.0.1): "))
        if_setting.append(input(interface + ": Enter default gateway: "))
        if_setting.append(input(interface + ": Enter network (192.168.0.0/24): "))

    interfaces.append(if_setting)

for interface in interfaces:
    print(interface)

print("")
print("Start generating...")
print("")

# Generate SGS file
config_file = open("Basic-config.sgs", "w")

for interface in interfaces:
    interface_name = interface[0]
    interface_dhcp = interface[1]
    if interface_dhcp == False:
        interface_ip = interface[2]
        interface_gw = interface[3]
        interface_net = interface[4]

    if interface_dhcp == True:
        config_file.write("set Interface Ethernet " + interface_name + " DHCPEnabled=Yes")
        config_file.write("\n")
    elif interface_dhcp == False:
        config_file.write("set Interface Ethernet " + interface_name + " DHCPEnabled=No")
        config_file.write("\n")
        if interface_ip:
            config_file.write("set Address IP4Address " + interfaceFolder + "/" + interface_name + "_ip Address=" + interface_ip)
            config_file.write("\n")
        if interface_gw:
            config_file.write("set Address IP4Address " + interfaceFolder + "/" + interface_name + "_gw Address=" + interface_gw)
            config_file.write("\n")
        if interface_net:
            config_file.write("set Address IP4Address " + interfaceFolder + "/" + interface_name + "_net Address=" + interface_net)
            config_file.write("\n")

config_file.close()

print("Config file successfully generated. Please import through webgui: Status -> Maintenance -> Import Script. Verify changes and commit changes.")