import tkinter as tk
from tkinter import ttk

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
        login_button = ttk.Button(self, text="Login", command=lambda : self.login(username, password)).grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
    
    def login(self, username, password):
        print("User name : " + username.get() + "\nPassword : " + password.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()



#Source: https://www.pythontutorial.net/tkinter/tkinter-grid/