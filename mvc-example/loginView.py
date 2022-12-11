import tkinter as tk
from tkinter import ttk
#from tkinter.messagebox import showinfo
from LoginController import * 

       
#GUI
class Login_View(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
  
        self.__username = tk.StringVar()
        self.__password = tk.StringVar()
        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.username_entry = ttk.Entry(self, textvariable=self.__username)
        self.username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.password_entry = ttk.Entry(self, textvariable=self.__password, show="*")
        self.password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
        self.login_button = ttk.Button(self, text="Login", command=self.login)
        self.login_button.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)
        self.signup_button = ttk.Button(self, text="SignUp", command=self.signup)
        self.signup_button.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

        self.message_label = ttk.Label(self, text='                                    ', foreground='black')
        self.message_label.grid(column=1, row=4, padx=5, pady=5)           

        self.controller = None

        
    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def set_controller(self, controller):
        self.controller = controller
    
    def show_success(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        self.username_entry.delete(0,'end')
        self.password_entry.delete(0,'end')
        self.username_entry['foreground'] = 'black'
        self.password_entry['foreground'] = 'black'
        self.__username.set('')
        self.__password.set('')
    
    def hide_message(self):
        self.message_label['text'] = ''
    
    def show_error(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'        
        self.username_entry['foreground'] = 'red'
        self.password_entry['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)

    def login(self):
        if self.controller:
            self.controller.login(self.__username.get(), self.__password.get())
              
    def signup(self):
        if self.controller:
            self.controller.signup(self.__username.get(), self.__password.get())
    