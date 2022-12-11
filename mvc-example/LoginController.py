from UserAccount_Model import *

class Login_Controller:
    def __init__(self, model, view):
        self.model = model 
        self.view = view

    def signup(self, username, password):        
        try:
            #if self.model.validateUsernameSyntax(username):    #check username syntax
            if self.model.setUser(username):    #check username syntax
                #if self.model.validateUserpasswordSyntax(password):    #check password syntax 
                if self.model.setPassword(password):
                    if self.model.saveUserNamePassword(username, password): #save username and password
                        print('username and password saved')                        
                        self.view.show_success(f'The username {username} and password saved!')
                    else:
                        print('username and password could not be saved!')                        
                        self.view.show_error(f'The username {username} and password could not be saved!')
                else:
                    #pass
                    print('password syntax is incorrect')
                    self.view.show_error('password syntax is incorrect!')
            else:
                #pass
                print('username syntax is incorrect')
                self.view.show_error('username syntax is incorrect!')        
                    
        except ValueError as error:
            self.view.show_error(error)


    def login(self, username, password):
        try:
            if self.model.validateUsernameSyntax(username):    #check username syntax
                if self.model.validateUserpasswordSyntax(password):    #check password syntax 
                    if self.model.checkUserNamePassword(username, password): #check if user exists
                        print('username and password found')
                        self.view.show_success('Successful login!')
                    else:
                        print('username or password does not exist')
                        self.view.show_error('Login failed!')
                else:
                    #pass
                    print('username or password does not exist - password syntax is incorrect')
                    self.view.show_error('Login failed! pw syntax is incorrect')
            else:
                #pass
                print('username or password does not exist - username syntax is incorrect')
                self.view.show_error('Login failed! username syntax is incorrect!')    
        except ValueError as error:
            self.view.show_error(error)
