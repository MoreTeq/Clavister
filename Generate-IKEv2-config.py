#############################################################################################################
# Generate "Roaming VPN (Simplified)" config file for Clavister 12.00.13                                    #
#                                                                                                           #
# Needed for this script:                                                                                   #
# - CA Cert                                                                                                 #
# - Gateway Cert                                                                                            #
# - Gateway Private Key                                                                                     #
# - Network information                                                                                     #
#     - Subnet                                                                                              #
#     - IP Pool for VPN users                                                                               #
#     - DNS for DNS users                                                                                   #
# - User Database - Local or RADIUS                                                                         #
#                                                                                                           #
# The generated script will add a variety of objects used for the Roaming VPN configuration.                #
#                                                                                                           #
# Contact: Roel van den Bussche (roel@moreteq.com)                                                          #
#############################################################################################################

preset = input("Enter preset for object names (i.e. Roaming_): ")

# pool
vpn_pool = input("Enter IP pool for Roaming VPN Clients (i.e. 10.2.0.100-10.2.0.150): ")

# dns
vpn_dns = input("Enter DNS server for Roaming VPN Client: ")

# CA Cert
ca_cert = input("Please manually upload the CA certificate via Clavister webgui. And copy/past object name (i.e. CA_cert): ")

# Gateway Cert
gw_cert = input("Please manually upload the gateway certificate + private key via Clavister webgui. And copy/past object name (i.e. GW_cert): ")

print("Let's Go!")


#add Address IP4Address tesddt Address=192.168.0.33
#add Interface RoamingVPN test IPPoolAddress=Personal-VPN/Roaming_pool AuthSource=RADIUS RadiusServer=RPI0 GatewayCertificate=remote-roebus-nl RootCertificates=root-roebus-nl DNS=DNS
