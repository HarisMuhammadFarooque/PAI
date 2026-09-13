class Agent:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def perform_task(self):
        return None

class SecurityAgent(Agent):
    def __init__(self, name, status):
        super().__init__(name, status)

    def perform_task(self):
        print("Security Agent- Detecting cyber threat!")

class MonitoringAgent(Agent):
    def __init__(self, name, status):
        super().__init__(name, status)

    def perform_task(self):
        print("Monitoring Agent- Monitoring System Activity!")

class RecoveryAgent(Agent):
    def __init__(self, name, status):
        super().__init__(name, status)

    def perform_task(self):
        print("Recovery Agent- Recovering system services!")

s1 = SecurityAgent("Security Chatbot", "Active")
m1 = MonitoringAgent("Monitoring Agent", "Active")
r1 = RecoveryAgent("Recovery Agent", "Active")

s1.perform_task()
r1.perform_task()
m1.perform_task()
