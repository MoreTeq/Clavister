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
        else:
            interfaces = ()
        return interfaces