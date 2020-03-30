class Clavister():
    def __init__(self, model):
        self.model = model

    def interfaces(self):
        if self.model == "E10":
            interfaces = ("WAN", "LAN", "G1", "G2")
        elif self.model == "E20":
            interfaces = ("G1", "G2", "GS")
        elif self.model == "E80":
            interfaces = ("G1", "G2", "G3", "G4", "G5", "G6")
        elif self.model == "W20":
            interfaces = ("G1", "G2", "G3", "G4", "G5", "G6")
        elif self.model == "W30":
            interfaces = ("G1", "G2", "G3", "G4", "G5", "G6")
        elif self.model == "W40":
            interfaces = ("G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8")
        elif self.model == "V2":
            interfaces = ("If1", "If2", "If3")
        elif self.model == "V3":
            interfaces = ("If1", "If2", "If3", "If4")
        elif self.model == "V5":
            interfaces = ("If1", "If2", "If3", "If4", "If5", "If6")
        elif self.model == "V7":
            interfaces = ("If1", "If2", "If3", "If4", "If5", "If6", "If7", "If8")
        elif self.model == "V9":
            interfaces = ("If1", "If2", "If3", "If4", "If5", "If6", "If7", "If8", "If9", "If10")
        elif self.model == "V10":
            interfaces = ("If1", "If2", "If3", "If4", "If5", "If6", "If7", "If8", "If9", "If10")
        else:
            interfaces = ()
        return interfaces

class Radius():
    def __init__(self, name, server, port, key):
        self.RadiusName = name
        self.RadiusServer = server
        self.RadiusPort = port
        self.RadiusKey = key

    def config_lines(self):
        cli = []
        cli.append("add Address IP4Address RadiusServer Address=" + self.RadiusServer)
        cli.append("add PSK RadiusKey Type=ASCII PSKAscii=" + self.RadiusKey)
        cli.append("add RadiusServer " + self.RadiusName + " IPAddress=RadiusServer SharedSecret=RadiusKey Port=" + self.RadiusPort)
        return cli