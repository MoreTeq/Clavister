#############################################################################################################
# Generate "Roaming VPN (Simplified)" config file for Clavister 12.00.13                                    #
#                                                                                                           #
# Needed for this script:                                                                                   #
# - CA Cert                                                                                                 #
# - Gateway Cert                                                                                            #
# - Gateway Private Key                                                                                     #
# - Network information                                                                                     #
#     - IP Pool for VPN users                                                                               #
#     - DNS for DNS users                                                                                   #
# - User Database - RADIUS                                                                                  #
#                                                                                                           #
# The generated script will add a variety of objects used for the Roaming VPN configuration.                #
#                                                                                                           #
# Contact: Roel van den Bussche (roel@moreteq.com)                                                          #
#############################################################################################################
def validate_ip(ip):
    octet = ip.split('.')
    if len(octet) != 4:
        return False
    for x in octet:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

def validate_password(pw):
    if len(pw) < 8:
        return False
    return True

preset = input("Enter preset for object names (i.e. Roaming): ")

# pool
vpn_pool_start = ""
vpn_pool_end = ""
while validate_ip(vpn_pool_start) == False:
    vpn_pool_start = input("Enter first IP in pool for Roaming VPN Clients (i.e. 10.2.0.100): ")

while validate_ip(vpn_pool_end) == False:
    vpn_pool_end = input("Enter last IP in pool for Roaming VPN Clients (i.e. 10.2.0.199): ")

vpn_pool = vpn_pool_start+"-"+vpn_pool_end

# dns
vpn_dns = ""
while validate_ip(vpn_dns) == False:
    vpn_dns = input("Enter DNS server for Roaming VPN Client: ")

# User auth - create local user db
user = input("Enter username for local user: ")
password = ""
while validate_password(password) == False:
    password = input("Enter password for user (lowercase + uppercase + number, min 8 chars.): ")

# CA Cert
ca_cert = input("Please manually upload the CA certificate via Clavister webgui. And copy/past object name (i.e. CA_cert): ")

# Gateway Cert
gw_cert = input("Please manually upload the gateway certificate + private key via Clavister webgui. And copy/past object name (i.e. GW_cert): ")

print("")
print("Start generating...")
print("")

# Generate SGS file
config_file = open("IKEv2-config.sgs", "w")
config_file.write("add Address IP4Address "+preset+"_pool Address="+vpn_pool)
config_file.write("\n")
config_file.write("add Address IP4Address "+preset+"_dns Address="+vpn_dns)
config_file.write("\n")
config_file.write("add LocalUserDatabase "+preset+"_users")
config_file.write("\n")
config_file.write("cc LocalUserDatabase "+preset+"_users")
config_file.write("\n")
config_file.write("add user "+user+" Password="+password)
config_file.write("\n")
config_file.write("cc")
config_file.write("\n")
config_file.write("add Interface RoamingVPN "+preset+"_VPN IPPoolAddress="+preset+"_pool AuthSource=Local LocalUserDB="+preset+"_users GatewayCertificate="+gw_cert+" RootCertificates="+ca_cert+" DNS="+preset+"_dns")
config_file.close()

print("Config file successfully generated. Please import through webgui: Status -> Maintenance -> Import Script. Verify changes and commit changes.")