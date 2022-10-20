import tkinter as tk
from tkinter import messagebox
from tkinter import *
from turtle import right
import mysql.connector
from passlib.hash import sha256_crypt



def get_connection():
    conn = mysql.connector.connect(host='localhost',
                                   port='3306',
                                   user='root',
                                   password='',
                                   database='tkinter')
    return conn

def main():
    root = tk.Tk()
    app = Login(root)


class Login:
    def __init__(self,window):
        self.window = window #Window
        self.window.title("Login")
        self.window.geometry("700x600")
        self.window.config(bg="#333333")
        self.frame = tk.Frame(self.window)
        self.frame.config(bg='#333333')

        # Create widgets
        self.login_label = tk.Label(self.frame, text='Login', borderwidth=1, bg='#333333',fg='#DD2424',font=("Arial",32))
        self.username_label = tk.Label(self.frame, text='Username', bg='#333333', fg='#FFFFFF',font=("Arial",18))
        self.username_entry = tk.Entry(self.frame, font=("Arial", 18))
        self.password_label = tk.Label(self.frame, text='Password', bg='#333333', fg='#FFFFFF',font=("Arial",18))
        self.password_entry = tk.Entry(self.frame, show='*', font=("Arial", 18))
        self.login_button = tk.Button(self.frame, text='Login', bg='#DD2424', fg='#000000',font=("Arial",18),command=self.login_verify)


        #Placing widgets
        self.login_label.grid(row=0, column=1, columnspan=2,pady=45)
        self.username_label.grid(row=1, column=1)
        self.username_entry.grid(row=2, column=1, pady=15)
        self.password_label.grid(row=3, column=1)
        self.password_entry.grid(row=4, column=1, pady=15)
        self.login_button.grid(row=5, column=1, columnspan=2,pady=35)


        self.frame.pack()        
        self.window.mainloop()


        
    def login_verify(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()

        conn = get_connection()
        dbcursor = conn.cursor()
        dbcursor.execute("SELECT username, password_hash, usertype \
                                FROM users WHERE username = %s;", (self.username,))
        
        data = dbcursor.fetchone()
        if dbcursor.rowcount < 1:
            messagebox.showerror(title="Error",message="User doesnt exist.")

        else:
            if sha256_crypt.verify(self.password, str(data[1])):
                messagebox.showinfo(title="Login Successful",message="You have successfully logged in.")
                self.window.destroy()
                self.create_dashboard(str(data[0]),str(data[2]))

            else:
                messagebox.showerror(title="Error",message="Incorrect username or password.")

    
    def create_dashboard(self,name,usertype):
        self.root = tk.Tk()
        self.name = name
        self.usertype = usertype
        self.app = Dashboard(self.root,self.name,self.usertype)
        #We can have here if usertype is... then direct it to that class dashboard. We can use inheritence for the classes or hardcode it

    

#Placement of the dashboard is wrong! Ive got the data passing through but this version the placement is all wrong. 
#This dashboard is only so you guys will be able to understand the process of how it works and passes through
class Dashboard:
    def __init__(self, window,name,usertype):
        self.window = window
        self.window.title("Dashboard")
        self.window.geometry("1200x700")
        self.window.config(bg='#333333')
        # self.frame = tk.Frame(self.window)
        # self.frame.config(bg='#333333')

        self.window.columnconfigure(0,weight=1)
        self.window.columnconfigure(1,weight=3)
        self.window.columnconfigure(2,weight=1)

        self.usertype = str(usertype)
        self.name = str(name)

        self.name_and_type = tk.Label(self.window, text=self.name + "[" + self.usertype + "]", borderwidth=1, bg='#333333',fg='#DD2424',font=("Arial",16),pady=20)
        self.name_and_type.pack(side=RIGHT,anchor=NE)

 
        self.name_label = tk.Label(self.window, text=self.name, borderwidth=1, bg='#333333',fg='#DD2424',font=("Arial",16))
        self.name_label.place(relx=0.1,rely=0.2,relwidth=0.4,relheight=0.7)    



        self.window.pack()
        self.window.mainloop()        



if (__name__ == "__main__"):
    main()