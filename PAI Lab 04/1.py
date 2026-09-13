class ThreatDetector:
    def __init__(self, name, ipAddress, threatLevel):
        self.name = name
        self.ipAddress = ipAddress
        self.threatLevel = threatLevel

    def scan(self):
        if self.threatLevel.lower() == "low":
            print("System Report- System Safe!")
        elif self.threatLevel.lower() == "medium":
            print("System Report- Suspicious Activity!")
        elif self.threatLevel.lower() == "high":
            print("System Report- Critical Threat Detetected!")
        else:
            print("Invalid Threat Level!")

t1 = ThreatDetector("Iphone", "IP6485", "high")
t1.scan()


        