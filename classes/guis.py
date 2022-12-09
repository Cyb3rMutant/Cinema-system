import tkinter as tk
import tkinter.messagebox
from tkcalendar import DateEntry
from datetime import datetime

from dbfunc import conn
# Started using inheritence for windows. In the testing stage atm of it
# Started create booking GUI, working on validation


class Main_frame(tk.Frame):
    def __init__(self, parent, controller):
        self.__app = parent
        self.__controller = controller
        self.login()

    def clear_frame(self):
        for widgets in self.__app.body_frame.winfo_children():
            widgets.destroy()

    def login(self):
        super().__init__(self.__app)
        # Create widgets
        self.__app.page_label["text"] = "Login"
        self.__username_label = tk.Label(
            self.__app.body_frame, text='Username', font=("Arial", 32))
        self.__username_label.place(x=562, y=60)
        self.__username_entry = tk.Entry(
            self.__app.body_frame, font=("Arial", 32))
        self.__username_entry.place(x=412, y=130)
        self.__password_label = tk.Label(
            self.__app.body_frame, text='Password', font=("Arial", 32))
        self.__password_label.place(x=562, y=260)
        self.__password_entry = tk.Entry(
            self.__app.body_frame, show='*', font=("Arial", 32))
        self.__password_entry.place(x=412, y=330)
        self.__login_button = tk.Button(
            self.__app.body_frame, text='Login', bg='#DD2424', fg='#000000', font=("Arial", 18), command=lambda: self.__controller.login(
                self.__username_entry.get(), self.__password_entry.get()))
        self.__login_button.place(x=612, y=460)

    def loggedin(self, data):
        tk.messagebox.showinfo(
            title="Login Successful", message="You have successfully logged in.")
        self.clear_frame()

        self.create_dashboard(
            data["USER_NAME"], data["USER_TYPE"], data["CINEMA_ID"])

    def show_error(self, message):
        tk.messagebox.showerror(title="Error", message=message)

    def create_dashboard(self, name, usertype, branch):
        self.dashboard(name, usertype, branch)

    def dashboard(self, name, usertype, branch):
        # Page Title
        self.__app.page_label["text"] = "Dashboard"
        self.__app.name_label["text"] = f"{name} [{usertype}]"
        self.__app.branch_label["text"] = branch
        # Body
        self.create_booking_btn = tk.Button(
            self.__app.body_frame, text="Create Booking", borderwidth=1, command=self.create_booking_gui)
        self.view_bookings_btn = tk.Button(
            self.__app.body_frame, text="View Bookings", borderwidth=1)
        self.view_film_listings_btn = tk.Button(
            self.__app.body_frame, text="View Film Listings", borderwidth=1)
        self.cancel_booking_btn = tk.Button(
            self.__app.body_frame, text="Cancel Booking", borderwidth=1)

        self.add_listing_btn = tk.Button(
            self.__app.body_frame, text="Add Listing", borderwidth=1)
        self.remove_listing_btn = tk.Button(
            self.__app.body_frame, text="Remove Listing", borderwidth=1)
        self.update_listing_btn = tk.Button(
            self.__app.body_frame, text="Update Listing", borderwidth=1)
        self.generate_report_btn = tk.Button(
            self.__app.body_frame, text="Generate Report", borderwidth=1)

        self.add_new_cinema_btn = tk.Button(
            self.__app.body_frame, text="Add New Cinema", borderwidth=1)
        self.add_listing_master_btn = tk.Button(
            self.__app.body_frame, text="Add Listing to Cinema", borderwidth=1)

        # Placing Widgets - Adjust Y Value for each user. This is for Manager view at the moment.
        self.create_booking_btn.place(x=170, y=150, width=240, height=100)
        self.view_bookings_btn.place(x=420, y=150, width=240, height=100)
        self.view_film_listings_btn.place(x=670, y=150, width=240, height=100)
        self.cancel_booking_btn.place(x=920, y=150, width=240, height=100)

        self.add_listing_btn.place(x=170, y=250, width=240, height=100)
        self.remove_listing_btn.place(x=420, y=250, width=240, height=100)
        self.update_listing_btn.place(x=670, y=250, width=240, height=100)
        self.generate_report_btn.place(x=920, y=250, width=240, height=100)

        self.add_new_cinema_btn.place(x=170, y=350, width=240, height=100)
        self.add_listing_master_btn.place(x=420, y=350, width=240, height=100)

    def create_booking_gui(self):
        self.booking()

    def booking(self):

        # Page Name
        self.__app.page_label["text"] = "Dashboard"

        # Body
        # Creating Widgets

        self.date_today = datetime.now()
        self.date_label = tk.Label(
            self.__app.body_frame, text="Select Date", fg='#DD2424', font=("Arial", 16))
        self.date_entry = DateEntry(self.__app.body_frame, width=10, font=(
            "Arial", 15), mindate=self.date_today)

        self.select_film_label = tk.Label(
            self.__app.body_frame, text="Select Film", fg='#DD2424', font=("Arial", 16))
        self.film_list = self.get_film_listings()  # List
        print(self.film_list)
        self.options = tk.StringVar(self.__app.body_frame)
        self.options.set(self.film_list[0])  # default value option
        self.select_film_entry = tk.OptionMenu(
            self.__app.body_frame, self.options, *self.film_list)

        # Call check availability function, currently is create showing
        self.check_showings_btn = tk.Button(self.__app.body_frame, text='Check Showings', bg='#DD2424', fg='#000000', font=(
            "Arial", 18), command=self.check_film_date_availability)

        # Placing Widgets
        self.date_label.place(x=150, y=0)
        self.date_entry.place(x=350, y=0)
        self.select_film_label.place(x=150, y=100)
        self.select_film_entry.place(x=350, y=100)
        self.check_showings_btn.place(x=250, y=150)

    def get_film_listings(self):
        self.film_list = conn.select("SELECT film_name FROM films")
        return self.film_list

    def check_film_date_availability(self):

        self.date = self.date_entry.get()  # Type = string
        # Still need to strip this. Gets the value of optionsmenu entered when button is pressed. Type = string
        self.film = self.options.get()

    # If valid then  delete labels and create_showing_options()

        # Destroy the labels so we can replace the screen with showing information
        self.date_label.destroy()
        self.date_entry.destroy()
        self.select_film_label.destroy()
        self.select_film_entry.destroy()
        self.check_showings_btn.destroy()

        self.create_showing_options(self.date, self.film)

    def create_showing_options(self, date, film):

        self.date = date  # Type = string
        self.film = film  # Type = string

        self.date_label = tk.Label(self.__app.body_frame, text=self.date, fg='#000000', font=(
            "Arial", 18)).place(x=150, y=100)
        self.film_title_label = tk.Label(
            self.__app.body_frame, text=self.film, fg='#000000').place(x=350, y=100)

        self.select_showings_label = tk.Label(
            self.__app.body_frame, text="Select Showing", fg='#DD2424', font=("Arial", 16)).place(x=150, y=200)
        self.showings_list = self.get_film_listings()  # List
        self.options = tk.StringVar(self.__app.body_frame)
        self.options.set(self.showings_list[0])  # default value option
        self.select_showing_entry = tk.OptionMenu(
            self.__app.body_frame, self.options, *self.showings_list).place(x=350, y=200)

        print(self.film)
        print(self.date)

    def get_showings_list(self):
        self.film_list = conn.select("SELECT FILM_TITLE FROM FILMS")

        return self.film_list
