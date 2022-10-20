import tkinter as tk
from tkinter import messagebox
from tkinter import *
from turtle import right
from urllib.request import DataHandler
import mysql.connector
from passlib.hash import sha256_crypt

#This one is a work in progress. Im trying to place stuff around the window

def get_connection():
    conn = mysql.connector.connect(host='localhost',
                                   port='3306',
                                   user='root',
                                   password='avatar',
                                   database='tkinter')
    return conn

def main():
    root = tk.Tk()
    app = DashboardTest(root)


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
        self.app = DashboardTest(self.root)
        #We can have here if usertype is... then direct it to that class dashboard. We can use inheritence for the classes or hardcode it



class DashboardTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background="gainsboro")

        self.MainFrame = Frame(self.root, bd=10, width=1350, height=800, bg='gainsboro',relief=RIDGE)
        self.MainFrame.grid()
        self.HeaderFrame = Frame(self.MainFrame, bd=10, width=1330, height=100, bg='gainsboro',relief=RIDGE)
        self.HeaderFrame.grid()    
        self.BodyFrame= Frame(self.MainFrame, bd=10, width=1320, height=670, bg="gainsboro",relief=RIDGE)
        self.BodyFrame.grid()


        self.name_label = tk.Label(self.HeaderFrame, text="roh", borderwidth=1, bg='#333333',fg='#DD2424',font=("Arial",16))
        self.name_label.place(x=0,y=0,width=443,height=100)

        self.name_label2 = tk.Label(self.HeaderFrame, text="roh2", borderwidth=1, bg='#333333',fg='#DD2424',font=("Arial",16))
        self.name_label2.place(x=443,y=0,width=443,height=100)

        self.name_label3 = tk.Label(self.HeaderFrame, text="roh3", borderwidth=1, bg='#333333',fg='#DD2424',font=("Arial",16))
        self.name_label3.place(x=886,y=0,width=443,height=100)

        self.root.mainloop()









if (__name__ == "__main__"):
    main()