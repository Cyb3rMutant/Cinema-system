import tkinter as tk
import tkinter.messagebox
from tkcalendar import DateEntry
from datetime import datetime
from admin import Admin
from manager import Manager
from city_container import cities
from film_container import films
from dbfunc import conn
# Started using inheritence for windows. In the testing stage atm of it
# Started create booking GUI, working on validation


class Main_frame(tk.Frame):
    def __init__(self, parent, controller):
        self.__app = parent
        super().__init__(self.__app)

        self.__user = None

        self.__controller = controller

        self.login()

    def clear_frame(self, frame):
        for widgets in frame.winfo_children():
            widgets.destroy()

    def login(self):
        self.clear_frame(self.__app.body_frame)
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

    def show_info(self, message):
        tk.messagebox.showinfo(
            title="Login Successful", message=message)

    def show_error(self, message):
        tk.messagebox.showerror(title="Error", message=message)

    def logged_in(self, user):
        # Page Title
        self.__user = user
        self.__app.name_label["text"] = f"{self.__user.get_id()}: {self.__user.get_name()}[{self.__user.__class__.__name__}]"
        self.__app.branch_label["text"] = self.__user.get_branch().get_address()

        self.dashboard()

    def dashboard(self):
        self.clear_frame(self.__app.body_frame)
        self.__app.page_label["text"] = "Dashboard"
        # Body
        view_bookings_btn = tk.Button(
            self.__app.body_frame, text="View Bookings", borderwidth=5, command=self.view_bookings, font=("Arial", 16))
        create_booking_btn = tk.Button(
            self.__app.body_frame, text="Create Booking", borderwidth=5, command=self.create_booking, font=("Arial", 16))
        cancel_booking_btn = tk.Button(
            self.__app.body_frame, text="Cancel Booking", borderwidth=5, command=self.cancel_booking, font=("Arial", 16))
        view_film_listings_btn = tk.Button(
            self.__app.body_frame, text="View Film Listings", borderwidth=5, command=self.view_film_listings, font=("Arial", 16))
        add_listing_btn = tk.Button(
            self.__app.body_frame, text="Add Listing", borderwidth=5, command=self.add_listing, font=("Arial", 16))
        remove_listing_btn = tk.Button(
            self.__app.body_frame, text="Remove Listing", borderwidth=5, command=self.remove_listing, font=("Arial", 16))
        update_listing_btn = tk.Button(
            self.__app.body_frame, text="Update Listing", borderwidth=5, command=self.update_listing, font=("Arial", 16))
        generate_report_btn = tk.Button(
            self.__app.body_frame, text="Generate Report", borderwidth=5, command=self.generate_report, font=("Arial", 16))
        add_new_cinema_btn = tk.Button(
            self.__app.body_frame, text="Add New Cinema", borderwidth=5, command=self.add_new_cinema, font=("Arial", 16))

        # Placing Widgets - Adjust Y Value for each user. This is for Manager view at the moment.
        view_bookings_btn.place(x=270, y=100, width=240, height=130)
        create_booking_btn.place(x=520, y=100, width=240, height=130)
        cancel_booking_btn.place(x=770, y=100, width=240, height=130)
        view_film_listings_btn.place(x=270, y=240, width=240, height=130)

        if (isinstance(self.__user, Admin)):
            add_listing_btn.place(x=520, y=240, width=240, height=130)
            remove_listing_btn.place(x=770, y=240, width=240, height=130)
            update_listing_btn.place(x=270, y=380, width=240, height=130)
            generate_report_btn.place(x=520, y=380, width=240, height=130)

            if (isinstance(self.__user, Manager)):
                add_new_cinema_btn.place(x=770, y=380, width=240, height=130)

    def view_bookings(self):
        self.clear_frame(self.__app.body_frame)
        self.__app.page_label["text"] = "View booking"
        if (isinstance(self.__user, Admin)):
            pass
        else:
            self.__controller.get_bookings(self.__user.get_branch())

    def create_booking(self):
        self.clear_frame(self.__app.body_frame)
        # Page Name
        self.__app.page_label["text"] = "Create booking"

        # Body
        # Creating Widgets

        date_today = datetime.now()
        date_label = tk.Label(
            self.__app.body_frame, text="Select Date", fg='#DD2424', font=("Arial", 16))
        date_entry = DateEntry(self.__app.body_frame, width=10, font=(
            "Arial", 15), mindate=date_today)

        select_film_label = tk.Label(
            self.__app.body_frame, text="Select Film", fg='#DD2424', font=("Arial", 16))
        film_list = self.get_film_listings()  # List
        print(film_list)
        options = tk.StringVar(self.__app.body_frame)
        options.set(film_list[0])  # default value option
        select_film_entry = tk.OptionMenu(
            self.__app.body_frame, options, *film_list)

        # Call check availability function, currently is create showing
        check_showings_btn = tk.Button(self.__app.body_frame, text='Check Showings', bg='#DD2424', fg='#000000', font=(
            "Arial", 18), command=self.check_film_date_availability)

        # Placing Widgets
        date_label.place(x=150, y=0)
        date_entry.place(x=350, y=0)
        select_film_label.place(x=150, y=100)
        select_film_entry.place(x=350, y=100)
        check_showings_btn.place(x=250, y=150)

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

    def view_film_listings(self):
        self.clear_frame(self.__app.body_frame)
        self.__app.page_label["text"] = "View film listings"

    def cancel_booking(self):
        self.clear_frame(self.__app.body_frame)
        self.__app.page_label["text"] = "Cancel booking"

    def update_options(self, city):
        menu = self.__cinema_options["menu"]
        menu.delete(0, "end")
        self.__cinema_choice.set(cities[city].get_cinemas()[0])
        for cinema in cities[city].get_cinemas():
            menu.add_command(
                label=cinema, command=lambda value=cinema: self.__cinema_choice.set(value))

        self.clear_frame(self.__screens_box)
        for screen in cities[city].get_cinemas()[0].get_screens():
            l = tk.Checkbutton(
                self.__screens_box, text=screen).pack(sid=tk.BOTTOM)

    def add_listing(self):
        self.clear_frame(self.__app.body_frame)
        self.__app.page_label["text"] = "Add listings"

        self.__city_choice = tk.StringVar()
        self.__city_choice.set(list(cities.get_cities().keys())[0])
        self.__city_options_lable = tk.Label(
            self.__app.body_frame, text="choose city: ")
        self.__city_options = tk.OptionMenu(
            self.__app.body_frame, self.__city_choice, *cities.get_cities().keys(), command=self.update_options)  # , command=self.set_cinema(self.__city_choice.get()))

        self.__cinema_choice = tk.StringVar()
        self.__cinema_choice.set(
            cities[self.__city_choice.get()].get_cinemas()[0])
        self.__cinema_options_label = tk.Label(
            self.__app.body_frame, text="choose cinema: ")
        self.__cinema_options = tk.OptionMenu(
            self.__app.body_frame, self.__cinema_choice, *cities[self.__city_choice.get()].get_cinemas())

        self.__film_choice = tk.StringVar()
        self.__film_choice.set(list(films.get_films().keys())[0])
        self.__film_options_label = tk.Label(
            self.__app.body_frame, text="choose film: ")
        self.__film_options = tk.OptionMenu(
            self.__app.body_frame, self.__film_choice, *films.get_films().keys())

        self.__date_label = tk.Label(
            self.__app.body_frame, text="Select Date: ")
        self.__date_entry = DateEntry(
            self.__app.body_frame, mindate=datetime.now())

        self.__screens_label = tk.Label(
            self.__app.body_frame, text="Select screens: ")
        self.__screens_box = tk.Frame(self.__app.body_frame)
        for screen in cities[self.__city_choice.get()].get_cinemas()[0].get_screens():
            l = tk.Checkbutton(
                self.__screens_box, text=screen).pack()

        self.__city_options_lable.place(x=10, y=10)
        self.__city_options.place(x=100, y=10)
        self.__cinema_options_label.place(x=10, y=70)
        self.__cinema_options.place(x=100, y=70)
        self.__film_options_label.place(x=10, y=140)
        self.__film_options.place(x=100, y=140)
        self.__date_label.place(x=10, y=210)
        self.__date_entry.place(x=100, y=210)
        self.__screens_label.place(x=10, y=280)
        self.__screens_box.place(x=100, y=280)

    def remove_listing(self):
        self.clear_frame(self.__app.body_frame)
        self.__app.page_label["text"] = "Remove listings"

    def update_listing(self):
        self.clear_frame(self.__app.body_frame)
        self.__app.page_label["text"] = "Update listings"

    def generate_report(self):
        self.clear_frame(self.__app.body_frame)
        self.__app.page_label["text"] = "Generate report"

    def add_new_cinema(self):
        self.clear_frame(self.__app.body_frame)
        self.__app.page_label["text"] = "Add new cinema"
