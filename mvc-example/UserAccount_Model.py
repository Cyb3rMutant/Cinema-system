import re 
from DataAccessObject import *

con = getConn()
c = getCursor()

#User class
class UserAccountModel:
    def __init__(self):
        self.__user = ""
        self.__password = ""
    
    def getUser(self):
        return self.__user

    def setUser(self, user):
        if self.validateUsernameSyntax(user):   #validating pattern
            self.__user = user
            return 1
        else:
            return 0
    
    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        if self.validateUserpasswordSyntax(password):
            self.__password = password
            return 1
        else:
            return 0
    
    def getPasswordLength(self):
        return len(self.getPassword())

    def validateUsernameSyntax(self, username):
        #write logic to validate username e.g., start with a letter and minimum 6 letters or numbers
        if len(username) > 0:
            pattern = r'[A-Za-z0-9]{6,}'
            if re.fullmatch(pattern, username):
                return 1
            else:
                return 0
        else:
            return 0

    def validateUserpasswordSyntax(self, pw):
        #write logic to validate username e.g., start with a letter and minimum 8 letters or numbers
        if len(pw) > 0:
            pattern = r'[A-Za-z0-9 ]{8,}'
            if re.fullmatch(pattern, pw):
                return 1
            else:
                return 0
        else:
            return 0

    def saveUserNamePassword(self, un, pw): #save username and password in database
        if self.checkUserNamePassword(un, pw):  
            print('Username or Password already exists or syntax error')
            return 0
        else:
            query = 'INSERT INTO users (username, password) VALUES (? , ?);'
            c.execute(query, (un, pw))
            conn.commit()
            print('Username and password successfully saved')
            return 1

    def checkUserNamePassword(self, un, pw): #check if un and password exist
       # if len(un) < 1 or len(pw) < 1:    #This is could be done in validateUser and PW methods...
       #         print('Empty username and password')
       #         return 1
       # else: 
        query = 'SELECT username, password FROM users WHERE username = ? and password = ?;'
        c.execute(query, (un, pw))
        record = c.fetchall()
        print('Type is : ', type(record))
        if len(record)>0:
            print('record exists')
            return 1    #record exists
        else:
            print('record does not exist')
            return 0    #record does not exist   

        
    def __str__(self):
        print("User: " + self.getUser() + " Password: " + self.getPassword())