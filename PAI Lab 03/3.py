class SecuritySystem:
    def respond(self):
        print("----- Security system -----")

class Firewall(SecuritySystem):
    def respond(self):
        print("Firewall- Block Suspicious network traffic!")

class AntiVirus(SecuritySystem):
    def respond(self):
        print("AntiVirus- Isolate malicious files!")

class IntrusionDetectionSystem(SecuritySystem):
    def respond(self):
        print("Intrusion Detection System- Generate Security Alert!")

s1 = SecuritySystem()
s1.respond()

f1 = Firewall()
f1.respond()

a1 = AntiVirus()
a1.respond()

i1 = IntrusionDetectionSystem()
i1.respond()