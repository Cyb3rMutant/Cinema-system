import tkinter as tk
from tkinter import messagebox
from tkinter import *
from turtle import right
from urllib.request import DataHandler
import mysql.connector
from numpy import logical_and
from passlib.hash import sha256_crypt

#Started using inheritence for windows. In the testing stage atm of it

def get_connection():
    conn = mysql.connector.connect(host='localhost',
                                   port='3306',
                                   user='root',
                                   password='avatar',
                                   database='tkinter')
    return conn

def main():
    root = tk.Tk()
    app = Dashboard(root)


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
        self.app = Dashboard(self.root)


class BaseWindow():
    def __init__(self, window):
        self.window = window
        self.window.title("Dashboard")
        self.window.geometry("1350x800+0+0")
        self.window.configure(background="gainsboro")
        self.MainFrame = Frame(self.window, bd=10, width=1350, height=800, bg='gainsboro',relief=RIDGE)
        self.MainFrame.grid()
        self.HeaderFrame = Frame(self.MainFrame, bd=10, width=1330, height=100, bg='gainsboro',relief=RIDGE)
        self.HeaderFrame.config(bg='#333333')
        self.HeaderFrame.grid()          
        self.BodyFrame= Frame(self.MainFrame, bd=10, width=1330, height=670, bg="gainsboro",relief=RIDGE)
        self.BodyFrame.grid()
  

        #Header
        #Page Name is different for each class. We place them on the class itself. (Top Left Title)
        self.title_label = tk.Label(self.HeaderFrame, text="Horizon Cinemas", borderwidth=1, bg='#333333',fg='#DD2424',font=("Arial",16))
        self.title_label.place(x=443,y=5,width=443,height=70) 
        self.branch_label = tk.Label(self.HeaderFrame, text="Bristol City Centre", borderwidth=1, bg='#333333',fg='#DD2424',font=("Arial",16))
        self.branch_label.place(x=890,y=5,width=400) #Higher width overlaps border. Had to make it smaller and adjust with X     
        self.name_label = tk.Label(self.HeaderFrame, text="James Jenkins [Booking Staff]", borderwidth=1, bg='#333333',fg='#DD2424',font=("Arial",16))
        self.name_label.place(x=890,y=40,width=400)
        

class Dashboard(BaseWindow):
    def __init__(self, window):
        super().__init__(window)
        
        #Page Title
        self.page_label = tk.Label(self.HeaderFrame, text="Dashboard", borderwidth=1, bg='#333333',fg='#DD2424',font=("Arial",16))
        self.page_label.place(x=0,y=5,width=443,height=70) #443 = width/3

        #Body
        self.create_booking_btn = tk.Button(self.BodyFrame, text="Create Booking", borderwidth=1, command=self.create_booking_gui)
        self.view_bookings_btn = tk.Button(self.BodyFrame, text="View Bookings", borderwidth=1)
        self.view_film_listings_btn = tk.Button(self.BodyFrame, text="View Film Listings", borderwidth=1)
        self.cancel_booking_btn = tk.Button(self.BodyFrame, text="Cancel Booking", borderwidth=1)
        
        self.add_listing_btn = tk.Button(self.BodyFrame, text="Add Listing", borderwidth=1)
        self.remove_listing_btn = tk.Button(self.BodyFrame, text="Remove Listing", borderwidth=1)
        self.update_listing_btn = tk.Button(self.BodyFrame, text="Update Listing", borderwidth=1)
        self.generate_report_btn = tk.Button(self.BodyFrame, text="Generate Report", borderwidth=1) 
        
        self.add_new_cinema_btn = tk.Button(self.BodyFrame, text="Add New Cinema", borderwidth=1)
        self.add_listing_master_btn = tk.Button(self.BodyFrame, text="Add Listing to Cinema", borderwidth=1)        


        #Placing Widgets - Adjust Y Value for each user. This is for Manager view at the moment.
        self.create_booking_btn.place(x=170,y=150,width=240,height=100)
        self.view_bookings_btn.place(x=420,y=150,width=240,height=100)
        self.view_film_listings_btn.place(x=670,y=150,width=240,height=100)
        self.cancel_booking_btn.place(x=920,y=150,width=240,height=100)

        self.add_listing_btn.place(x=170,y=250,width=240,height=100)
        self.remove_listing_btn.place(x=420,y=250,width=240,height=100)
        self.update_listing_btn.place(x=670,y=250,width=240,height=100)
        self.generate_report_btn.place(x=920,y=250,width=240,height=100)

        self.add_new_cinema_btn.place(x=170,y=350,width=240,height=100)
        self.add_listing_master_btn.place(x=420,y=350,width=240,height=100)



        self.window.mainloop()

    def create_booking_gui(self):
        self.root = tk.Tk()
        self.window.destroy()
        self.app = BookingGUI(self.root)


class BookingGUI(BaseWindow):
    def __init__(self, window):
        super().__init__(window)
        
        #Page Name
        self.page_label = tk.Label(self.HeaderFrame, text="Create Booking", borderwidth=1, bg='#333333',fg='#DD2424',font=("Arial",16))
        self.page_label.place(x=0,y=5,width=443,height=70) #443 = width/3


if (__name__ == "__main__"):
    main()