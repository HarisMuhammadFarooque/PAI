class PasswordVault:
    def __init__(self, name, vaultStatus, password):
        self.name = name
        self._vaultstatus = vaultStatus
        self.__password = password

    def verifyPassword(self, password):
        if self.__password == password:
            return True
        else:
            return False

    def changePassword(self):
        oldPass = input("Enter Password: ")
        if self.verifyPassword(oldPass):
            newPass = input("Enter new password: ")
            self.__password = newPass
            print("Password Changed Successfully!\n")
        else:
            print("Sorry! Password not verified!\n")

    def displayStatus(self):
        print(f"Name: {self.name}\nVault Status: {self._vaultstatus}\n")

p1 = PasswordVault("Basement Vault", "Closed", "haris1231")
p1.changePassword()
p1.changePassword()
p1.displayStatus()

        