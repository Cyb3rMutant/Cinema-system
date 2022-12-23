import tkinter as tk
import tkinter.messagebox
from tkcalendar import DateEntry
import datetime
from admin import Admin
from manager import Manager
import re
import random
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

            if (isinstance(self.__user, Manager)):
                add_new_cinema_btn.place(x=770, y=340, width=240, height=130)
                add_new_city_btn.place(x=270, y=480, width=240, height=130)

    def view_bookings(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "View booking"
        if (isinstance(self.__user, Admin)):
            pass
        else:
            self.__controller.get_bookings(self.__user.get_branch())

    def update_films_and_shows_based_on_date(self, *args):
        try:
            self.book_now_btn.destroy()
        except:
            pass
        # Clearing both options
        menu = self.film_options["menu"]
        menu.delete(0, "end")
        menu2 = self.show_options["menu"]
        menu2.delete(0, "end")
        self.film_choice.set('')
        self.show_choice.set('')

        # Assigns an ID to cinema chosen (0,1,2). The og cinema with all the data will always be 0 cus it came first
        i = 0
        for obj in (self.__controller.get_cities()[self.__city_choice.get()].get_cinemas()):
            if str(self.__cinema_choice.get()) == str(obj.get_address()):
                self.cinema_num.set(i)
            i += 1

        self.__film_list_titles_update = []
        # For every listing in the selected cinema on the date chosen, add it to an array
        for listing_on_date in self.__controller.get_cities()[self.__city_choice.get()].get_cinemas()[self.cinema_num.get()].get_listings():
            temp_date = str(self.selected_date.get())
            if temp_date == str(listing_on_date.get_date()):
                self.__film_list_titles_update.append(
                    str(listing_on_date.get_film()))

        # If there are listings airing at the cinema on the date then
        if len(self.__film_list_titles_update) > 0:
            # Placing film titles into optionsmenu
            # for film_title in self.__film_list_titles_update:
            #     self.film_choice.set(film_title)
            #     # menu.add_command(label=film_title,command=self.update_shows_based_on_film) #Command doesn't work to set the actual value. It still works without the i.
            #     menu.add_command(label=film_title, command=lambda value=film_title: self.film_choice.set(value)) #Command doesn't work to set the actual value. It still works without the i.

            # Hardcoded way just replacing the widget with a new one.
            # The code above works, the only problem is that the command attached to film_options to update the show_options gets removed when we change the date. e.g. load page --> change date --> 2 films airing --> click other film --> [Doesn't display showings for newly clicked film, still showing previous film showings]
            # But if we, load page --> dont change date --> change film, it works

            # Add all the choices to film options
            self.film_choice.set(self.__film_list_titles_update[0])
            self.film_options.destroy()
            self.film_options = tk.OptionMenu(self.__app.body_frame, self.film_choice,
                                              *self.__film_list_titles_update, command=self.update_shows_based_on_film)
            self.film_options.place(x=100, y=150)

            # Shows
            # Gets the shows for film listing selected. It puts it into a list size of 1. e.g. len(show_times_list_object) = 1. len(show_times_list_object[0]) = 4 because 4 shows for the listing
            film_title = self.film_choice.get()  # Gets film selected
            self.show_times_list_object = []
            # For every listing in the cinema
            for listing_on_date in (self.__controller.get_cities()[self.__city_choice.get()].get_cinemas()[self.cinema_num.get()].get_listings()):
                temp_date = str(self.selected_date.get())
                # If the listings date is the same as date selected
                if temp_date == str(listing_on_date.get_date()):
                    # If the listings date is the same as date selected AND the listings title is equal to the one chosen
                    if str(film_title) == str(listing_on_date.get_film()):

                        # Removed the object way, it was messy and unneeded
                        # Getting every show time for the listing
                        self.show_times_list = []
                        for show in listing_on_date.get_shows():
                            self.show_times_list.append(show.get_time())

                        # Outputting the shows into optionsmenu
                        self.show_choice.set(self.show_times_list[0])
                        self.show_options.destroy()
                        self.show_options = tk.OptionMenu(
                            self.__app.body_frame, self.show_choice, *self.show_times_list, command=self.destroy_book_now_btn)
                        self.show_options.place(x=100, y=200)

                        # Same problem as film options. Cant attach the destroy_book_now_btn command when we do it this way.
                        # for show_time in self.show_times_list:
                        #     self.show_choice.set(show_time)
                        #     menu2.add_command(label=show_time, command=lambda value=show_time: self.show_choice.set(value))

            print(str(self.show_times_list))

        else:
            print("no films airing today")  # Debug

    def update_shows_based_on_film(self, film_title):
        try:
            self.book_now_btn.destroy()
        except:
            pass

        # Assigns an ID to cinema chosen (0,1,2). The og cinema with all the data will always be 0 cus it came first
        i = 0
        for obj in (self.__controller.get_cities()[self.__city_choice.get()].get_cinemas()):
            if str(self.__cinema_choice.get()) == str(obj.get_address()):
                self.cinema_num.set(i)
            i += 1

        # Does the same as the code above. Just updating show options when a different film is selected.
        menu = self.show_options["menu"]
        menu.delete(0, "end")
        film_title = self.film_choice.get()
        self.show_choice.set('')
        self.show_times_list_object = []
        # For every listing in the cinema
        for listing_on_date in (self.__controller.get_cities()[self.__city_choice.get()].get_cinemas()[self.cinema_num.get()].get_listings()):
            temp_date = str(self.selected_date.get())
            # If the listings date is the same as date selected
            if temp_date == str(listing_on_date.get_date()):
                # If the listings date is the same as date selected AND the listings title is equal to the one chosen
                if str(film_title) == str(listing_on_date.get_film()):

                    # Getting every show time for the listing
                    self.show_times_list = []
                    for show in listing_on_date.get_shows():
                        self.show_times_list.append(show.get_time())

                       # Outputting the shows into optionsmenu
                        self.show_choice.set(self.show_times_list[0])
                        self.show_options.destroy()
                        self.show_options = tk.OptionMenu(
                            self.__app.body_frame, self.show_choice, *self.show_times_list, command=self.destroy_book_now_btn)
                        self.show_options.place(x=100, y=200)

                        # Same problem as film options. Cant attach the destroy_book_now_btn command when we do it this way.
                        # for show_time in self.show_times_list:
                        #     self.show_choice.set(show_time)
                        #     menu2.add_command(label=show_time, command=lambda value=show_time: self.show_choice.set(value))

    def destroy_book_now_btn(self, *args):
        try:
            self.book_now_btn.destroy()
        except:
            pass

    def update_cinemas_booking(self, city):
        # Adds all cinemas for selected city
        menu = self.__cinema_options["menu"]
        menu.delete(0, "end")
        self.__cinema_choice.set(self.__controller.get_cities()[
                                 city].get_cinemas()[0])
        self.__cinema_options.destroy()
        self.__cinema_options = tk.OptionMenu(self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cities()[
                                              self.__city_choice.get()].get_cinemas(), command=self.update_films_and_shows_based_on_date)
        self.__cinema_options.place(x=400, y=50)
        # Updating rest of params based on the new city
        self.update_films_and_shows_based_on_date()

    def create_booking(self):

        # When we change cinema option value --> update_films_and_shows_based_on_date. (Because we fill in the rest of paramaeters using city chosen)
        # When we change date value --> update_films_and_shows_based_on_date (We fetch all listings showing at a specific day at the cinema)
        # When we change a film value -->  update_shows_based_on_film (We fetch all showing times for the listing)
        # When we chang ea show --> Nothing

        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Create booking"

        if (isinstance(self.__user, Admin)):
            self.__city_choice = tk.StringVar()
            self.__city_choice.set(
                list(self.__controller.get_cities().keys())[0])
            self.__city_options_lable = tk.Label(
                self.__app.body_frame, text="choose city: ").place(x=0, y=50)
            self.__city_options = tk.OptionMenu(self.__app.body_frame, self.__city_choice, *self.__controller.get_cities(
            ).keys(), command=self.update_cinemas_booking)  # When we change a city, we update its cinemas
            self.__city_options.place(x=100, y=50)

            self.__cinema = self.__controller.get_cities(
            )[self.__city_choice.get()].get_cinemas()[0]
            self.__cinema_choice = tk.StringVar()
            self.__cinema_choice.set(self.__cinema)
            self.__cinema_options_label = tk.Label(
                self.__app.body_frame, text="choose cinema: ").place(x=300, y=50)
            self.__cinema_options = tk.OptionMenu(self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cities()[
                                                  self.__city_choice.get()].get_cinemas(), command=self.update_films_and_shows_based_on_date)
            self.__cinema_options.place(x=400, y=50)

            # Assigns an ID to cinema chosen (0,1,2). The og cinema with all the data will always be 0 cus it came first
            self.cinema_num = tk.IntVar()
            self.cinema_num.set(0)
            i = 0
            for obj in (self.__controller.get_cities()[self.__city_choice.get()].get_cinemas()):
                if str(self.__cinema_choice.get()) == str(obj.get_address()):
                    self.cinema_num.set(i)
                i += 1

        else:
            # Still need todo - Get booking staffs city
            self.__city_choice = tk.StringVar()
            self.__city_choice.set("Bristol")

            # Dynamic cinema numbers. Our original cinemas with all the data value will always be 0 because it came first.
            # Will be 0 for the OG cinemas we have. If we add any more they'll be 1.2.3.4. etc. (Used as an index)
            self.cinema_num = tk.IntVar()
            i = 0
            for obj in (self.__controller.get_cities()[self.__city_choice.get()].get_cinemas()):
                if str(self.__user.get_branch()) == str(obj.get_address()):
                    self.cinema_num.set(i)
                i += 1

        # Standard labels
        self.__date_label = tk.Label(
            self.__app.body_frame, text="Select Date").place(x=0, y=100)
        self.__select_film_label = tk.Label(
            self.__app.body_frame, text="Select Film").place(x=0, y=150)
        self.__select_show_label = tk.Label(
            self.__app.body_frame, text="Select Show").place(x=0, y=200)
        self.__select_seat_type = tk.Label(
            self.__app.body_frame, text="Select Ticket Type").place(x=0, y=250)
        self.__select_num_of_seats = tk.Label(
            self.__app.body_frame, text="Select # of Tickets").place(x=0, y=300)

        # Date
        self.selected_date = tk.StringVar()
        self.__date_today = datetime.date.today()
        self.__date_entry = DateEntry(self.__app.body_frame, date_pattern='y-mm-dd',
                                      mindate=self.__date_today, textvariable=self.selected_date)
        self.selected_date.trace(
            'w', self.update_films_and_shows_based_on_date)  # Event listener

        # Films - Gets all listing titles (film titles) based on the date selected. Only here for first loadup of page, as after the first load whenever date is changed it goes to function
        self.film_choice = tk.StringVar()
        self.film_choice.set('')
        self.film_list_titles = ['']

        # For every listing in the cinema
        for listing_on_date in self.__controller.get_cities()[self.__city_choice.get()].get_cinemas()[self.cinema_num.get()].get_listings():
            temp_date = str(self.selected_date.get())
            # If the listings date is the same as date selected -> Add it to array for options menu
            if temp_date == str(listing_on_date.get_date()):
                self.film_list_titles.append(str(listing_on_date.get_film()))

        # Formatting crap -ignore
        try:
            self.film_choice.set(self.film_list_titles[1])
            self.film_list_titles.pop(0)
        except:
            pass

        # Command doesnt work if we change date then change film, only works first time loaded thats why i hardcoded destroy widget in the update_film_and_show function.
        self.film_options = tk.OptionMenu(
            self.__app.body_frame, self.film_choice, *self.film_list_titles, command=self.update_shows_based_on_film)

        # Shows

        self.show_times_list = ['']
        film_title = self.film_choice.get()
        self.show_times_list_object = []

        # For every listing in the cinema
        for listing_on_date in (self.__controller.get_cities()[self.__city_choice.get()].get_cinemas()[self.cinema_num.get()].get_listings()):
            temp_date = str(self.selected_date.get())
            # If the listings date is the same as date selected
            if temp_date == str(listing_on_date.get_date()):
                # If the listings date is the same as date selected AND the listings title is equal to the one chosen
                if str(film_title) == str(listing_on_date.get_film()):

                    # Getting every show time for the listing
                    self.show_times_list = []
                    for show in listing_on_date.get_shows():
                        self.show_times_list.append(show.get_time())

                    self.show_times_list.pop(0)

        self.show_choice = tk.StringVar()
        self.show_choice.set('')
        self.show_choice.set(self.show_times_list[0])
        self.show_options = tk.OptionMenu(
            self.__app.body_frame, self.show_choice, *self.show_times_list, command=self.destroy_book_now_btn)

        # Ticket type & Number of tickets entry
        self.seat_type_btn = tk.StringVar()
        self.lower_hall = tk.Radiobutton(self.__app.body_frame, text="Lower", value="Lower",
                                         variable=self.seat_type_btn, tristatevalue=0, command=self.destroy_book_now_btn)
        self.upper_hall = tk.Radiobutton(self.__app.body_frame, text="Upper", value="Upper",
                                         variable=self.seat_type_btn, tristatevalue=0, command=self.destroy_book_now_btn)
        self.vip_hall = tk.Radiobutton(self.__app.body_frame, text="VIP", value="VIP",
                                       variable=self.seat_type_btn, tristatevalue=0, command=self.destroy_book_now_btn)

        self.num_of_tickets_list = [1, 2, 3, 4, 5]
        self.num_of_ticket_choice = tk.IntVar()
        self.num_of_ticket_choice.set(self.num_of_tickets_list[0])
        self.num_of_ticket_options = tk.OptionMenu(
            self.__app.body_frame, self.num_of_ticket_choice, *self.num_of_tickets_list, command=self.destroy_book_now_btn)

        self.check_availability = tk.Button(
            self.__app.body_frame, text='Check Availability and Price', command=self.verify_booking_data)

        # Book Now button is only created when we verify the booking data

        # Placing interactive widgets
        self.__date_entry.place(x=100, y=100)
        self.film_options.place(x=100, y=150)
        self.show_options.place(x=100, y=200)

        self.lower_hall.place(x=100, y=250)
        self.upper_hall.place(x=220, y=250)
        self.vip_hall.place(x=340, y=250)

        self.num_of_ticket_options.place(x=100, y=300)
        self.check_availability.place(x=50, y=350)

    def verify_booking_data(self):
        cinema = self.__city_choice.get()  # Cinema is city in this instance for ease
        date = self.selected_date.get()
        film = self.film_choice.get()
        show = self.show_choice.get()
        seat_type = self.seat_type_btn.get()
        num_of_tickets = self.num_of_ticket_choice.get()

        Upper = False
        Lower = False
        VIP = False
        if seat_type == "Upper":
            Upper = True
        if seat_type == "Lower":
            Lower = True
        if seat_type == "VIP":
            VIP = True

        seat_availability = False

        multiplier = 0

        # If any fields are null its len 0
        if (len(film) > 0 and len(show) > 0 and len(seat_type) > 0):
            print("data is filled in correctly!")

            # For every listing in the cinema
            for listing_on_date in (self.__controller.get_cities()[cinema].get_cinemas()[self.cinema_num.get()].get_listings()):
                if str(date) == str(listing_on_date.get_date()):
                    if str(film) == str(listing_on_date.get_film()):
                        # For every showing in for the selected listing
                        for showing in listing_on_date.get_shows():
                            # Now we have the specific showing that we want since we got it's time.
                            if show == str(showing.get_time()):
                                show_id = showing.get_show_id()  # Get ID for later
                                # Need to check if theres available seats for seleceted seat type
                                if Lower == True:
                                    if (showing.get_available_lower_seats() - num_of_tickets >= 0):
                                        seat_availability = True
                                        multiplier = 1
                                if Upper == True:
                                    if (showing.get_available_upper_seats() - num_of_tickets >= 0):
                                        seat_availability = True
                                        multiplier = 1.2
                                if VIP == True:
                                    if (showing.get_available_vip_seats() - num_of_tickets >= 0):
                                        seat_availability = True

            if (seat_availability):
                print("available seats")
                # Now there are seats available for the showing, check price
                # Price --> Dependant on SHOWING TIME and CITY and TICKET TYPE

                # Generate price of ticket
                # 12:00:00 turned to 120000
                show_int = show.replace(":", "")
                show_int = int(show_int)
                if (show_int >= 80000 and show_int <= 120000):
                    city_price_lower_hall = self.__controller.get_cities(
                    )[cinema].get_morning_price()  # cinema is city in this instance
                if (show_int >= 120001 and show_int <= 170000):
                    city_price_lower_hall = self.__controller.get_cities(
                    )[cinema].get_afternoon_price()  # cinema is city in this instance
                if (show_int >= 170001 and show_int <= 240000):
                    city_price_lower_hall = self.__controller.get_cities(
                    )[cinema].get_evening_price()  # cinema is city in this instance

                if (Lower) or (Upper):
                    one_ticket = city_price_lower_hall * multiplier
                if (VIP):
                    one_ticket = (city_price_lower_hall * 1.2) * 1.2

                final_ticket_price = one_ticket * num_of_tickets
                final_ticket_price = round(final_ticket_price, 2)

                # Generate random booking reference
                booking_reference = random.randint(100000, 999999)

                date_today = str(datetime.today().strftime('%Y-%m-%d'))

                self.book_now_btn = tk.Button(self.__app.body_frame, text='Book Now',  bg='#DD2424', fg='#000000',
                                              command=lambda: self.add_booking_command(booking_reference, num_of_tickets, date_today, final_ticket_price, show_id, seat_type, "poop@gmail.com"))
                self.book_now_btn.place(x=50, y=400)

                # self.book_now_btn = tk.Button(self.__app.body_frame, text='Book Now',  bg='#DD2424', fg='#000000')

            else:
                print("no available seats")

        else:
            print("data is not all filled in correctly")

    def add_booking_command(self, booking_reference, num_of_tickets, date, final_ticket_price, show_id, seat_type, customer_email):
        # pass booking info to this function so we print green labels and receipts etc.
        self.__controller.add_booking(booking_reference, num_of_tickets,
                                      date, final_ticket_price, show_id, seat_type, "poop@gmail.com")
        print("successfully done booking")
        print("booking info: ")
        print(f'{booking_reference}\n{num_of_tickets}\n{date}\n{final_ticket_price}\n{show_id}\n{seat_type}\n poop@gmail.com \n')

    def view_film_listings(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "View film listings"

    def cancel_booking(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Cancel booking"

    def update_cinemas(self, func):
        self.__cinema_choice.set("choose cinema")
        self.__cinema_options = tk.OptionMenu(
            self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cities()[self.__city_choice.get()].get_cinemas(), command=func)
        self.__cinema_options.place(x=100, y=70)

    def update_screens(self, cinema):
        print(cinema, type(cinema))
        self.clear_frame(self.__screens_box)
        self.__items = []
        idx = 0
        for screen in cinema.get_screens():
            self.__items.append(tk.IntVar())
            tk.Checkbutton(
                self.__screens_box, variable=self.__items[idx], text=screen, onvalue=screen.get_screen_id(), offvalue=None).pack(sid=tk.BOTTOM)
            idx += 1

    def update_listings_many(self, cinema):
        print(cinema, type(cinema))
        self.clear_frame(self.__listings_box)
        self.__items = []
        idx = 0
        for listing in cinema.get_listings():
            if listing.get_date() < datetime.date.today():
                continue

            self.__items.append(tk.IntVar())
            tk.Checkbutton(
                self.__listings_box, variable=self.__items[idx], text=listing, onvalue=listing.get_listing_id(), offvalue=None).pack(sid=tk.BOTTOM)
            idx += 1

    def update_listings_one(self, cinema):
        print(cinema, type(cinema))
        self.clear_frame(self.__listings_box)
        self.__item = tk.IntVar()
        for listing in cinema.get_listings():
            if listing.get_date() < datetime.date.today():
                continue

            tk.Checkbutton(
                self.__listings_box, variable=self.__item, text=listing, onvalue=listing.get_listing_id(), offvalue=None).pack(sid=tk.BOTTOM)

    def add_listing(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Add listings"

        # city
        self.__city_choice = tk.StringVar()
        self.__city_choice.set(list(self.__controller.get_cities().keys())[0])
        self.__city_options_lable = tk.Label(
            self.__app.body_frame, text="choose city: ")
        self.__city_options = tk.OptionMenu(
            self.__app.body_frame, self.__city_choice, *self.__controller.get_cities().keys(), command=lambda unused: self.update_cinemas(self.update_screens))  # , command=self.set_cinema(self.__city_choice.get()))

        # cinema
        self.__cinema_choice = tk.StringVar()
        self.__cinema_choice.set(self.__controller.get_cities()[
                                 self.__city_choice.get()].get_cinemas()[0])
        self.__cinema_options_label = tk.Label(
            self.__app.body_frame, text="choose cinema: ")
        self.__cinema_options = tk.OptionMenu(
            self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cities()[self.__city_choice.get()].get_cinemas(), command=self.update_screens)

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
        self.__date_entry = DateEntry(
            self.__app.body_frame, mindate=datetime.date.today())

        # # screens
        # self.__screens_label = tk.Label(
        #     self.__app.body_frame, text="Select screens: ")
        # self.__screens_box = tk.Frame(self.__app.body_frame)
        # self.__items = []
        # idx = 0
        # for screen in self.__controller.get_cities()[self.__city_choice.get()].get_cinemas()[0].get_screens():
        #     self.__items.append(tk.IntVar())
        #     tk.Checkbutton(
        #         self.__screens_box, variable=self.__items[idx], text=screen, onvalue=screen.get_screen_id(), offvalue=None).pack()
        #     idx += 1

        self.__login_button = tk.Button(self.__app.body_frame, text='add listing', bg='#DD2424', fg='#000000', font=("Arial", 18), command=lambda: self.__controller.add_listing(
            self.__date_entry.get_date(), self.__film_choice.get(), self.__city_choice.get(), self.get_id(self.__cinema_choice.get())))
        self.__login_button.place(x=612, y=460)

        self.__city_options_lable.place(x=10, y=10)
        self.__city_options.place(x=100, y=10)
        self.__cinema_options_label.place(x=10, y=70)
        self.__cinema_options.place(x=100, y=70)
        self.__film_options_label.place(x=10, y=140)
        self.__film_options.place(x=100, y=140)
        self.__date_label.place(x=10, y=210)
        self.__date_entry.place(x=100, y=210)
        # self.__screens_label.place(x=10, y=280)
        # self.__screens_box.place(x=100, y=280)

    def remove_listing(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Remove listings"

        # city
        self.__city_choice = tk.StringVar()
        self.__city_choice.set(list(self.__controller.get_cities().keys())[0])
        self.__city_options_lable = tk.Label(
            self.__app.body_frame, text="choose city: ")
        self.__city_options = tk.OptionMenu(
            self.__app.body_frame, self.__city_choice, *self.__controller.get_cities().keys(), command=lambda unused: self.update_cinemas(self.update_listings_many))  # , command=self.set_cinema(self.__city_choice.get()))

        # cinema
        self.__cinema_choice = tk.StringVar()
        self.__cinema_choice.set(self.__controller.get_cities()[
                                 self.__city_choice.get()].get_cinemas()[0])
        self.__cinema_options_label = tk.Label(
            self.__app.body_frame, text="choose cinema: ")
        self.__cinema_options = tk.OptionMenu(
            self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cities()[self.__city_choice.get()].get_cinemas(), command=self.update_listings_many)

        # date
        self.__date_label = tk.Label(
            self.__app.body_frame, text="Select Date: ")
        self.__date_entry = DateEntry(
            self.__app.body_frame, mindate=datetime.date.today())

        # listings
        self.__listings_label = tk.Label(
            self.__app.body_frame, text="Select listings: ")
        self.__listings_box = tk.Frame(self.__app.body_frame)
        self.__items = []
        idx = 0
        for listing in self.__controller.get_cities()[self.__city_choice.get()].get_cinemas()[0].get_listings():
            if listing.get_date() < datetime.date.today():
                continue

            self.__items.append(tk.IntVar())
            tk.Checkbutton(
                self.__listings_box, variable=self.__items[idx], text=listing, onvalue=listing.get_listing_id(), offvalue=None).pack()
            idx += 1

        self.__login_button = tk.Button(self.__app.body_frame, text='remove listing', bg='#DD2424', fg='#000000', font=("Arial", 18), command=lambda: self.__controller.remove_listing(
            self.__city_choice.get(), self.get_id(self.__cinema_choice.get()), [int(id.get()) for id in self.__items if id != None]))
        self.__login_button.place(x=612, y=460)

        self.__city_options_lable.place(x=10, y=10)
        self.__city_options.place(x=100, y=10)
        self.__cinema_options_label.place(x=10, y=70)
        self.__cinema_options.place(x=100, y=70)
        self.__date_label.place(x=10, y=210)
        self.__date_entry.place(x=100, y=210)
        self.__listings_label.place(x=10, y=280)
        self.__listings_box.place(x=100, y=280)

    def update_listing(self):
        print("Update listing page opened")  # debugging
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Update listings"

        # city
        self.__city_choice = tk.StringVar()
        self.__city_choice.set(list(self.__controller.get_cities().keys())[0])
        self.__city_options_lable = tk.Label(
            self.__app.body_frame, text="choose city: ")
        self.__city_options = tk.OptionMenu(
            self.__app.body_frame, self.__city_choice, *self.__controller.get_cities().keys(), command=lambda unused: self.update_cinemas(self.update_listings_one))  # , command=self.set_cinema(self.__city_choice.get()))

        # cinema
        self.__cinema_choice = tk.StringVar()
        self.__cinema_choice.set(self.__controller.get_cities()[
                                 self.__city_choice.get()].get_cinemas()[0])
        self.__cinema_options_label = tk.Label(
            self.__app.body_frame, text="choose cinema: ")
        self.__cinema_options = tk.OptionMenu(
            self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cities()[self.__city_choice.get()].get_cinemas(), command=self.update_listings_one)

        # date
        self.__date_label = tk.Label(
            self.__app.body_frame, text="Select Date: ")
        self.__date_entry = DateEntry(
            self.__app.body_frame, mindate=datetime.date.today())

        # listings  (need to change this so they can only pick one)
        self.__listings_label = tk.Label(
            self.__app.body_frame, text="Select listings: ")
        self.__listings_box = tk.Frame(self.__app.body_frame)
        self.__item = tk.IntVar()
        for listing in self.__controller.get_cities()[self.__city_choice.get()].get_cinemas()[0].get_listings():
            if listing.get_date() < datetime.date.today():
                continue

            tk.Checkbutton(
                self.__listings_box, variable=self.__item, text=listing, onvalue=listing.get_listing_id(), offvalue=None).pack()

        self.__login_button = tk.Button(self.__app.body_frame, text='select listing', bg='#DD2424', fg='#000000', font=("Arial", 18),
                                        command=lambda: self.update_listing_details(self.__item.get(), self.__city_choice.get(), self.get_id(self.__cinema_choice.get())))

        self.__login_button.place(x=612, y=460)

        self.__city_options_lable.place(x=10, y=10)
        self.__city_options.place(x=100, y=10)
        self.__cinema_options_label.place(x=10, y=70)
        self.__cinema_options.place(x=100, y=70)
        self.__date_label.place(x=10, y=210)
        self.__date_entry.place(x=100, y=210)
        self.__listings_label.place(x=10, y=280)
        self.__listings_box.place(x=100, y=280)

    # after they have selected a listing in (update listing) this lets them actually change the listings details
    def update_listing_details(self, listing_id, city, cinema):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Update listings"

        # get cinema, film and date from the paramter listing id
        # already passing through city as its easier
        for listing in self.__controller.get_cities()[city][cinema].get_listings():
            if listing.get_listing_id() == listing_id:
                self.__original_film = listing.get_film()
                self.__original_date = listing.get_date()

        # all inputs are pre filled with the current values of the listing they want to update

        # display current listing details
        self.__orignal_listing_label = tk.Label(
            self.__app.body_frame, text=f'Original Listing Details: City: {city}, Cinema ID: {cinema},Film: {self.__original_film}, Date: {self.__original_date}', font=("Arial", 12))

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
        self.__date_entry = DateEntry(
            self.__app.body_frame, mindate=datetime.date.today())

        # update listing button
        self.__login_button = tk.Button(self.__app.body_frame, text='update listing', bg='#DD2424', fg='#000000', font=("Arial", 18), command=lambda: self.__controller.update_listing(
            self.__city_choice.get(), self.get_id(self.__cinema_choice.get()), listing_id, self.__date_entry.get_date(), self.__film_choice.get()))

        # place buttons
        self.__login_button.place(x=612, y=460)

        self.__film_options_label.place(x=10, y=140)
        self.__film_options.place(x=100, y=140)
        self.__date_label.place(x=10, y=210)
        self.__date_entry.place(x=100, y=210)
        self.__orignal_listing_label.place(x=290, y=100)

    def generate_report(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Generate report"

    def add_new_cinema(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Add new cinema"

        # city
        self.__city_choice = tk.StringVar()
        self.__city_choice.set(list(self.__controller.get_cities().keys())[0])
        self.__city_options_lable = tk.Label(
            self.__app.body_frame, text="choose city: ")
        self.__city_options = tk.OptionMenu(
            self.__app.body_frame, self.__city_choice, *self.__controller.get_cities().keys())  # , command=self.set_cinema(self.__city_choice.get()))

        self.__cinema_address_lable = tk.Label(
            self.__app.body_frame, text="Cinema address: ")
        self.__cinema_address = tk.Entry(self.__app.body_frame)

        self.__number_of_screens_lable = tk.Label(
            self.__app.body_frame, text="Number of screens: ")
        self.__number_of_screens = tk.Entry(self.__app.body_frame)

        self.__login_button = tk.Button(self.__app.body_frame, text='Add cinema', bg='#DD2424', fg='#000000', font=("Arial", 18), command=lambda: self.__controller.add_cinema(
            self.__city_choice.get(), self.__cinema_address.get(), int(self.__number_of_screens.get())))
        self.__login_button.place(x=612, y=460)

        self.__city_options_lable.place(x=10, y=10)
        self.__city_options.place(x=100, y=10)
        self.__cinema_address_lable.place(x=10, y=70)
        self.__cinema_address.place(x=100, y=70)
        self.__number_of_screens_lable.place(x=10, y=140)
        self.__number_of_screens.place(x=100, y=140)

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

        self.__city_name_lable.place(x=10, y=10)
        self.__city_name.place(x=100, y=10)
        self.__city_morning_price_lable.place(x=10, y=70)
        self.__city_morning_price.place(x=100, y=70)
        self.__city_afternoon_price_lable.place(x=10, y=140)
        self.__city_afternoon_price.place(x=100, y=140)
        self.__city_evening_price_lable.place(x=10, y=210)
        self.__city_evening_price.place(x=100, y=210)

    def get_id(self, string):
        return int(re.search(r'\d+', string).group())
