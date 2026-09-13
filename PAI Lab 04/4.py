class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def move(self):
        return None

    def charge(self):
        return None

class DeliveryRobot(Robot):
    def __init__(self, name, battery):
        super().__init__(name, battery)

    def move(self):
        if self.battery >= 20:
            print("Delivery Robot- Moves to a Delivery Location!")
        else:
            print("Delivery Robot- Not Enough Battery!")

    def charge(self, amount):
        if(amount < 0 or amount + self.battery > 100):
                print("Invalid Charging amount!")
        else:
            self.battery += amount
            print("Delivery Robot- Charged!")

class SecurityRobot(Robot):
    def __init__(self, name, battery):
        super().__init__(name, battery)

    def charge(self, amount):
        if(amount < 0 or amount + self.battery > 100):
                print("Invalid Charging amount!")
        else:
            self.battery += amount
            print("Security Robot- Charged!")

    def move(self):
        if self.battery >= 20:
            print("Security Robot- Patrols a specific area!")
        else:
            print("Security Robot- Not Enough Battery!")

class RescueRobot(Robot):
    def __init__(self, name, battery):
        super().__init__(name, battery)

    def charge(self, amount):
        if(amount < 0 or amount + self.battery > 100):
            print("Invalid Charging amount!")
        else:
            self.battery += amount
            print("Rescue Robot- Charged!")


    def move(self):
        if self.battery >= 20:
            print("Rescue Robot- Moves toward a disaster Location!")
        else:
            print("Rescue Robot- Not Enough Battery!")

d1 = DeliveryRobot("Allen", 32)
s1 = SecurityRobot("kayo", 98)
r1 = RescueRobot("Pavilion", 19)

d1.move()
d1.charge(325)

s1.move()

r1.move()
r1.charge(32)
r1.move()