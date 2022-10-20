import tkinter
from tkinter import messagebox
import mysql.connector
from passlib.hash import sha256_crypt


def get_connection():
    conn = mysql.connector.connect(host='localhost',
                                   port='3306',
                                   user='root',
                                   password='',
                                   database='tkinter')
    return conn

window = tkinter.Tk()
window.title("Login")
window.geometry("700x600")
window.configure(bg='#333333')

login_frame = tkinter.Frame(window)
login_frame.configure(bg='#333333')



def login_verify():
    username = username_entry.get()
    password = password_entry.get()

    conn = get_connection()
    dbcursor = conn.cursor()
    dbcursor.execute("SELECT password_hash, usertype \
                            FROM users WHERE username = %s;", (username,))
    
    data = dbcursor.fetchone()
    if dbcursor.rowcount < 1:
        messagebox.showerror(title="Error",message="User doesnt exist.")

    else:
        if sha256_crypt.verify(password, str(data[0])):
            messagebox.showinfo(title="Login Successful",message="You have successfully logged in.")
        else:
            messagebox.showerror(title="Error",message="Incorrect username or password.")




    

    # if username == "roh" and password == "roh":
    #     messagebox.showinfo(title="Login Successful",message="You have successfully logged in.")
    # else:
    #     messagebox.showerror(title="Error",message="Invalid login.")




# Create widgets
login_label = tkinter.Label(login_frame, text='Login', borderwidth=1, bg='#333333',fg='#DD2424',font=("Arial",32))
username_label = tkinter.Label(login_frame, text='Username', bg='#333333', fg='#FFFFFF',font=("Arial",18))
username_entry = tkinter.Entry(login_frame, font=("Arial", 18))
password_label = tkinter.Label(login_frame, text='Password', bg='#333333', fg='#FFFFFF',font=("Arial",18))
password_entry = tkinter.Entry(login_frame, show='*', font=("Arial", 18))
login_button = tkinter.Button(login_frame, text='Login', bg='#DD2424', fg='#000000',font=("Arial",18), command=login_verify)


#Placing widgets
login_label.grid(row=0, column=1, columnspan=2,pady=45)
username_label.grid(row=1, column=1)
username_entry.grid(row=2, column=1, pady=15)
password_label.grid(row=3, column=1)
password_entry.grid(row=4, column=1, pady=15)
login_button.grid(row=5, column=1, columnspan=2,pady=35)


login_frame.pack()
window.mainloop()



#IGNORE THIS
# Placing widgets on the screen
# login_label.grid(row=0,column=0,columnspan=2)
# username_label.grid(row=1,column=0)
# username_entry.grid(row=1,column=1)
# password_label.grid(row=2,column=0)
# password_entry.grid(row=2,column=1)
# login_button.grid(row=3,column=0, columnspan=2)
