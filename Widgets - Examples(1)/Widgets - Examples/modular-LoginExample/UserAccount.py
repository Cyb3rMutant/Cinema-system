#User class
class UserAccount:
    def __init__(self, user, password):
        self.__user = user
        self.__password = password
    
    def getUser(self):
        return self.__user

    def setUser(self, user):
        self.__user = user
    
    def getPassword(self):
        return self.__password

    def setUser(self, password):
        self.__password = password
    
    def getPasswordLength(self):
        return len(self.getPassword())

    def __str__(self):
        print("User: " + self.getUser() + " Password: " + self.getPassword())