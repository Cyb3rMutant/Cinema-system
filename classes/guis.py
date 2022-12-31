from textwrap import wrap
import tkinter as tk
import tkinter.messagebox
from tkcalendar import DateEntry
import datetime
from admin import Admin
from manager import Manager
from tkinter import ttk
from tkinter.messagebox import showinfo
import re
# Started using inheritence for windows. In the testing stage atm of it
# Started create booking GUI, working on validation


class Main_frame(tk.Frame):
    def __init__(self, parent, controller):
        self.__app = parent
        super().__init__(self.__app)

        self.__user = None

        self.__controller = controller

        self.__back_to_dashboard = tk.Button(self.__app.main_frame, text='go back to dashboard', bg='#DD2424', fg='#000000', font=(
            "Arial", 18), command=lambda: [self.__back_to_dashboard.place_forget(), self.dashboard()])

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
        add_new_show_btn = tk.Button(
            self.__app.body_frame, text="Add new show", borderwidth=5, command=self.add_new_show, font=("Arial", 16))
        add_new_cinema_btn = tk.Button(
            self.__app.body_frame, text="Add New Cinema", borderwidth=5, command=self.add_new_cinema, font=("Arial", 16))
        add_new_city_btn = tk.Button(
            self.__app.body_frame, text="Add New city", borderwidth=5, command=self.add_new_city, font=("Arial", 16))

        # Placing Widgets - Adjust Y Value for each user. This is for Manager view at the moment.
        view_bookings_btn.place(x=270, y=60, width=240, height=130)
        create_booking_btn.place(x=520, y=60, width=240, height=130)
        cancel_booking_btn.place(x=770, y=60, width=240, height=130)
        view_film_listings_btn.place(x=270, y=200, width=240, height=130)

        if (isinstance(self.__user, Admin)):
            add_listing_btn.place(x=520, y=200, width=240, height=130)
            remove_listing_btn.place(x=770, y=200, width=240, height=130)
            update_listing_btn.place(x=270, y=340, width=240, height=130)
            generate_report_btn.place(x=520, y=340, width=240, height=130)
            add_new_show_btn.place(x=770, y=340, width=240, height=130)

            if (isinstance(self.__user, Manager)):
                add_new_cinema_btn.place(x=270, y=480, width=240, height=130)
                add_new_city_btn.place(x=520, y=480, width=240, height=130)

    def view_bookings(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "View bookings"

        self.__btn = tk.Button(
            self.__app.body_frame, text='view', command=lambda: self.view_bookings_treeview())

        self.__tree_frame = tk.Frame(
            self.__app.body_frame, width=700, height=400, bg='gainsboro')
        self.__tree_frame.place(x=150, y=200)

        if (isinstance(self.__user, Admin)):  # if manager or admin
            self.__city_options_label = tk.Label(
                self.__app.body_frame, text="choose city: ").place(x=10, y=30)
            self.__cinema_options_label = tk.Label(
                self.__app.body_frame, text="choose cinema: ").place(x=300, y=30)

            self.__city_choice = tk.StringVar()
            self.__city_choice.set(
                self.__controller.get_city())
            self.__city_options = tk.OptionMenu(self.__app.body_frame, self.__city_choice, *self.__controller.get_cities(),
                                                command=lambda city: (self.__controller.set_city(city), self.update_cinemas()))  # When we change a city, we update its cinemas
            self.__city_options.place(x=100, y=30)

            self.__cinema_choice = tk.StringVar()
            self.__cinema_choice.set(self.__controller.get_cinema())
            self.__cinema_options = tk.OptionMenu(self.__app.body_frame, self.__cinema_choice,
                                                  *self.__controller.get_cinemas(), command=lambda cinema: [self.__controller.set_cinema(cinema)])
            self.__cinema_options.place(x=400, y=30)

            self.__btn.place(x=10, y=90)
        else:
            self.__city_choice = tk.StringVar()
            self.__controller.set_cinema(self.__user.get_branch())
            self.__city_choice.set(
                self.__controller.get_cinema_city())
            # no point having an extra button to view bookings
            self.view_bookings_treeview()

        # optional
        self.search_entry = tk.Entry(self.__app.body_frame)
        self.search_btn = tk.Button(self.__app.body_frame, text='Search',
                                    command=lambda: self.validate_search(self.search_entry.get()))
        self.search_btn.place(x=300, y=550)
        self.search_entry.place(x=100, y=550)

    # optional function

    def validate_search(self, booking_ref):
        try:
            booking_ref = int(booking_ref)
        except:
            self.show_error("string entered")
            return

        if len(str(booking_ref)) != 6:
            self.show_error("Not 6 integers")
            return
        self.view_bookings_treeview(search=True, booking_ref=booking_ref)

    def view_bookings_treeview(self, search=False, booking_ref=000000):
        try:
            self.__login_button.destroy()
        except:
            pass
        self.clear_frame(self.__tree_frame)

        xscrollbar = tk.Scrollbar(self.__tree_frame, orient=tk.HORIZONTAL)
        yscrollbar = tk.Scrollbar(self.__tree_frame, orient=tk.VERTICAL)

        self.__tree_view = ttk.Treeview(
            self.__tree_frame, yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set, selectmode="extended", columns=("booking_ref", "seat_count", "date", "price", "show_id", "seat_type", "cust_email"))
        self.__tree_view.grid(row=0, column=0)
        xscrollbar.configure(command=self.__tree_view.xview)
        yscrollbar.configure(command=self.__tree_view.yview)

        xscrollbar.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        yscrollbar.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        # Tree headings
        self.__tree_view.heading(
            "booking_ref", text="booking_ref", anchor=tk.CENTER)
        self.__tree_view.heading(
            "seat_count", text="seat_count", anchor=tk.CENTER)
        self.__tree_view.heading("date", text="date", anchor=tk.CENTER)
        self.__tree_view.heading("price", text="price", anchor=tk.CENTER)
        self.__tree_view.heading("show_id", text="show_id", anchor=tk.CENTER)
        self.__tree_view.heading(
            "seat_type", text="seat_type", anchor=tk.CENTER)
        self.__tree_view.heading(
            "cust_email", text="cust_email", anchor=tk.CENTER)

        # Null column to prevent overflow of large size column (disablet o test)
        self.__tree_view.column("#0", width=0,  stretch=tk.NO)
        self.__tree_view.column("booking_ref", anchor=tk.CENTER, width=140)
        self.__tree_view.column("seat_count", anchor=tk.CENTER, width=140)
        self.__tree_view.column("date", anchor=tk.CENTER, width=140)
        self.__tree_view.column("price", anchor=tk.CENTER, width=140)
        self.__tree_view.column("show_id", anchor=tk.CENTER, width=140)
        self.__tree_view.column("seat_type", anchor=tk.CENTER, width=140)
        self.__tree_view.column("cust_email", anchor=tk.CENTER, width=140)

        if search == False:  # City selection search
            print(booking_ref)
            for data in self.__controller.get_all_bookings_as_list():
                self.__tree_view.insert('', tk.END, values=data)
        # optional
        if search == True:
            self.__tree_view.insert(
                '', tk.END, values=self.__controller.get_booking(booking_ref).as_list())

    def update_films_and_shows_based_on_date(self, btn_text, btn_command):
        self.remove_create_stuff()
        try:  # Only got this cus it doesnt work with booking staff causes error crash. KEEP it tho, you can remove comments
            # Debug -> Change city to anything but birmingham and date only. U will see it prints birminghams address when it shouldnt be. the if statement prevents this

            # Added this because when we load create_booking -> change city to Bristol -> change date to any date -> the above debug will print birminghams cinema info -> change date to birmingham listing date -> film and show options will update with birminghams and not bristols
            # And cinema_choice will still be "choose cinema" whilst it prints birminghams listings in city_choice bristol
            if str(self.__cinema_choice.get()) == "choose cinema":
                print('error: choose cinema is selected, wont update film')
                return
        except:
            pass
        # Main. All above is just format

        # Command doesnt work if we change date then change film, only works first time loaded thats why i hardcoded destroy widget in the update_film_and_show function.
        listing = self.__controller.get_listing()
        if not listing:
            return
        self.__film_choice = tk.StringVar()
        self.__film_choice.set(listing)
        self.__film_options = tk.OptionMenu(
            self.__app.body_frame, self.__film_choice, *self.__controller.get_listings(), command=lambda listing: (self.__controller.set_listing(listing), self.update_shows()))

        # Shows
        self.__show_choice = tk.StringVar()
        self.__show_choice.set(self.__controller.get_show())
        self.__show_options = tk.OptionMenu(
            self.__app.body_frame, self.__show_choice, *self.__controller.get_shows(), command=lambda show: self.__controller.set_show(show))

        self.__btn = tk.Button(
            self.__app.body_frame, text=btn_text, command=btn_command)

        self.__film_options.place(x=100, y=150)
        self.__show_options.place(x=100, y=200)
        self.__btn.place(x=50, y=350)

    def create_booking(self):

        # When we change cinema option value --> update_films_and_shows_based_on_date. (Because we fill in the rest of paramaeters using city chosen)
        # When we change date value --> update_films_and_shows_based_on_date (We fetch all listings showing at a specific day at the cinema)
        # When we change a film value -->  update_shows (We fetch all showing times for the listing)
        # When we chang ea show --> Nothing

        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Create booking"

        if (isinstance(self.__user, Admin)):

            self.__city_options_label = tk.Label(
                self.__app.body_frame, text="choose city: ").place(x=10, y=30)
            self.__cinema_options_label = tk.Label(
                self.__app.body_frame, text="choose cinema: ").place(x=300, y=30)

            self.__city_choice = tk.StringVar()
            self.__city_choice.set(
                self.__controller.get_city())
            self.__city_options = tk.OptionMenu(self.__app.body_frame, self.__city_choice, *self.__controller.get_cities(),
                                                command=lambda city: (self.__controller.set_city(city), self.remove_create_stuff(),  self.update_cinemas(self.update_films_and_shows_based_on_date("Book now", lambda: self.__controller.add_booking(str(self.__seat_type_btn.get()), int(self.__num_of_ticket_choice.get()))))))  # When we change a city, we update its cinemas
            self.__city_options.place(x=100, y=30)

            self.__cinema_choice = tk.StringVar()
            self.__cinema_choice.set(self.__controller.get_cinema())
            self.__cinema_options = tk.OptionMenu(self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cinemas(), command=lambda cinema: [self.__controller.set_cinema(
                cinema), self.update_films_and_shows_based_on_date("Book now", lambda: self.__controller.add_booking(str(self.__seat_type_btn.get()), int(self.__num_of_ticket_choice.get())))])
            self.__cinema_options.place(x=400, y=30)

        else:
            self.__city_choice = tk.StringVar()
            self.__controller.set_cinema(self.__user.get_branch())
            self.__city_choice.set(
                self.__controller.get_cinema_city())

        # Standard labels
        self.__date_label = tk.Label(
            self.__app.body_frame, text="Select Date").place(x=10, y=90)
        self.__select_film_label = tk.Label(
            self.__app.body_frame, text="Select Film").place(x=10, y=150)
        self.__select_show_label = tk.Label(
            self.__app.body_frame, text="Select Show").place(x=10, y=210)
        self.__select_seat_type = tk.Label(
            self.__app.body_frame, text="Select Ticket Type").place(x=10, y=270)
        self.__select_num_of_seats = tk.Label(
            self.__app.body_frame, text="Select # of Tickets").place(x=10, y=330)

        # Date
        self.__date_today = datetime.date.today()
        self.__selected_date = tk.StringVar()
        self.__date_entry = DateEntry(self.__app.body_frame, date_pattern='y-mm-dd',
                                      mindate=datetime.date.today(), textvariable=self.__selected_date)
        self.__selected_date.trace(
            'w', lambda *unused: self.update_films_and_shows_based_on_date("Book now", lambda: self.__controller.add_booking(str(self.__seat_type_btn.get()), int(self.__num_of_ticket_choice.get()))))
        self.__controller.set_date(str(datetime.date.today()))

        self.__seat_type_btn = tk.StringVar()
        self.__lower_hall = tk.Radiobutton(self.__app.body_frame, text="lower", value="lower",
                                           variable=self.__seat_type_btn, tristatevalue=0)
        self.__upper_hall = tk.Radiobutton(self.__app.body_frame, text="upper", value="upper",
                                           variable=self.__seat_type_btn, tristatevalue=0)
        self.__vip_hall = tk.Radiobutton(self.__app.body_frame, text="vip", value="vip",
                                         variable=self.__seat_type_btn, tristatevalue=0)

        self.__num_of_ticket_choice = tk.IntVar()
        self.__num_of_ticket_choice.set(1)
        self.__num_of_ticket_options = tk.Spinbox(
            self.__app.body_frame, textvariable=self.__num_of_ticket_choice, from_=1, to=5, width=5)

        self.__date_entry.place(x=100, y=90)
        self.__lower_hall.place(x=120, y=270)
        self.__upper_hall.place(x=240, y=270)
        self.__vip_hall.place(x=360, y=270)
        self.__num_of_ticket_options.place(x=120, y=330)

        # Films - Gets all listing titles (film titles) based on the date selected. Only here for first loadup of page, as after the first load whenever date is changed it goes to function

        # Command doesnt work if we change date then change film, only works first time loaded thats why i hardcoded destroy widget in the update_film_and_show function.
        listing = self.__controller.get_listing()
        if not listing:
            return
        self.__film_choice = tk.StringVar()
        self.__film_choice.set(listing)
        self.__film_options = tk.OptionMenu(
            self.__app.body_frame, self.__film_choice, *self.__controller.get_listings(), command=lambda listing: (self.__controller.set_listing(listing), self.update_shows()))

        # Shows
        self.__show_choice = tk.StringVar()
        self.__show_choice.set(self.__controller.get_show())
        self.__show_options = tk.OptionMenu(
            self.__app.body_frame, self.__show_choice, *self.__controller.get_shows(), command=lambda show: self.__controller.set_show(show))

        # Ticket type & Number of tickets entry
        self.__btn = tk.Button(
            self.__app.body_frame, text='Book now', command=lambda: self.__controller.add_booking(str(self.__seat_type_btn.get()), int(self.__num_of_ticket_choice.get())))

        # Placing interactive widgets
        self.__film_options.place(x=100, y=150)
        self.__show_options.place(x=100, y=200)
        self.__btn.place(x=50, y=350)

    def view_film_listings(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "View film listings"

    def display_bookings_treeview(self):
        try:
            self.__login_button.destroy()
        except:
            pass
        self.clear_frame(self.__tree_frame)

        xscrollbar = tk.Scrollbar(self.__tree_frame, orient=tk.HORIZONTAL)
        yscrollbar = tk.Scrollbar(self.__tree_frame, orient=tk.VERTICAL)

        self.__tree_view = ttk.Treeview(
            self.__tree_frame, yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set, selectmode="extended", columns=("booking_ref", "seat_count", "date", "price", "show_id", "seat_type", "cust_email"))
        self.__tree_view.grid(row=0, column=0)
        xscrollbar.configure(command=self.__tree_view.xview)
        yscrollbar.configure(command=self.__tree_view.yview)

        xscrollbar.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        yscrollbar.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        # Tree headings
        self.__tree_view.heading(
            "booking_ref", text="booking_ref", anchor=tk.CENTER)
        self.__tree_view.heading(
            "seat_count", text="seat_count", anchor=tk.CENTER)
        self.__tree_view.heading("date", text="date", anchor=tk.CENTER)
        self.__tree_view.heading("price", text="price", anchor=tk.CENTER)
        self.__tree_view.heading("show_id", text="show_id", anchor=tk.CENTER)
        self.__tree_view.heading(
            "seat_type", text="seat_type", anchor=tk.CENTER)
        self.__tree_view.heading(
            "cust_email", text="cust_email", anchor=tk.CENTER)

        # Null column to prevent overflow of large size column (disablet o test)
        self.__tree_view.column("#0", width=0,  stretch=tk.NO)
        self.__tree_view.column("booking_ref", anchor=tk.CENTER, width=140)
        self.__tree_view.column("seat_count", anchor=tk.CENTER, width=140)
        self.__tree_view.column("date", anchor=tk.CENTER, width=140)
        self.__tree_view.column("price", anchor=tk.CENTER, width=140)
        self.__tree_view.column("show_id", anchor=tk.CENTER, width=140)
        self.__tree_view.column("seat_type", anchor=tk.CENTER, width=140)
        self.__tree_view.column("cust_email", anchor=tk.CENTER, width=140)

        self.__tree_view.bind('<<TreeviewSelect>>',
                              lambda unused: self.item_selected())

        # generate sample data
        # add data to the treeview
        for data in self.__controller.get_bookings_as_list():
            self.__tree_view.insert('', tk.END, values=data)

    # Event listener, anytime a record is clicked itll print it
    def item_selected(self):
        record = self.__tree_view.item(
            self.__tree_view.selection()[0])["values"]

        self.__login_button = tk.Button(self.__app.body_frame, text='cancel booking', bg='#DD2424', fg='#000000', font=(
            "Arial", 18), command=lambda: (self.__controller.cancel_booking(str(record[0])), self.display_bookings_treeview()))
        self.__login_button.place(x=212, y=560)

    def cancel_booking(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Cancel booking"

        if (isinstance(self.__user, Admin)):
            self.__city_options_label = tk.Label(
                self.__app.body_frame, text="choose city: ").place(x=10, y=30)
            self.__cinema_options_label = tk.Label(
                self.__app.body_frame, text="choose cinema: ").place(x=300, y=30)

            self.__city_choice = tk.StringVar()
            self.__city_choice.set(
                self.__controller.get_city())
            self.__city_options = tk.OptionMenu(self.__app.body_frame, self.__city_choice, *self.__controller.get_cities(),
                                                command=lambda city: (self.__controller.set_city(city), self.update_cinemas(self.update_films_and_shows_based_on_date("refresh", self.display_bookings_treeview))))  # When we change a city, we update its cinemas
            self.__city_options.place(x=100, y=30)

            self.__cinema_choice = tk.StringVar()
            self.__cinema_choice.set(self.__controller.get_cinema())
            self.__cinema_options = tk.OptionMenu(self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cinemas(), command=lambda cinema: [
                                                  self.__controller.set_cinema(cinema), self.update_films_and_shows_based_on_date("refresh", self.display_bookings_treeview)])
            self.__cinema_options.place(x=400, y=30)

        else:
            self.__city_choice = tk.StringVar()
            self.__controller.set_cinema(self.__user.get_branch())
            self.__city_choice.set(
                self.__controller.get_cinema_city())

        # Standard labels
        self.__date_label = tk.Label(
            self.__app.body_frame, text="Select Date").place(x=10, y=90)
        self.__select_film_label = tk.Label(
            self.__app.body_frame, text="Select Film").place(x=10, y=150)
        self.__select_show_label = tk.Label(
            self.__app.body_frame, text="Select Show").place(x=10, y=210)
        self.__select_seat_type = tk.Label(
            self.__app.body_frame, text="Select Ticket Type").place(x=10, y=270)
        self.__select_num_of_seats = tk.Label(
            self.__app.body_frame, text="Select # of Tickets").place(x=10, y=330)

        # Date
        self.__date_today = datetime.date.today()
        self.__selected_date = tk.StringVar()
        self.__date_entry = DateEntry(self.__app.body_frame, date_pattern='y-mm-dd',
                                      mindate=datetime.date.today(), textvariable=self.__selected_date)
        self.__selected_date.trace(
            'w', lambda *unused: self.update_films_and_shows_based_on_date("refresh", self.display_bookings_treeview))
        self.__controller.set_date(str(datetime.date.today()))

        self.__date_entry.place(x=100, y=90)

        # uncomment all the treeview code to see the frame bg
        self.__tree_frame = tk.Frame(
            self.__app.body_frame, width=700, height=400, bg='gainsboro')
        self.__tree_frame.place(x=300, y=200)

        # Films - Gets all listing titles (film titles) based on the date selected. Only here for first loadup of page, as after the first load whenever date is changed it goes to function

        # Command doesnt work if we change date then change film, only works first time loaded thats why i hardcoded destroy widget in the update_film_and_show function.
        listing = self.__controller.get_listing()
        if not listing:
            return
        self.__film_choice = tk.StringVar()
        self.__film_choice.set(listing)
        self.__film_options = tk.OptionMenu(
            self.__app.body_frame, self.__film_choice, *self.__controller.get_listings(), command=lambda listing: (self.__controller.set_listing(listing), self.update_shows()))

        # Shows
        self.__show_choice = tk.StringVar()
        self.__show_choice.set(self.__controller.get_show())
        self.__show_options = tk.OptionMenu(
            self.__app.body_frame, self.__show_choice, *self.__controller.get_shows(), command=lambda show: self.__controller.set_show(show))

        # Ticket type & Number of tickets entry
        self.__btn = tk.Button(
            self.__app.body_frame, text='refresh', command=self.display_bookings_treeview)

        # Placing interactive widgets
        self.__film_options.place(x=100, y=150)
        self.__show_options.place(x=100, y=210)
        self.__btn.place(x=50, y=390)

    def add_listing(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Add listings"

        # city
        self.__city_choice = tk.StringVar()
        self.__city_choice.set(self.__controller.get_city())
        self.__city_options_lable = tk.Label(
            self.__app.body_frame, text="choose city: ")
        self.__city_options = tk.OptionMenu(
            self.__app.body_frame, self.__city_choice, *self.__controller.get_cities(), command=lambda city: (self.__controller.set_city(city), self.update_cinemas()))  # , command=self.__controller.set_cinema(self.__city_choice.get()))

        # cinema
        self.__cinema_choice = tk.StringVar()
        self.__cinema_choice.set(self.__controller.get_cinema())
        self.__cinema_options_label = tk.Label(
            self.__app.body_frame, text="choose cinema: ")
        self.__cinema_options = tk.OptionMenu(
            self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cinemas(), command=lambda cinema: (self.__controller.set_cinema(cinema)))

        # film
        self.__film_choice = tk.StringVar()
        self.__film_choice.set(list(self.__controller.get_films().keys())[0])
        self.__film_options_label = tk.Label(
            self.__app.body_frame, text="choose film: ")
        self.__film_options = tk.OptionMenu(
            self.__app.body_frame, self.__film_choice, *self.__controller.get_films().keys())

        # date
        self.__date_label = tk.Label(
            self.__app.body_frame, text="Select Date: ")
        self.__selected_date = tk.StringVar()
        self.__date_entry = DateEntry(self.__app.body_frame, date_pattern='y-mm-dd',
                                      mindate=datetime.date.today(), textvariable=self.__selected_date)
        self.__selected_date.trace(
            'w', lambda *unused: self.__controller.set_date(self.__selected_date.get()))
        self.__controller.set_date(str(datetime.date.today()))

        self.__login_button = tk.Button(self.__app.body_frame, text='add listing', bg='#DD2424', fg='#000000', font=(
            "Arial", 18), command=lambda: self.__controller.add_listing(self.__film_choice.get()))
        self.__login_button.place(x=612, y=460)

        self.__city_options_lable.place(x=10, y=30)
        self.__city_options.place(x=100, y=30)
        self.__cinema_options_label.place(x=300, y=30)
        self.__cinema_options.place(x=400, y=30)
        self.__film_options_label.place(x=10, y=90)
        self.__film_options.place(x=100, y=90)
        self.__date_label.place(x=10, y=150)
        self.__date_entry.place(x=100, y=150)

    def remove_listing(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Remove listings"

        # city
        self.__city_choice = tk.StringVar()
        self.__city_choice.set(self.__controller.get_city())
        self.__city_options_lable = tk.Label(
            self.__app.body_frame, text="choose city: ")
        self.__city_options = tk.OptionMenu(self.__app.body_frame, self.__city_choice, *self.__controller.get_cities(
        ), command=lambda city: (self.__controller.set_city(city), self.update_cinemas(lambda cinema: self.update_listings_many())))

        # cinema
        self.__cinema_choice = tk.StringVar()
        self.__cinema_choice.set(self.__controller.get_cinema())
        self.__cinema_options_label = tk.Label(
            self.__app.body_frame, text="choose cinema: ")
        self.__cinema_options = tk.OptionMenu(
            self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cinemas(), command=lambda cinema: (self.__controller.set_cinema(cinema), self.update_listings_many()))

        # date
        self.__date_label = tk.Label(
            self.__app.body_frame, text="Select Date: ")
        self.__selected_date = tk.StringVar()
        self.__date_entry = DateEntry(self.__app.body_frame, date_pattern='y-mm-dd',
                                      mindate=datetime.date.today(), textvariable=self.__selected_date)
        self.__selected_date.trace(
            'w', lambda *unused: (self.__controller.set_date(self.__selected_date.get()), self.update_listings_one()))
        self.__controller.set_date(str(datetime.date.today()))

        # listings
        self.__listings_label = tk.Label(
            self.__app.body_frame, text="Select listings: ")
        self.__listings_box = tk.Frame(self.__app.body_frame)
        self.__items = []
        idx = 0
        for listing in self.__controller.get_listings():
            self.__items.append(tk.IntVar())
            tk.Checkbutton(
                self.__listings_box, variable=self.__items[idx], text=listing, onvalue=listing.get_listing_id(), offvalue=None).pack()
            idx += 1

        self.__login_button = tk.Button(self.__app.body_frame, text='remove listing', bg='#DD2424', fg='#000000', font=(
            "Arial", 18), command=lambda: self.__controller.remove_listing([int(id.get()) for id in self.__items if id != None]))
        self.__login_button.place(x=612, y=460)

        self.__city_options_lable.place(x=10, y=30)
        self.__city_options.place(x=100, y=30)
        self.__cinema_options_label.place(x=300, y=30)
        self.__cinema_options.place(x=400, y=30)
        self.__date_label.place(x=10, y=90)
        self.__date_entry.place(x=100, y=90)
        self.__listings_label.place(x=10, y=150)
        self.__listings_box.place(x=100, y=150)

    def update_listing(self):
        print("Update listing page opened")  # debugging
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Update listings"

        # city
        self.__city_choice = tk.StringVar()
        self.__city_choice.set(self.__controller.get_city())
        self.__city_options_lable = tk.Label(
            self.__app.body_frame, text="choose city: ")
        self.__city_options = tk.OptionMenu(self.__app.body_frame, self.__city_choice, *self.__controller.get_cities(
        ), command=lambda city: (self.__controller.set_city(city), self.update_cinemas(lambda cinema: self.update_listings_one())))

        # cinema
        self.__cinema_choice = tk.StringVar()
        self.__cinema_choice.set(self.__controller.get_cinema())
        self.__cinema_options_label = tk.Label(
            self.__app.body_frame, text="choose cinema: ")
        self.__cinema_options = tk.OptionMenu(
            self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cinemas(), command=lambda cinema: (self.__controller.set_cinema(cinema), self.update_listings_one()))

        # date
        self.__date_label = tk.Label(
            self.__app.body_frame, text="Select Date: ")
        self.__selected_date = tk.StringVar()
        self.__date_entry = DateEntry(self.__app.body_frame, date_pattern='y-mm-dd',
                                      mindate=datetime.date.today(), textvariable=self.__selected_date)
        self.__selected_date.trace(
            'w', lambda *unused: (self.__controller.set_date(self.__selected_date.get()), self.update_listings_one()))
        self.__controller.set_date(str(datetime.date.today()))

        # listings  (need to change this so they can only pick one)
        self.__listings_label = tk.Label(
            self.__app.body_frame, text="select date:")
        self.__listing_choice = tk.StringVar()
        self.__listing_choice.set(self.__controller.get_listing())
        self.__listing_options = tk.OptionMenu(
            self.__app.body_frame, self.__listing_choice, *self.__controller.get_listings(), command=lambda listing: self.__controller.set_listing(listing))

        self.__login_button = tk.Button(self.__app.body_frame, text='select listing', bg='#DD2424', fg='#000000', font=("Arial", 18),
                                        command=lambda: self.update_listing_details(self.get_id(self.__listing_choice.get()), self.__city_choice.get(), self.get_id(self.__cinema_choice.get())))

        self.__login_button.place(x=612, y=460)

        self.__city_options_lable.place(x=10, y=30)
        self.__city_options.place(x=100, y=30)
        self.__cinema_options_label.place(x=300, y=30)
        self.__cinema_options.place(x=400, y=30)
        self.__date_label.place(x=10, y=90)
        self.__date_entry.place(x=100, y=90)
        self.__listings_label.place(x=10, y=150)
        self.__listing_options.place(x=100, y=150)

    # after they have selected a listing in (update listing) this lets them actually change the listings details

    def update_listing_details(self, listing_id, city, cinema):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Update listings"

        # get cinema, film and date from the paramter listing id
        # already passing through city as its easier
        listing = self.__controller.get_listing(listing_id)
        self.__original_film = listing.get_film()
        self.__original_date = listing.get_date()

        # all inputs are pre filled with the current values of the listing they want to update

        # display current listing details
        self.__orignal_listing_label = tk.Label(
            self.__app.body_frame, text=f'Original Listing Details:\n City: {city}\n Cinema ID: {cinema}\n Film: {self.__original_film}\n Date: {self.__original_date}', font=("Arial", 12))

        # select film
        self.__film_choice = tk.StringVar()
        self.__film_choice.set(self.__original_film)
        self.__film_options_label = tk.Label(
            self.__app.body_frame, text="choose film: ")
        self.__film_options = tk.OptionMenu(
            self.__app.body_frame, self.__film_choice, *self.__controller.get_films().keys())

        # select date
        self.__date_label = tk.Label(
            self.__app.body_frame, text="Select Date: ")
        self.__selected_date = tk.StringVar()
        self.__date_entry = DateEntry(self.__app.body_frame, date_pattern='y-mm-dd',
                                      mindate=datetime.date.today(), textvariable=self.__selected_date)
        self.__selected_date.trace(
            'w', lambda *unused: (self.__controller.set_date(self.__selected_date.get()), self.update_listings_one()))
        self.__controller.set_date(str(datetime.date.today()))

        # update listing button
        self.__login_button = tk.Button(self.__app.body_frame, text='update listing', bg='#DD2424', fg='#000000', font=(
            "Arial", 18), command=lambda: self.__controller.update_listing(self.__film_choice.get()))

        # place buttons
        self.__login_button.place(x=612, y=460)

        self.__film_options_label.place(x=10, y=30)
        self.__film_options.place(x=100, y=30)
        self.__date_label.place(x=10, y=90)
        self.__date_entry.place(x=100, y=90)
        self.__orignal_listing_label.place(x=500, y=30)

    def generate_report(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Generate report"

    def add_new_show(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "add new show"

        # city
        self.__city_choice = tk.StringVar()
        self.__city_choice.set(self.__controller.get_city())
        self.__city_options_lable = tk.Label(
            self.__app.body_frame, text="choose city: ")
        self.__city_options = tk.OptionMenu(
            self.__app.body_frame, self.__city_choice, *self.__controller.get_cities(), command=lambda city: (self.__controller.set_city(city), self.update_cinemas(lambda cinema: self.update_listings_one())))  # , command=self.__controller.set_cinema(self.__city_choice.get()))

        # cinema
        self.__cinema_choice = tk.StringVar()
        self.__cinema_choice.set(self.__controller.get_cinema())
        self.__cinema_options_label = tk.Label(
            self.__app.body_frame, text="choose cinema: ")
        self.__cinema_options = tk.OptionMenu(
            self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cinemas(), command=lambda cinema: (self.__controller.set_cinema(cinema), self.update_listings_one()))

        # date
        self.__date_label = tk.Label(
            self.__app.body_frame, text="Select Date: ")
        self.__selected_date = tk.StringVar()
        self.__date_entry = DateEntry(self.__app.body_frame, date_pattern='y-mm-dd',
                                      mindate=datetime.date.today(), textvariable=self.__selected_date)
        self.__selected_date.trace(
            'w', lambda *unused: (self.__controller.set_date(self.__selected_date.get()), self.update_listings_one()))
        self.__controller.set_date(str(datetime.date.today()))

        # listings  (need to change this so they can only pick one)

        self.__listings_label = tk.Label(
            self.__app.body_frame, text="select date:")
        self.__listing_choice = tk.StringVar()
        self.__listing_choice.set(self.__controller.get_listing())
        self.__listing_options = tk.OptionMenu(
            self.__app.body_frame, self.__listing_choice, *self.__controller.get_listings(), command=lambda listing: self.__controller.set_listing(listing))
        self.__listing_options.place(x=100, y=150)

        self.__time_label = tk.Label(
            self.__app.body_frame, text="select time: ")
        self.__hours_choice = tk.IntVar()
        self.__hours_choice.set(8)
        self.__hours_options = tk.Spinbox(
            self.__app.body_frame, textvariable=self.__hours_choice, from_=8, to=23, width=5)
        self.__minutes_choice = tk.IntVar()
        self.__minutes_choice.set(0)
        self.__minutes_options = tk.Spinbox(
            self.__app.body_frame, textvariable=self.__minutes_choice, from_=0, to=59, width=5)

        self.__login_button = tk.Button(self.__app.body_frame, text='select listing', bg='#DD2424', fg='#000000', font=("Arial", 18),
                                        command=lambda: self.__controller.add_show(datetime.time(self.__hours_choice.get(), self.__minutes_choice.get(), 0)))

        self.__login_button.place(x=612, y=460)

        self.__city_options_lable.place(x=10, y=30)
        self.__city_options.place(x=100, y=30)
        self.__cinema_options_label.place(x=300, y=30)
        self.__cinema_options.place(x=400, y=30)
        self.__date_label.place(x=10, y=90)
        self.__date_entry.place(x=100, y=90)
        self.__listings_label.place(x=10, y=150)
        self.__time_label.place(x=10, y=270)
        self.__hours_options.place(x=100, y=270)
        self.__minutes_options.place(x=150, y=270)

    def add_new_cinema(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Add new cinema"

        # city
        self.__city_choice = tk.StringVar()
        self.__city_choice.set(self.__controller.get_city())
        self.__city_options_lable = tk.Label(
            self.__app.body_frame, text="choose city: ")
        self.__city_options = tk.OptionMenu(
            self.__app.body_frame, self.__city_choice, *self.__controller.get_cities(), command=lambda city: self.__controller.set_city(city))  # , command=self.__controller.set_cinema(self.__city_choice.get()))

        self.__cinema_address_lable = tk.Label(
            self.__app.body_frame, text="Cinema address: ")
        self.__cinema_address = tk.Entry(self.__app.body_frame)

        self.__number_of_screens_lable = tk.Label(
            self.__app.body_frame, text="Number of screens: ")
        self.__number_of_screens = tk.Entry(self.__app.body_frame)

        self.__login_button = tk.Button(self.__app.body_frame, text='Add cinema', bg='#DD2424', fg='#000000', font=(
            "Arial", 18), command=lambda: self.__controller.add_cinema(self.__cinema_address.get(), int(self.__number_of_screens.get())))
        self.__login_button.place(x=612, y=460)

        self.__city_options_lable.place(x=10, y=30)
        self.__city_options.place(x=130, y=30)
        self.__cinema_address_lable.place(x=10, y=90)
        self.__cinema_address.place(x=130, y=90)
        self.__number_of_screens_lable.place(x=10, y=150)
        self.__number_of_screens.place(x=130, y=150)

    def add_new_city(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Add new city"

        self.__city_name_lable = tk.Label(
            self.__app.body_frame, text="City name: ")
        self.__city_name = tk.Entry(self.__app.body_frame)

        self.__city_morning_price_lable = tk.Label(
            self.__app.body_frame, text="City morning price: ")
        self.__city_morning_price = tk.Entry(self.__app.body_frame)

        self.__city_afternoon_price_lable = tk.Label(
            self.__app.body_frame, text="City afternoon price: ")
        self.__city_afternoon_price = tk.Entry(self.__app.body_frame)

        self.__city_evening_price_lable = tk.Label(
            self.__app.body_frame, text="City evening price: ")
        self.__city_evening_price = tk.Entry(self.__app.body_frame)

        self.__login_button = tk.Button(self.__app.body_frame, text='Add city', bg='#DD2424', fg='#000000', font=("Arial", 18), command=lambda: self.__controller.add_city(
            self.__city_name.get(), self.__city_morning_price.get(), self.__city_afternoon_price.get(), self.__city_evening_price.get()))
        self.__login_button.place(x=612, y=460)

        self.__city_name_lable.place(x=10, y=30)
        self.__city_name.place(x=130, y=30)
        self.__city_morning_price_lable.place(x=10, y=90)
        self.__city_morning_price.place(x=130, y=90)
        self.__city_afternoon_price_lable.place(x=10, y=150)
        self.__city_afternoon_price.place(x=130, y=150)
        self.__city_evening_price_lable.place(x=10, y=210)
        self.__city_evening_price.place(x=130, y=210)

    def get_id(self, string):
        print(string, type(string))
        return int(re.search(r'\d+', string).group())

    def remove_create_stuff(self):

        try:
            self.__film_options.destroy()
            self.__show_options.destroy()
            self.__btn.destroy()
        except:
            pass

    def update_cinemas(self, func=lambda: None):
        self.__cinema_choice.set(self.__controller.get_cinema())
        self.__cinema_options.destroy()
        self.__cinema_options = tk.OptionMenu(
            self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cinemas(), command=lambda cinema: (self.__controller.set_cinema(cinema), func()))
        self.__cinema_options.place(x=400, y=30)

    def update_listings_many(self):
        self.clear_frame(self.__listings_box)
        self.__items = []
        idx = 0
        for listing in self.__controller.get_listings():
            self.__items.append(tk.IntVar())
            tk.Checkbutton(
                self.__listings_box, variable=self.__items[idx], text=listing, onvalue=listing.get_listing_id(), offvalue=None).pack(sid=tk.BOTTOM)
            idx += 1

    def update_listings_one(self):
        # self.clear_frame(self.__listings_box)
        # self.__item = tk.IntVar()
        # for listing in self.__controller.get_listings():
        #     if str(listing.get_date()) != self.__selected_date.get():
        #         continue

        #     tk.Checkbutton(
        #         self.__listings_box, variable=self.__item, text=listing, onvalue=listing.get_listing_id(), offvalue=None).pack(sid=tk.BOTTOM)

        self.__listings_label = tk.Label(
            self.__app.body_frame, text="select date:")
        self.__listing_choice = tk.StringVar()
        self.__listing_choice.set(self.__controller.get_listing())
        self.__listing_options = tk.OptionMenu(
            self.__app.body_frame, self.__listing_choice, *self.__controller.get_listings(), command=lambda listing: self.__controller.set_listing(listing))
        self.__listing_options.place(x=100, y=150)

    def update_shows(self):
        self.__show_options.destroy()
        self.__show_choice = tk.StringVar()
        # Instead of "choose show". If we choose city, cinema, date, film AND show is still equal to "choose show", we can still book which it shouldnt. This prevents this by automatically updating shows to the times instead of it.
        self.__show_choice.set(self.__controller.get_show())
        self.__show_options = tk.OptionMenu(self.__app.body_frame, self.__show_choice,
                                            *self.__controller.get_shows(), command=lambda show: [self.__controller.set_show(show)])
        self.__show_options.place(x=100, y=200)
