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
# Author: Roel van den Bussche                                                                              #
#############################################################################################################

print("Let's Go!")