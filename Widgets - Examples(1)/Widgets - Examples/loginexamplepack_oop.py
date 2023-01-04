#Source: https://www.pythontutorial.net/tkinter/tkinter-pack/
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("350x220")
        self.title('Login')
        self.create_widgets()

    def create_widgets(self):        
        username = tk.StringVar()
        password = tk.StringVar()

        fields = {} # dictionary
        fields['username_label'] = ttk.Label(text='Username:')
        fields['username'] = ttk.Entry(textvariable=username)
        fields['password_label'] = ttk.Label(text='Password:')
        fields['password'] = ttk.Entry(textvariable=password, show="*")

        for field in fields.values():
            field.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        ttk.Button(text='Login', command=lambda : self.login(username, password)).pack(anchor=tk.W, padx=10, pady=5)    
    
    def login(self, username, password):
        print("User name : " + username.get() + "\nPassword : " + password.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()


