from Clavister import Radius

NewRadius = Radius(
    input("Name for RADIUS Object: "),
    input("Radius server IP: "),
    input("Radius server port: "),
    input("Radius shared secret: ")
)

config_file = open("Radius-config.sgs", "w")

for entry in NewRadius.config_lines():
    config_file.write(entry)
    config_file.write("\n")

config_file.close()

print("Config file successfully generated. Please import through webgui: Status -> Maintenance -> Import Script. Verify changes and commit changes.")