"""
Authors:
    Rohaan Aslam (21017718)
    Benjamin Hussey (21022768)
    Yazeed Abu-Hummous (21014295)
Date: 08/01/2023
Module: Advanced Software Development 22/23
"""
import tkinter as tk
from tkcalendar import DateEntry
import datetime
from admin import Admin
from manager import Manager
from tkinter import ttk
import re



class Main_frame(tk.Frame):
    def __init__(self, parent, controller):
        self.__app = parent
        super().__init__(self.__app)

        self.__user = None

        self.__controller = controller

        self.__back_to_dashboard = tk.Button(self.__app.main_frame, text='go back to dashboard', bg='#DD2424', fg='#000000', font=(
            "Arial", 18), command=lambda: [self.__back_to_dashboard.place_forget(), self.dashboard()])

        self.__log_out = tk.Button(
            self.__app.header_frame, text="logout", command=lambda: (self.__log_out.place_forget(), self.__controller.logout()))

        self.login()

    def clear_frame(self, frame):
        for widgets in frame.winfo_children():
            widgets.destroy()

    def login(self):
        self.__user = None
        self.__app.name_label["text"] = ""
        self.__app.branch_label["text"] = ""
        self.clear_frame(self.__app.body_frame)
        # Create widgets
        self.__app.page_label["text"] = "Login"
        self.__user_id_label = tk.Label(
            self.__app.body_frame, text='User_id', font=("Arial", 32))
        self.__user_id_label.place(x=562, y=60)
        self.__user_id_entry = tk.Entry(
            self.__app.body_frame, font=("Arial", 32))
        self.__user_id_entry.place(x=412, y=130)
        self.__password_label = tk.Label(
            self.__app.body_frame, text='Password', font=("Arial", 32))
        self.__password_label.place(x=562, y=260)
        self.__password_entry = tk.Entry(
            self.__app.body_frame, show='*', font=("Arial", 32))
        self.__password_entry.place(x=412, y=330)
        self.__login_button = tk.Button(
            self.__app.body_frame, text='Login', bg='#DD2424', fg='#000000', font=("Arial", 18), command=lambda: self.__controller.login(
                self.__user_id_entry.get(), self.__password_entry.get()))
        self.__login_button.place(x=612, y=460)

    def show_info(self, message):
        tk.messagebox.showinfo(
            title="Success", message=message)

    def show_error(self, message):
        tk.messagebox.showerror(title="Error", message=message)

    def askquestion(self, message):
        msg_box = tk.messagebox.askquestion(
            "Returning Customer", message, icon='question')
        if msg_box == 'yes':
            self.__controller.update_customer(self.__customer_name.get(
            ), self.__customer_email.get(), self.__customer_phone.get(), self.__card_number.get())

    def logged_in(self, user):
        # Page Title
        self.__log_out.place(x=0, y=0)
        self.__user = user
        self.__app.name_label["text"] = self.__user
        self.__app.branch_label["text"] = self.__user.get_branch().get_address()

        self.dashboard()

    def dashboard(self):
        self.__controller.clear_data()
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place_forget()

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
        add_new_film_btn = tk.Button(
            self.__app.body_frame, text="Add New film", borderwidth=5, command=self.add_new_film, font=("Arial", 16))
        add_new_user_btn = tk.Button(
            self.__app.body_frame, text="Add New user", borderwidth=5, command=self.add_new_user, font=("Arial", 16))

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
                add_new_film_btn.place(x=520, y=480, width=240, height=130)
                add_new_user_btn.place(x=770, y=480, width=240, height=130)

    def view_bookings(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "View bookings"

        self.__view_btn = tk.Button(
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
                                                command=lambda city: (self.__controller.set_city(city), self.update_cinemas(lambda cinema: (self.__controller.set_cinema(cinema)))))
            self.__city_options.place(x=100, y=30)

            self.__cinema_choice = tk.StringVar()
            self.__cinema_choice.set(self.__controller.get_cinema())
            self.__cinema_options = tk.OptionMenu(self.__app.body_frame, self.__cinema_choice,
                                                  *self.__controller.get_cinemas(), command=lambda cinema: [self.__controller.set_cinema(cinema)])
            self.__cinema_options.place(x=400, y=30)

            self.__view_btn.place(x=10, y=90)
        else:
            self.__city_choice = tk.StringVar()
            self.__controller.set_cinema(self.__user.get_branch())
            self.__city_choice.set(
                self.__controller.get_cinema_city())
            self.__cinema_choice = tk.StringVar()
            self.__cinema_choice.set(self.__controller.get_cinema(
                self.__user.get_branch().get_cinema_id()))
            self.__view_btn = tk.Button(
                self.__app.body_frame, text='reset', command=lambda: self.view_bookings_treeview())
            self.__view_btn.place(x=10, y=90)

            self.view_bookings_treeview()

        # Search works fine.
        self.search_entry = tk.Entry(self.__app.body_frame)
        self.search_btn = tk.Button(self.__app.body_frame, text='Search',
                                    command=lambda: self.validate_search(self.search_entry.get(), "view"))

        self.search_btn.place(x=300, y=550)
        self.search_entry.place(x=100, y=550)

    def validate_search(self, booking_ref, page):
        try:
            booking_ref = int(booking_ref)
        except:
            self.show_error("string entered")
        if len(str(booking_ref)) != 6:
            self.show_error("Not 6 integers")
            return
        if page == "view":
            self.view_bookings_treeview(search=True, booking_ref=booking_ref)
        if page == "cancel":
            self.display_bookings_treeview(search=True, booking_ref=booking_ref)

    def view_bookings_treeview(self, search=False, booking_ref=000000):
        try:
            self.__login_button.destroy()
        except:
            pass
        self.clear_frame(self.__tree_frame)

        xscrollbar = tk.Scrollbar(self.__tree_frame, orient=tk.HORIZONTAL)
        yscrollbar = tk.Scrollbar(self.__tree_frame, orient=tk.VERTICAL)

        self.__tree_view = ttk.Treeview(
            self.__tree_frame, yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set, selectmode="extended", columns=("booking_ref", "seat_count", "date", "price", "show_id", "seat_type"))
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

        # Null column to prevent overflow of large size column (disablet o test)
        self.__tree_view.column("#0", width=0,  stretch=tk.NO)
        self.__tree_view.column("booking_ref", anchor=tk.CENTER, width=140)
        self.__tree_view.column("seat_count", anchor=tk.CENTER, width=140)
        self.__tree_view.column("date", anchor=tk.CENTER, width=140)
        self.__tree_view.column("price", anchor=tk.CENTER, width=140)
        self.__tree_view.column("show_id", anchor=tk.CENTER, width=140)
        self.__tree_view.column("seat_type", anchor=tk.CENTER, width=140)

        if search == False:  # City selection search
            print(booking_ref)
            for data in self.__controller.get_all_bookings_as_list():
                self.__tree_view.insert('', tk.END, values=data)
        # optional
        if search == True:
            self.__tree_view.insert(
                '', tk.END, values=self.__controller.get_booking(booking_ref).as_list())

    def create_booking(self):

        # When we change cinema option value --> update_listings_and_shows_based_on_date. (Because we fill in the rest of paramaeters using city chosen)
        # When we change date value --> update_listings_and_shows_based_on_date (We fetch all listings showing at a specific day at the cinema)
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
                                                command=lambda city: (self.__controller.set_city(city), self.remove_create_stuff(),  self.update_cinemas(lambda cinema: (self.__controller.set_cinema(cinema), self.update_listings_and_shows_based_on_date("Book now", lambda: self.__controller.validate_booking(str(self.__seat_type_btn.get()), int(self.__num_of_ticket_choice.get()))))), self.update_listings_and_shows_based_on_date("Book now", lambda: self.__controller.validate_booking(str(self.__seat_type_btn.get()), int(self.__num_of_ticket_choice.get())))))

            self.__city_options.place(x=100, y=30)

            self.__cinema_choice = tk.StringVar()
            self.__cinema_choice.set(self.__controller.get_cinema())
            self.__cinema_options = tk.OptionMenu(self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cinemas(), command=lambda cinema: [self.__controller.set_cinema(
                cinema), self.update_listings_and_shows_based_on_date("Book now", lambda: self.__controller.validate_booking(str(self.__seat_type_btn.get()), int(self.__num_of_ticket_choice.get())))])
            self.__cinema_options.place(x=400, y=30)

        else:
            self.__city_choice = tk.StringVar()
            self.__controller.set_cinema(self.__user.get_branch())
            self.__city_choice.set(
                self.__controller.get_cinema_city())
            self.__cinema_choice = tk.StringVar()
            self.__cinema_choice.set(self.__controller.get_cinema(
                self.__user.get_branch().get_cinema_id()))

        # Standard labels
        self.__date_label = tk.Label(
            self.__app.body_frame, text="Select Date").place(x=10, y=90)
        self.__select_film_label = tk.Label(
            self.__app.body_frame, text="Select listing").place(x=10, y=150)
        self.__select_show_label = tk.Label(
            self.__app.body_frame, text="Select Show").place(x=10, y=210)
        self.__select_seat_type = tk.Label(
            self.__app.body_frame, text="Select Ticket Type").place(x=10, y=270)
        self.__select_num_of_seats = tk.Label(
            self.__app.body_frame, text="Select # of Tickets").place(x=10, y=330)

        # Date
        self.__selected_date = tk.StringVar()
        self.__date_entry = DateEntry(self.__app.body_frame, date_pattern='y-mm-dd',
                                      mindate=datetime.date.today(), textvariable=self.__selected_date)
        self.__selected_date.trace(
            'w', lambda *unused: (self.__controller.set_date(self.__selected_date.get()), self.update_listings_and_shows_based_on_date("Book now", lambda: self.__controller.validate_booking(str(self.__seat_type_btn.get()), int(self.__num_of_ticket_choice.get())))))
        self.__controller.set_date(str(self.__selected_date.get()))

        self.__seat_type_btn = tk.StringVar()
        self.__lower_hall = tk.Radiobutton(self.__app.body_frame, text="lower", value="lower",
                                           variable=self.__seat_type_btn, tristatevalue=0)
        self.__upper_hall = tk.Radiobutton(self.__app.body_frame, text="upper", value="upper",
                                           variable=self.__seat_type_btn, tristatevalue=0)
        self.__vip_hall = tk.Radiobutton(self.__app.body_frame, text="vip", value="vip",
                                         variable=self.__seat_type_btn, tristatevalue=0)

        self.__num_of_ticket_choice = tk.IntVar()
        self.__num_of_ticket_choice.set(1)
        self.__num_of_ticket_options = tk.OptionMenu(
            self.__app.body_frame, self.__num_of_ticket_choice, *range(1, 6))

        self.__date_entry.place(x=100, y=90)
        self.__lower_hall.place(x=120, y=270)
        self.__upper_hall.place(x=240, y=270)
        self.__vip_hall.place(x=360, y=270)
        self.__num_of_ticket_options.place(x=120, y=330)

        # Films - Gets all listing titles (film titles) based on the date selected. Only here for first loadup of page, as after the first load whenever date is changed it goes to function

        # Command doesnt work if we change date then change film, only works first time loaded thats why i hardcoded destroy widget in the update_film_and_show function.
        self.__film_choice = tk.StringVar()
        self.__film_choice.set(self.__controller.get_listing())
        self.__listing_options = tk.OptionMenu(
            self.__app.body_frame, self.__film_choice, *self.__controller.get_listings(), command=lambda listing: (self.__controller.set_listing(listing), self.update_shows()))

        # Shows
        self.__show_choice = tk.StringVar()
        self.__show_choice.set(self.__controller.get_show())
        self.__show_options = tk.OptionMenu(
            self.__app.body_frame, self.__show_choice, *self.__controller.get_shows(), command=lambda show: self.__controller.set_show(show))

        # Ticket type & Number of tickets entry
        self.__btn = tk.Button(
            self.__app.body_frame, text='Book now', command=lambda: self.__controller.validate_booking(str(self.__seat_type_btn.get()), int(self.__num_of_ticket_choice.get())))

        # Placing interactive widgets
        self.__listing_options.place(x=100, y=150)
        self.__show_options.place(x=100, y=200)
        self.__btn.place(x=50, y=380)

    def book_now(self, info):
        self.clear_frame(self.__app.body_frame)

        self.__booking_info = tk.Label(
            self.__app.body_frame, text=info).place(x=500, y=50)

        self.__customer_name_lable = tk.Label(
            self.__app.body_frame, text="customer name: ")
        self.__customer_name = tk.Entry(self.__app.body_frame)

        self.__customer_email_lable = tk.Label(
            self.__app.body_frame, text="customer email: ")
        self.__customer_email = tk.Entry(self.__app.body_frame)

        self.__customer_phone_lable = tk.Label(
            self.__app.body_frame, text="customer phone: ")
        self.__customer_phone = tk.Entry(self.__app.body_frame)

        self.__name_on_card_lable = tk.Label(
            self.__app.body_frame, text="name on card: ")
        self.__name_on_card = tk.Entry(self.__app.body_frame)

        self.__card_number_lable = tk.Label(
            self.__app.body_frame, text="card number: ")
        self.__card_number = tk.Entry(self.__app.body_frame)

        self.__cvv_lable = tk.Label(
            self.__app.body_frame, text="cvv: ")
        self.__cvv = tk.Entry(self.__app.body_frame)

        self.__expiry_date_lable = tk.Label(
            self.__app.body_frame, text="expiry date: ")
        self.__expiry_date = tk.Entry(self.__app.body_frame)

        self.__login_button = tk.Button(self.__app.body_frame, text='Book', bg='#DD2424', fg='#000000', font=("Arial", 18), command=lambda: self.__controller.add_booking(
            self.__customer_name.get(), self.__customer_email.get(), self.__customer_phone.get(), self.__name_on_card.get(), self.__card_number.get(), self.__cvv.get(), self.__expiry_date.get()))
        self.__login_button.place(x=612, y=460)

        self.__customer_name_lable.place(x=10, y=30)
        self.__customer_name.place(x=130, y=30)
        self.__customer_email_lable.place(x=10, y=90)
        self.__customer_email.place(x=130, y=90)
        self.__customer_phone_lable.place(x=10, y=150)
        self.__customer_phone.place(x=130, y=150)
        self.__name_on_card_lable.place(x=10, y=210)
        self.__name_on_card.place(x=130, y=210)
        self.__card_number_lable.place(x=10, y=270)
        self.__card_number.place(x=130, y=270)
        self.__cvv_lable.place(x=10, y=330)
        self.__cvv.place(x=130, y=330)
        self.__expiry_date_lable.place(x=10, y=390)
        self.__expiry_date.place(x=130, y=390)

    def view_film_listings(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "View film listings"

        self.__film_label = tk.Label(
            self.__app.body_frame, text="")
        self.__film_label.place(x=200, y=400)
        self.__view_btn = tk.Button(
            self.__app.body_frame, text='view', command=lambda: self.view_film_listings_treeview())

        self.__tree_frame = tk.Frame(
            self.__app.body_frame, width=700, height=400, bg='gainsboro')
        self.__tree_frame.place(x=150, y=150)
        if (isinstance(self.__user, Admin)):  # if manager or admin
            self.__city_options_label = tk.Label(
                self.__app.body_frame, text="choose city: ").place(x=10, y=30)
            self.__cinema_options_label = tk.Label(
                self.__app.body_frame, text="choose cinema: ").place(x=300, y=30)

            self.__city_choice = tk.StringVar()
            self.__city_choice.set(
                self.__controller.get_city())
            self.__city_options = tk.OptionMenu(self.__app.body_frame, self.__city_choice, *self.__controller.get_cities(),
                                                command=lambda city: (self.__controller.set_city(city), self.update_cinemas(lambda cinema: (self.__controller.set_cinema(cinema)))))
            self.__city_options.place(x=100, y=30)

            self.__cinema_choice = tk.StringVar()
            self.__cinema_choice.set(self.__controller.get_cinema())
            self.__cinema_options = tk.OptionMenu(self.__app.body_frame, self.__cinema_choice,
                                                  *self.__controller.get_cinemas(), command=lambda cinema: [self.__controller.set_cinema(cinema)])
            self.__cinema_options.place(x=400, y=30)

            self.__view_btn.place(x=10, y=90)
        else:
            self.__city_choice = tk.StringVar()
            self.__controller.set_cinema(self.__user.get_branch())
            self.__city_choice.set(
                self.__controller.get_cinema_city())
            self.__cinema_choice = tk.StringVar()
            self.__cinema_choice.set(self.__controller.get_cinema(
                self.__user.get_branch().get_cinema_id()))

            self.view_film_listings_treeview()

    def view_film_listings_treeview(self):
        try:
            self.__login_button.destroy()
        except:
            pass
        self.clear_frame(self.__tree_frame)

        xscrollbar = tk.Scrollbar(self.__tree_frame, orient=tk.HORIZONTAL)
        yscrollbar = tk.Scrollbar(self.__tree_frame, orient=tk.VERTICAL)

        self.__tree_view = ttk.Treeview(
            self.__tree_frame, yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set, selectmode="extended", columns=("listing_id", "listing_date", "film_title"))
        self.__tree_view.grid(row=0, column=0)
        xscrollbar.configure(command=self.__tree_view.xview)
        yscrollbar.configure(command=self.__tree_view.yview)

        xscrollbar.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        yscrollbar.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        # Tree headings
        self.__tree_view.heading(
            "listing_id", text="listing_id", anchor=tk.CENTER)
        self.__tree_view.heading(
            "listing_date", text="listing_date", anchor=tk.CENTER)
        self.__tree_view.heading(
            "film_title", text="film_title", anchor=tk.CENTER)

        # Null column to prevent overflow of large size column (disablet o test)
        self.__tree_view.column("#0", width=0,  stretch=tk.NO)
        self.__tree_view.column("listing_id", anchor=tk.CENTER, width=310)
        self.__tree_view.column("listing_date", anchor=tk.CENTER, width=310)
        self.__tree_view.column("film_title", anchor=tk.CENTER, width=310)

        self.__tree_view.bind('<<TreeviewSelect>>',
                              lambda unused: (self.item_selected_listings(), self.print_film()))

        # Going to insert view listings data here
        for data in self.__controller.get_cinema_listings_as_list():
            self.__tree_view.insert('', tk.END, values=data)

    # On select- print its show times for the listing selected as a label or any other way

    def item_selected_listings(self):
        record = self.__tree_view.item(self.__tree_view.selection()[0])[
            "values"]  # Selected record
        show_data = self.__controller.get_shows_for_listing(record[0])

        self.__show_tree_frame = tk.Frame(
            self.__app.body_frame, width=300, height=300, bg='gainsboro')
        self.__show_tree_frame.place(x=900, y=400)

        self.__show_tree_view = ttk.Treeview(
            self.__show_tree_frame, selectmode="extended", columns=("show_id", "show_time", "screen_id"))
        self.__show_tree_view.grid(row=0, column=0)

        self.__show_tree_view.heading(
            "show_id", text="show_id", anchor=tk.CENTER)
        self.__show_tree_view.heading(
            "show_time", text="show_time", anchor=tk.CENTER)
        self.__show_tree_view.heading(
            "screen_id", text="screen_id", anchor=tk.CENTER)

        self.__show_tree_view.column("#0", width=0,  stretch=tk.NO)
        self.__show_tree_view.column("show_id", anchor=tk.CENTER, width=100)
        self.__show_tree_view.column("show_time", anchor=tk.CENTER, width=100)
        self.__show_tree_view.column("screen_id", anchor=tk.CENTER, width=100)

        for data in show_data:
            self.__show_tree_view.insert('', tk.END, values=data)

    def display_bookings_treeview(self, search=False, booking_ref=000000):
        try:
            self.__login_button.destroy()
        except:
            pass
        self.clear_frame(self.__tree_frame)

        xscrollbar = tk.Scrollbar(self.__tree_frame, orient=tk.HORIZONTAL)
        yscrollbar = tk.Scrollbar(self.__tree_frame, orient=tk.VERTICAL)

        self.__tree_view = ttk.Treeview(
            self.__tree_frame, yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set, selectmode="extended", columns=("booking_ref", "seat_count", "date", "price", "show_id", "seat_type"))
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

        # Null column to prevent overflow of large size column (disablet o test)
        self.__tree_view.column("#0", width=0,  stretch=tk.NO)
        self.__tree_view.column("booking_ref", anchor=tk.CENTER, width=140)
        self.__tree_view.column("seat_count", anchor=tk.CENTER, width=140)
        self.__tree_view.column("date", anchor=tk.CENTER, width=140)
        self.__tree_view.column("price", anchor=tk.CENTER, width=140)
        self.__tree_view.column("show_id", anchor=tk.CENTER, width=140)
        self.__tree_view.column("seat_type", anchor=tk.CENTER, width=140)

        self.__tree_view.bind('<<TreeviewSelect>>',
                              lambda unused: self.item_selected())

        if search == True:
            self.__tree_view.insert(
                '', tk.END, values=self.__controller.get_booking(booking_ref).as_list())

        if search == False:
            try:
                for data in self.__controller.get_bookings_as_list():
                    self.__tree_view.insert('', tk.END, values=data)
            except:
                self.show_error("No Listings Airing.")
    # Event listener, anytime a record is clicked itll print it

    def item_selected(self):
        record = self.__tree_view.item(
            self.__tree_view.selection()[0])["values"]

        self.__login_button = tk.Button(self.__app.body_frame, text='cancel booking', bg='#DD2424', fg='#000000', font=(
            "Arial", 18), command=lambda: (self.__controller.cancel_booking(str(record[0]), self.__customer_email.get(), None, self.__card_number.get(), None, None), self.display_bookings_treeview()))
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
                                                command=lambda city: (self.__controller.set_city(city), self.remove_create_stuff(),  self.update_cinemas(lambda cinema: (self.__controller.set_cinema(cinema), self.update_listings_and_shows_based_on_date("refresh", self.display_bookings_treeview))), self.update_listings_and_shows_based_on_date("refresh", self.display_bookings_treeview)))
            self.__city_options.place(x=100, y=30)

            self.__cinema_choice = tk.StringVar()
            self.__cinema_choice.set(self.__controller.get_cinema())
            self.__cinema_options = tk.OptionMenu(self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cinemas(), command=lambda cinema: [
                                                  self.__controller.set_cinema(cinema), self.update_listings_and_shows_based_on_date("refresh", self.display_bookings_treeview)])
            self.__cinema_options.place(x=400, y=30)

        else:
            self.__city_choice = tk.StringVar()
            self.__controller.set_cinema(self.__user.get_branch())
            self.__city_choice.set(
                self.__controller.get_cinema_city())
            self.__cinema_choice = tk.StringVar()
            self.__cinema_choice.set(self.__controller.get_cinema(
                self.__user.get_branch().get_cinema_id()))

        self.search_entry = tk.Entry(self.__app.body_frame)
        self.search_entry.place(x=100, y=450)

        # Standard labels
        self.__date_label = tk.Label(
            self.__app.body_frame, text="Select Date").place(x=10, y=90)
        self.__select_film_label = tk.Label(
            self.__app.body_frame, text="Select listing").place(x=10, y=150)
        self.__select_show_label = tk.Label(
            self.__app.body_frame, text="Select Show").place(x=10, y=210)

        # Date
        self.__selected_date = tk.StringVar()
        self.__date_entry = DateEntry(self.__app.body_frame, date_pattern='y-mm-dd',
                                      mindate=datetime.date.today(), textvariable=self.__selected_date)
        self.__selected_date.trace(
            'w', lambda *unused: (self.__controller.set_date(self.__selected_date.get()), self.update_listings_and_shows_based_on_date("refresh", self.display_bookings_treeview)))
        self.__controller.set_date(str(datetime.date.today()))

        self.__date_entry.place(x=100, y=90)

        # uncomment all the treeview code to see the frame bg
        self.__tree_frame = tk.Frame(
            self.__app.body_frame, width=700, height=400, bg='gainsboro')
        self.__tree_frame.place(x=300, y=200)

        # Needs to be placed here, just wont work if we have up there with search entry
        self.search_btn = tk.Button(self.__app.body_frame, text='Search',
                                    command=lambda: self.validate_search(self.search_entry.get(), "cancel"))

        self.search_btn.place(x=300, y=450)

        # Ticket type & Number of tickets entry
        self.__btn = tk.Button(
            self.__app.body_frame, text='refresh', command=self.display_bookings_treeview)

        self.__customer_email_lable = tk.Label(
            self.__app.body_frame, text="customer email: ")
        self.__customer_email = tk.Entry(self.__app.body_frame)

        self.__card_number_lable = tk.Label(
            self.__app.body_frame, text="card number: ")
        self.__card_number = tk.Entry(self.__app.body_frame)

        self.__customer_email_lable.place(x=450, y=500)
        self.__customer_email.place(x=570, y=500)
        self.__card_number_lable.place(x=730, y=600)
        self.__card_number.place(x=850, y=600)

        # Placing interactive widgets
        self.__btn.place(x=50, y=380)

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
            self.__app.body_frame, self.__city_choice, *self.__controller.get_cities(), command=lambda city: (self.__controller.set_city(city), self.update_cinemas(lambda cinema: self.__controller.set_cinema(cinema), 1)))  # , command=self.__controller.set_cinema(self.__city_choice.get()))

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
        self.__listing_options_label = tk.Label(
            self.__app.body_frame, text="choose film: ")
        self.__listing_options = tk.OptionMenu(
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
            "Arial", 18), command=lambda: self.__controller.add_listing(self.__film_choice.get(), self.__cinema_choice.get()))
        self.__login_button.place(x=612, y=460)

        self.__city_options_lable.place(x=10, y=30)
        self.__city_options.place(x=100, y=30)
        self.__cinema_options_label.place(x=300, y=30)
        self.__cinema_options.place(x=400, y=30)
        self.__listing_options_label.place(x=10, y=90)
        self.__listing_options.place(x=100, y=90)
        self.__date_label.place(x=10, y=150)
        self.__date_entry.place(x=100, y=150)

    def remove_listing(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Remove listings"

        self.__city_options_label = tk.Label(
            self.__app.body_frame, text="choose city: ").place(x=10, y=30)
        self.__cinema_options_label = tk.Label(
            self.__app.body_frame, text="choose cinema: ").place(x=300, y=30)

        self.__city_choice = tk.StringVar()
        self.__city_choice.set(
            self.__controller.get_city())
        self.__city_options = tk.OptionMenu(self.__app.body_frame, self.__city_choice, *self.__controller.get_cities(),
                                            command=lambda city: (self.__controller.set_city(city), self.update_cinemas(lambda cinema: (self.__controller.set_cinema(cinema), self.update_listings(lambda listing: (self.__controller.set_listing(listing), self.update_shows()), 1)))))
        self.__city_options.place(x=100, y=30)

        self.__cinema_choice = tk.StringVar()
        self.__cinema_choice.set(self.__controller.get_cinema())
        self.__cinema_options = tk.OptionMenu(self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cinemas(), command=lambda cinema: [
            self.__controller.set_cinema(cinema), self.update_listings(lambda listing: (self.__controller.set_listing(listing), self.update_shows()), 1)])
        self.__cinema_options.place(x=400, y=30)

        # Standard labels
        self.__date_label = tk.Label(
            self.__app.body_frame, text="Select Date").place(x=10, y=90)
        self.__select_film_label = tk.Label(
            self.__app.body_frame, text="Select listing").place(x=10, y=150)
        self.__select_show_label = tk.Label(
            self.__app.body_frame, text="Select Show").place(x=10, y=210)

        # Date
        self.__selected_date = tk.StringVar()
        self.__date_entry = DateEntry(self.__app.body_frame, date_pattern='y-mm-dd',
                                      mindate=datetime.date.today(), textvariable=self.__selected_date)
        self.__selected_date.trace(
            'w', lambda *unused: (self.__controller.set_date(self.__selected_date.get()), self.update_listings(lambda listing: (self.__controller.set_listing(listing), self.update_shows()), 1)))
        self.__controller.set_date(str(datetime.date.today()))

        self.__listing_choice = tk.StringVar()
        self.__listing_choice.set(self.__controller.get_listing())
        self.__listing_options = tk.OptionMenu(
            self.__app.body_frame, self.__listing_choice, *self.__controller.get_listings(), command=lambda listing: (self.__controller.set_listing(listing), self.update_shows()))
        self.__listing_options.place(x=100, y=150)
        self.__remove_listing_btn = tk.Button(
            self.__app.body_frame, text="remove listing", command=lambda: self.__controller.remove_listing(self.__cinema_choice.get())).place(x=400, y=150)

        # Shows
        self.__show_choice = tk.StringVar()
        self.__show_choice.set(self.__controller.get_show())
        self.__show_options = tk.OptionMenu(
            self.__app.body_frame, self.__show_choice, *self.__controller.get_shows(), command=lambda show: self.__controller.set_show(show))
        self.__show_options.place(x=100, y=200)
        self.__remove_show_btn = tk.Button(
            self.__app.body_frame, text="remove show", command=self.__controller.remove_show).place(x=400, y=200)

        self.__date_entry.place(x=100, y=90)

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
        ), command=lambda city: (self.__controller.set_city(city), self.update_cinemas(lambda cinema: (self.__controller.set_cinema(cinema), self.update_listings(lambda listing: (self.__controller.set_listing(listing))))), self.update_listings(lambda listing: (self.__controller.set_listing(listing)))))

        # cinema
        self.__cinema_choice = tk.StringVar()
        self.__cinema_choice.set(self.__controller.get_cinema())
        self.__cinema_options_label = tk.Label(
            self.__app.body_frame, text="choose cinema: ")
        self.__cinema_options = tk.OptionMenu(
            self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cinemas(), command=lambda cinema: (self.__controller.set_cinema(cinema), self.update_listings(lambda listing: (self.__controller.set_listing(listing)))))

        # date
        self.__date_label = tk.Label(
            self.__app.body_frame, text="Select Date: ")
        self.__selected_date = tk.StringVar()
        self.__date_entry = DateEntry(self.__app.body_frame, date_pattern='y-mm-dd',
                                      mindate=datetime.date.today(), textvariable=self.__selected_date)
        self.__selected_date.trace(
            'w', lambda *unused: (self.__controller.set_date(self.__selected_date.get()), self.update_listings(lambda listing: (self.__controller.set_listing(listing)))))
        self.__controller.set_date(str(datetime.date.today()))

        # listings  (need to change this so they can only pick one)
        self.__listings_label = tk.Label(
            self.__app.body_frame, text="select listing:")
        self.__listing_choice = tk.StringVar()
        self.__listing_choice.set(self.__controller.get_listing())
        self.__listing_options = tk.OptionMenu(
            self.__app.body_frame, self.__listing_choice, *self.__controller.get_listings(), command=lambda listing: self.__controller.set_listing(listing))

        self.__login_button = tk.Button(self.__app.body_frame, text='select listing', bg='#DD2424', fg='#000000', font=("Arial", 18),
                                        command=lambda: self.update_listing_details(self.__listing_choice.get(), self.__city_choice.get(), self.__cinema_choice.get()))

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
        if listing_id == "no listings":
            self.show_error("Please select a listing.")
            return
        listing_id = self.get_id(listing_id)
        cinema = self.get_id(cinema)
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

        # select listing
        self.__film_choice = tk.StringVar()
        self.__film_choice.set(self.__original_film)
        self.__listing_options_label = tk.Label(
            self.__app.body_frame, text="choose film: ")
        self.__listing_options = tk.OptionMenu(
            self.__app.body_frame, self.__film_choice, *self.__controller.get_films().keys())

        # select date
        self.__date_label = tk.Label(
            self.__app.body_frame, text="Select Date: ")
        self.__selected_date = tk.StringVar()
        self.__date_entry = DateEntry(self.__app.body_frame, date_pattern='y-mm-dd',
                                      mindate=datetime.date.today(), textvariable=self.__selected_date)
        self.__selected_date.trace(
            'w', lambda *unused: (self.__controller.set_date(self.__selected_date.get())))
        self.__controller.set_date(str(datetime.date.today()))

        # update listing button
        self.__login_button = tk.Button(self.__app.body_frame, text='update listing', bg='#DD2424', fg='#000000', font=(
            "Arial", 18), command=lambda: self.__controller.update_listing(self.__film_choice.get()))

        # place buttons
        self.__login_button.place(x=612, y=460)

        self.__listing_options_label.place(x=10, y=30)
        self.__listing_options.place(x=100, y=30)
        self.__date_label.place(x=10, y=90)
        self.__date_entry.place(x=100, y=90)
        self.__orignal_listing_label.place(x=500, y=30)

    def generate_report(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Generate report"

        self.__city_options_label = tk.Label(
            self.__app.body_frame, text="choose city: ").place(x=10, y=30)
        self.__cinema_options_label = tk.Label(
            self.__app.body_frame, text="choose cinema: ").place(x=300, y=30)

        self.__city_choice = tk.StringVar()
        self.__city_choice.set(
            self.__controller.get_city())
        self.__city_options = tk.OptionMenu(self.__app.body_frame, self.__city_choice, *self.__controller.get_cities(),
                                            command=lambda city: (self.__controller.set_city(city), self.update_cinemas(lambda cinema: (self.__controller.set_cinema(cinema)))))
        self.__city_options.place(x=100, y=30)

        self.__cinema_choice = tk.StringVar()
        self.__cinema_choice.set(self.__controller.get_cinema())
        self.__cinema_options = tk.OptionMenu(self.__app.body_frame, self.__cinema_choice,
                                              *self.__controller.get_cinemas(), command=lambda cinema: [self.__controller.set_cinema(cinema)])
        self.__cinema_options.place(x=400, y=30)

        self.__start_date_label = tk.Label(
            self.__app.body_frame, text="start date").place(x=10, y=90)
        self.__selected_start_date = tk.StringVar()
        self.__start_date = DateEntry(self.__app.body_frame, date_pattern='y-mm-dd',
                                      maxdate=datetime.date.today(), textvariable=self.__selected_start_date).place(x=100, y=90)

        self.__end_date_label = tk.Label(
            self.__app.body_frame, text="end date").place(x=10, y=150)
        self.__selected_end_date = tk.StringVar()
        self.__end_date = DateEntry(self.__app.body_frame, date_pattern='y-mm-dd',
                                    maxdate=datetime.date.today(), textvariable=self.__selected_end_date).place(x=100, y=150)

        self.__listing_number_of_bookings = tk.Button(self.__app.body_frame, text='listing number\nof bookings', bg='#DD2424', fg='#000000', font=(
            "Arial", 18), command=lambda: self.__controller.listing_number_of_bookings(datetime.datetime.strptime(self.__selected_start_date.get(), '%Y-%m-%d').date(), datetime.datetime.strptime(self.__selected_end_date.get(), '%Y-%m-%d').date()))
        self.__listing_number_of_bookings.place(x=112, y=160+50)

        self.__cinema_revenue = tk.Button(self.__app.body_frame, text='cinema revenue\n(only dates required)', bg='#DD2424', fg='#000000', font=(
            "Arial", 18), command=lambda: self.__controller.cinema_revenue(datetime.datetime.strptime(self.__selected_start_date.get(), '%Y-%m-%d').date(), datetime.datetime.strptime(self.__selected_end_date.get(), '%Y-%m-%d').date()))
        self.__cinema_revenue.place(x=112, y=260+50)

        self.__film_revenue = tk.Button(self.__app.body_frame, text='film revenue\n(no data required)', bg='#DD2424', fg='#000000', font=(
            "Arial", 18), command=lambda: self.__controller.film_revenue())
        self.__film_revenue.place(x=112, y=360+50)

        self.__staff_number_of_bookings = tk.Button(self.__app.body_frame, text='staff number\nof bookings', bg='#DD2424', fg='#000000', font=(
            "Arial", 18), command=lambda: self.__controller.staff_number_of_bookings(datetime.datetime.strptime(self.__selected_start_date.get(), '%Y-%m-%d').date(), datetime.datetime.strptime(self.__selected_end_date.get(), '%Y-%m-%d').date()))
        self.__staff_number_of_bookings.place(x=112, y=460+50)

        self.__tree_frame = tk.Frame(
            self.__app.body_frame, width=700, height=400, bg='gainsboro')
        self.__tree_frame.place(x=350, y=200)

    def report_tree(self, data):
        self.clear_frame(self.__tree_frame)

        xscrollbar = tk.Scrollbar(self.__tree_frame, orient=tk.HORIZONTAL)
        yscrollbar = tk.Scrollbar(self.__tree_frame, orient=tk.VERTICAL)

        self.__tree_view = ttk.Treeview(
            self.__tree_frame, yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set, selectmode="extended", columns=list(data[0].keys()))

        self.__tree_view.grid(row=0, column=0)
        xscrollbar.configure(command=self.__tree_view.xview)
        yscrollbar.configure(command=self.__tree_view.yview)

        xscrollbar.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        yscrollbar.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        self.__tree_view.column("#0", width=0,  stretch=tk.NO)
        for d in data[0].keys():
            print(d)
            self.__tree_view.heading(d, text=d, anchor=tk.CENTER)
            self.__tree_view.column(d, anchor=tk.CENTER, width=140)
        for d in data:
            print(d)
            self.__tree_view.insert('', tk.END, values=list(d.values()))

    # IF WE DO BIRMIGNAHm

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
            self.__app.body_frame, self.__city_choice, *self.__controller.get_cities(), command=lambda city: (self.__controller.set_city(city), self.update_cinemas(lambda cinema: (self.__controller.set_cinema(cinema), self.update_listings(lambda listing: (self.__controller.set_listing(listing))))), self.update_listings(lambda listing: (self.__controller.set_listing(listing)))))  # , command=self.__controller.set_cinema(self.__city_choice.get()))

        # cinema
        self.__cinema_choice = tk.StringVar()
        self.__cinema_choice.set(self.__controller.get_cinema())
        self.__cinema_options_label = tk.Label(
            self.__app.body_frame, text="choose cinema: ")
        self.__cinema_options = tk.OptionMenu(
            self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cinemas(), command=lambda cinema: (self.__controller.set_cinema(cinema), self.update_listings(lambda listing: (self.__controller.set_listing(listing)))))

        # date
        self.__date_label = tk.Label(
            self.__app.body_frame, text="Select Date: ")
        self.__selected_date = tk.StringVar()
        self.__date_entry = DateEntry(self.__app.body_frame, date_pattern='y-mm-dd',
                                      mindate=datetime.date.today(), textvariable=self.__selected_date)
        self.__selected_date.trace(
            'w', lambda *unused: (self.__controller.set_date(self.__selected_date.get()), self.update_listings(lambda listing: (self.__controller.set_listing(listing)))))
        self.__controller.set_date(str(datetime.date.today()))

        # listings  (need to change this so they can only pick one)

        self.__listings_label = tk.Label(
            self.__app.body_frame, text="select listing:")
        self.__listing_choice = tk.StringVar()
        self.__listing_choice.set(self.__controller.get_listing())
        self.__listing_options = tk.OptionMenu(
            self.__app.body_frame, self.__listing_choice, *self.__controller.get_listings(), command=lambda listing: self.__controller.set_listing(listing))
        self.__listing_options.place(x=100, y=150)

        self.__time_label = tk.Label(
            self.__app.body_frame, text="select time: ")
        self.__hours_choice = tk.IntVar()
        self.__hours_choice.set(8)
        self.__hours_options = tk.OptionMenu(
            self.__app.body_frame, self.__hours_choice, *range(8, 24))
        self.__minutes_choice = tk.IntVar()
        self.__minutes_choice.set(0)
        self.__minutes_options = tk.OptionMenu(
            self.__app.body_frame, self.__minutes_choice, *range(0, 60, 5))

        self.__login_button = tk.Button(self.__app.body_frame, text='select listing', bg='#DD2424', fg='#000000', font=("Arial", 18),
                                        command=lambda: self.__controller.add_show(datetime.time(self.__hours_choice.get(), self.__minutes_choice.get()), self.__cinema_choice.get()))

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
        self.__add_new_city_btn = tk.Button(
            self.__app.body_frame, text="Add New city", command=self.add_new_city)

        self.__cinema_address_lable = tk.Label(
            self.__app.body_frame, text="Cinema address: ")
        self.__cinema_address = tk.Entry(self.__app.body_frame)

        self.__number_of_screens_lable = tk.Label(
            self.__app.body_frame, text="Number of screens: ")
        self.__number_of_screens = tk.Entry(self.__app.body_frame)

        self.__login_button = tk.Button(self.__app.body_frame, text='Add cinema', bg='#DD2424', fg='#000000', font=(
            "Arial", 18), command=lambda: self.__controller.add_cinema(self.__cinema_address.get(), self.__number_of_screens.get()))
        self.__login_button.place(x=612, y=460)

        self.__city_options_lable.place(x=10, y=30)
        self.__city_options.place(x=130, y=30)
        self.__add_new_city_btn.place(x=250, y=30)
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

    def add_new_film(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Add new film"

        self.__film_title_lable = tk.Label(
            self.__app.body_frame, text="film title: ")
        self.__film_title = tk.Entry(self.__app.body_frame)

        self.__film_rating_lable = tk.Label(
            self.__app.body_frame, text="film rating: ")
        self.__film_rating = tk.Entry(self.__app.body_frame)

        self.__film_genre_lable = tk.Label(
            self.__app.body_frame, text="film genre: ")
        self.__film_genre = tk.Entry(self.__app.body_frame)

        self.__film_year_lable = tk.Label(
            self.__app.body_frame, text="film year: ")
        self.__film_year = tk.Entry(self.__app.body_frame)

        self.__film_age_rating_lable = tk.Label(
            self.__app.body_frame, text="film age rating: ")
        self.__film_age_rating = tk.Entry(self.__app.body_frame)

        self.__film_duration_lable = tk.Label(
            self.__app.body_frame, text="film duration: ")
        self.__film_duration = tk.Entry(self.__app.body_frame)

        self.__film_description_lable = tk.Label(
            self.__app.body_frame, text="film description: ")
        self.__film_description = tk.Entry(self.__app.body_frame)

        self.__film_cast_lable = tk.Label(
            self.__app.body_frame, text="film cast: ")
        self.__film_cast = tk.Entry(self.__app.body_frame)
        self.__login_button = tk.Button(self.__app.body_frame, text='Add film', bg='#DD2424', fg='#000000', font=("Arial", 18), command=lambda: self.__controller.add_film(self.__film_title.get(
        ), self.__film_rating.get(), self.__film_genre.get(), self.__film_year.get(), self.__film_age_rating.get(), self.__film_duration.get(), self.__film_description.get(), self.__film_cast.get()))
        self.__login_button.place(x=612, y=460)

        self.__film_title_lable.place(x=10, y=30)
        self.__film_title.place(x=130, y=30)
        self.__film_rating_lable.place(x=10, y=90)
        self.__film_rating.place(x=130, y=90)
        self.__film_genre_lable.place(x=10, y=150)
        self.__film_genre.place(x=130, y=150)
        self.__film_year_lable.place(x=10, y=210)
        self.__film_year.place(x=130, y=210)
        self.__film_age_rating_lable.place(x=10, y=270)
        self.__film_age_rating.place(x=130, y=270)
        self.__film_duration_lable.place(x=10, y=330)
        self.__film_duration.place(x=130, y=330)
        self.__film_description_lable.place(x=10, y=390)
        self.__film_description.place(x=130, y=390)
        self.__film_cast_lable.place(x=10, y=450)
        self.__film_cast.place(x=130, y=450)

    def add_new_user(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Add new user"

        # city
        self.__city_choice = tk.StringVar()
        self.__city_choice.set(self.__controller.get_city())
        self.__city_options_lable = tk.Label(
            self.__app.body_frame, text="choose city: ")
        self.__city_options = tk.OptionMenu(
            self.__app.body_frame, self.__city_choice, *self.__controller.get_cities(), command=lambda city: (self.__controller.set_city(city), self.update_cinemas(lambda cinema: self.__controller.set_cinema(cinema))))  # , command=self.__controller.set_cinema(self.__city_choice.get()))

        # cinema
        self.__cinema_choice = tk.StringVar()
        self.__cinema_choice.set(self.__controller.get_cinema())
        self.__cinema_options_label = tk.Label(
            self.__app.body_frame, text="choose cinema: ")
        self.__cinema_options = tk.OptionMenu(
            self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cinemas(), command=lambda cinema: (self.__controller.set_cinema(cinema)))

        types = self.__controller.get_user_types()
        self.__user_type_choice = tk.StringVar()
        self.__user_type_choice.set(types[0])
        self.__user_type_label = tk.Label(
            self.__app.body_frame, text="user type:")
        self.__user_type_options = tk.OptionMenu(
            self.__app.body_frame, self.__user_type_choice, *types)

        self.__user_name_lable = tk.Label(
            self.__app.body_frame, text="user name: ")
        self.__user_name = tk.Entry(self.__app.body_frame)

        self.__user_password_lable = tk.Label(
            self.__app.body_frame, text="user password: ")
        self.__user_password = tk.Entry(self.__app.body_frame, show="*")

        self.__login_button = tk.Button(self.__app.body_frame, text='Add user', bg='#DD2424', fg='#000000', font=("Arial", 18), command=lambda: self.__controller.add_user(
            self.__user_name.get(), self.__user_password.get(), self.__user_type_choice.get(), self.__cinema_choice.get()))
        self.__login_button.place(x=612, y=460)

        self.__city_options_lable.place(x=10, y=30)
        self.__city_options.place(x=100, y=30)
        self.__cinema_options_label.place(x=300, y=30)
        self.__cinema_options.place(x=400, y=30)
        self.__user_type_label.place(x=10, y=90)
        self.__user_type_options.place(x=130, y=90)
        self.__user_name_lable.place(x=10, y=150)
        self.__user_name.place(x=130, y=150)
        self.__user_password_lable.place(x=10, y=210)
        self.__user_password.place(x=130, y=210)

    def print_film(self):
        record = self.__tree_view.item(self.__tree_view.selection()[0])[
            "values"][2]
        film = self.__controller.get_films()[str(record)].__dict__
        a = film["_Film__description"].split()
        print(a)
        film["_Film__description"] = ''
        print(film["_Film__description"])
        for i in range(0, len(a), 15):
            film["_Film__description"] += ' '.join(a[i:i+10]) + '\n'

        self.__film_label["text"] = "\n".join(
            [f"{x.replace('_', ' ')}: {y}" for x, y in film.items()])

    def get_id(self, string):
        print(string, type(string))
        return int(re.search(r'\d+', string).group())

    def remove_create_stuff(self):
        try:
            self.__listing_options.destroy()
        except:
            pass
        try:
            self.__show_options.destroy()
        except:
            pass
        try:
            self.__btn.destroy()
        except:
            pass
        try:
            self.clear_frame(self.__tree_frame)
        except:
            pass

    def update_cinemas(self, func, add_listing=0):
        if add_listing == 1:  # need this
            pass
        else:
            self.remove_create_stuff()
        self.__cinema_choice.set(self.__controller.get_cinema())
        self.__cinema_options.destroy()
        self.__cinema_options = tk.OptionMenu(
            self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cinemas(), command=func)
        self.__cinema_options.place(x=400, y=30)

    def update_listings(self, func, remove_listing=0):
        # added in commit 124, get rid of if doesnt work
        self.__controller.set_date(str(self.__selected_date.get()))
        self.__listing_options.destroy()
        self.__listing_choice = tk.StringVar()
        self.__listing_choice.set(self.__controller.get_listing())
        self.__listing_options = tk.OptionMenu(
            self.__app.body_frame, self.__listing_choice, *self.__controller.get_listings(), command=func)
        self.__listing_options.place(x=100, y=150)
        if remove_listing == 1:  # Needs this. Without this if we do. Remove listing --> Bristol, Cinema_ID:1 --> date: 2022-01-13 --> It will show listing but not the shows and we have to click it again which is unintuitive and not good at all
            self.update_shows()

    def update_listings_and_shows_based_on_date(self, btn_text, btn_command):
        self.remove_create_stuff()

        self.__controller.set_date(str(self.__selected_date.get()))
        self.__film_choice = tk.StringVar()
        self.__film_choice.set(self.__controller.get_listing())
        self.__listing_options = tk.OptionMenu(
            self.__app.body_frame, self.__film_choice, *self.__controller.get_listings(), command=lambda listing: (self.__controller.set_listing(listing), self.update_shows()))

        # Shows
        self.__show_choice = tk.StringVar()
        self.__show_choice.set(self.__controller.get_show())
        self.__show_options = tk.OptionMenu(
            self.__app.body_frame, self.__show_choice, *self.__controller.get_shows(), command=lambda show: self.__controller.set_show(show))

        self.__btn = tk.Button(
            self.__app.body_frame, text=btn_text, command=btn_command)

        self.__listing_options.place(x=100, y=150)
        self.__show_options.place(x=100, y=200)
        self.__btn.place(x=50, y=380)

    def update_shows(self):
        print("im in")
        self.__show_options.destroy()
        self.__show_choice = tk.StringVar()
        self.__show_choice.set(self.__controller.get_show())
        self.__show_options = tk.OptionMenu(self.__app.body_frame, self.__show_choice,
                                            *self.__controller.get_shows(), command=lambda show: [self.__controller.set_show(show)])
        self.__show_options.place(x=100, y=200)
