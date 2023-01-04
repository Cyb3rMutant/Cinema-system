import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

users = []

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
        
#GUI
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("250x120")
        self.title('Login')
        self.resizable(0, 0)        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.create_widgets()

    def create_widgets(self):        
        username = tk.StringVar()
        password = tk.StringVar()
        username_label = ttk.Label(self, text="Username:").grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        username_entry = ttk.Entry(self, textvariable=username).grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        password_label = ttk.Label(self, text="Password:").grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        password_entry = ttk.Entry(self, textvariable=password, show="*").grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
        login_button = ttk.Button(self, text="Login", command=lambda : self.login(username, password)).grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)
        signup_button = ttk.Button(self, text="SignUp", command=lambda : self.signup(username, password)).grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)
    
    def login(self, username, password):
        check = 0
        for user in users:
            if user.getUser() == username.get():
                if user.getPassword() == password.get():
                    check=1
                    print("Successful Login: User name : " + username.get() + "\nPassword : " + password.get())
                    msg = "Successful Login: User name : " + username.get() + "\nPassword : " + password.get()
                    showinfo(title='Information', message=msg)
                    break
                else:
                    continue
            else:
                continue

        if not check:
            print("Login Failed: username of password does not match")
            showinfo(title="Error", message="Login Failed: username of password does not match")
        
    def signup(self, username, password):
        print("User name : " + username.get() + "\nPassword : " + password.get())
        #No checks being made here
        user = UserAccount(username.get(), password.get())
        users.append(user)       

if __name__ == "__main__":
    app = App()    
    app.mainloop()



#Source adapted from: https://www.pythontutorial.net/tkinter/tkinter-grid/