#Adapted from source: https://www.pythontutorial.net/tkinter/tkinter-entry/
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry("400x200")
root.resizable(False, False)
root.title('Login Window')

# To store email address and password values
email = tk.StringVar()
password = tk.StringVar()

# callback function when button is clicked
def login_clicked():
    """ callback when the login button clicked
    """
    msg = f'You entered email: {email.get()}, and password: {password.get()}'
    showinfo(title='Information', message=msg)

# Creating a frame for Login/Sign-in
#Frame needs root window as parameter
signin = ttk.Frame(root).pack(padx=10, pady=10, fill='x', expand=True) #fill=x will fill x-axis space..

# email label
email_label = ttk.Label(signin, text="Email Address:").pack(fill='x', expand=True)

# email entry box and linking textvariable with email variable
email_entry = ttk.Entry(signin, textvariable=email).pack(fill='x', expand=True)
#email_entry.focus() #focus means control will be in this field when window is loaded and user can enter data
#focus is not working on my Macbook

# password label
password_label = ttk.Label(signin, text="Password:").pack(fill='x', expand=True)

# password entry box and linking textvariable with password. show="*" will make the text as */hidden
password_entry = ttk.Entry(signin, textvariable=password, show="*").pack(fill='x', expand=True)

# login button
login_button = ttk.Button(signin, text="Login", command=login_clicked).pack(fill='x', expand=True, pady=10)
    
root.mainloop()