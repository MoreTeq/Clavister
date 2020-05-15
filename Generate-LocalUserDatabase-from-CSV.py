#############################################################################################################
# Generate LocalUserDatabase from CSV file (user,password)                                                  #
#                                                                                                           #
# Needed for this script:                                                                                   #
# - users.csv                                                                                               #
#                                                                                                           #
# The generated script will add a LocalUserDatabase populated with the contents of the users.csv file.      #
#                                                                                                           #
# Contact: Roel van den Bussche (roel@moreteq.com)                                                          #
#############################################################################################################

#!/usr/bin/python3

import csv

import_file = input("Locate CSV file (user,password): ")
clav_user_db = input("Name for new LocalUserDatabase: ")

f = open(import_file, 'r')
of = open('Generate-LocalUserDatabase-and-Populate.sgs', 'w')

of.write("add LocalUserDatabase "+clav_user_db)
of.write("\n")
of.write("cc LocalUserDatabase "+clav_user_db)
of.write("\n")

with f:
        reader = csv.reader(f)
        for row in reader:
                of.write("add User "+row[0]+" Password="+row[1])
                of.write("\n")

of.close()

print("Generated Clavister script for importing a LocalUserDatabase from CSV: "+import_file)