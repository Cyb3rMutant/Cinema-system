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
            self.__film_options.destroy()
            self.__show_options.destroy()
            self.__book_now_btn.destroy()
        except:
            pass

        try: #Only got this cus it doesnt work with booking staff causes error crash. KEEP it tho, you can remove comments
            #Debug -> Change city to anything but birmingham and date only. U will see it prints birminghams address when it shouldnt be. the if statement prevents this
            print(f'{type(self.__cinema)} : {self.__cinema}')
            print(f'{type(self.__cinema_choice.get())} : {self.__cinema_choice.get()}')
            
            #Added this because when we load create_booking -> change city to Bristol -> change date to any date -> the above debug will print birminghams cinema info -> change date to birmingham listing date -> film and show options will update with birminghams and not bristols
            #And cinema_choice will still be "choose cinema" whilst it prints birminghams listings in city_choice bristol
            if str(self.__cinema_choice.get()) == "choose cinema":
                print('error: choose cinema is selected, wont update film')
                return 0 
        except:
            pass
        #Main. All above is just format
        self.__listings = []
        # For every listing in the cinema
        for l in self.__cinema.get_listings():
            #If date selected = listings date -> add it to array for optionsmenu
            if str(self.selected_date.get()) == str(l.get_date()):
                self.__listings.append(l)

        if not self.__listings:
            print("no shows airing today")
            return 0
        # Command doesnt work if we change date then change film, only works first time loaded thats why i hardcoded destroy widget in the update_film_and_show function.
        self.__film_choice = tk.StringVar()
        self.__film_choice.set(self.__listings[0])
        self.__film_options = tk.OptionMenu(
            self.__app.body_frame, self.__film_choice, *self.__listings, command=self.update_shows)

        # Shows
        self.__show = self.__listings[0].get_shows()[0]
        self.__show_choice = tk.StringVar()
        self.__show_choice.set(self.__show)
        self.__show_options = tk.OptionMenu(
            self.__app.body_frame, self.__show_choice, *self.__listings[0].get_shows(), command=lambda show: [self.set_show(show)])

        self.__book_now_btn = tk.Button(
            self.__app.body_frame, text='Book now', command=lambda: self.__controller.add_booking(str(self.__city_choice.get()), self.__show, str(self.__seat_type_btn.get()), int(self.__num_of_ticket_choice.get())))

        self.__film_options.place(x=100, y=150)
        self.__show_options.place(x=100, y=200)
        self.__book_now_btn.place(x=50, y=350)

    def update_shows(self, listing):
        self.__show_options.destroy()
        self.__show = listing.get_shows()[0]
        self.__show_choice = tk.StringVar()
        self.__show_choice.set(self.__show) #Instead of "choose show". If we choose city, cinema, date, film AND show is still equal to "choose show", we can still book which it shouldnt. This prevents this by automatically updating shows to the times instead of it.
        self.__show_options = tk.OptionMenu(self.__app.body_frame, self.__show_choice,
                                            *listing.get_shows(), command=lambda show: [self.set_show(show)])
        self.__show_options.place(x=100, y=200)

    def create_booking(self):

        # When we change cinema option value --> update_films_and_shows_based_on_date. (Because we fill in the rest of paramaeters using city chosen)
        # When we change date value --> update_films_and_shows_based_on_date (We fetch all listings showing at a specific day at the cinema)
        # When we change a film value -->  update_shows (We fetch all showing times for the listing)
        # When we chang ea show --> Nothing

        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Create booking"

        if (isinstance(self.__user, Admin)):
            
            self.__city_options_label = tk.Label(self.__app.body_frame, text="choose city: ").place(x=0, y=50)
            self.__cinema_options_label = tk.Label(self.__app.body_frame, text="choose cinema: ").place(x=300, y=50)


            self.__city_choice = tk.StringVar()
            self.__city_choice.set(list(self.__controller.get_cities().keys())[0])
            self.__city_options = tk.OptionMenu(self.__app.body_frame, self.__city_choice, *self.__controller.get_cities().keys(), 
            command=lambda unused: self.update_cinemas(lambda cinema: [self.set_cinema(cinema), self.update_films_and_shows_based_on_date()]))  # When we change a city, we update its cinemas
            self.__city_options.place(x=100, y=50)

            self.__cinema = self.__controller.get_cities()[self.__city_choice.get()].get_cinemas()[0]
            self.__cinema_choice = tk.StringVar()
            self.__cinema_choice.set("choose cinema")
            self.__cinema_options = tk.OptionMenu(self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cities()[
                                                  self.__city_choice.get()].get_cinemas(), command=lambda cinema: [self.set_cinema(cinema), self.update_films_and_shows_based_on_date()])
            self.__cinema_options.place(x=400, y=50)


        else:
            self.__cinema = self.__user.get_branch()
            self.__city_choice = self.__controller.get_city(self.__cinema)

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
        self.__date_today = datetime.date.today()
        self.selected_date = tk.StringVar()
        self.__date_entry = DateEntry(self.__app.body_frame,date_pattern='y-mm-dd', mindate=self.__date_today, textvariable=self.selected_date)
        self.selected_date.trace('w',self.update_films_and_shows_based_on_date)


        self.__seat_type_btn = tk.StringVar()
        self.__lower_hall = tk.Radiobutton(self.__app.body_frame, text="lower", value="lower",
                                           variable=self.__seat_type_btn, tristatevalue=0)
        self.__upper_hall = tk.Radiobutton(self.__app.body_frame, text="upper", value="upper",
                                           variable=self.__seat_type_btn, tristatevalue=0)
        self.__vip_hall = tk.Radiobutton(self.__app.body_frame, text="vip", value="vip",
                                         variable=self.__seat_type_btn, tristatevalue=0)

        self.num_of_tickets_list = [1, 2, 3, 4, 5]
        self.__num_of_ticket_choice = tk.IntVar()
        self.__num_of_ticket_choice.set(self.num_of_tickets_list[0])
        self.__num_of_ticket_options = tk.OptionMenu(
            self.__app.body_frame, self.__num_of_ticket_choice, *self.num_of_tickets_list)

        self.__date_entry.place(x=100, y=100)
        self.__lower_hall.place(x=100, y=250)
        self.__upper_hall.place(x=220, y=250)
        self.__vip_hall.place(x=340, y=250)
        self.__num_of_ticket_options.place(x=100, y=300)

        # Films - Gets all listing titles (film titles) based on the date selected. Only here for first loadup of page, as after the first load whenever date is changed it goes to function
        self.__listings = []
        # For every listing in the cinema
        for l in self.__cinema.get_listings():
            # If the listings date is the same as date selected -> Add it to array for options menu
            # if str(self.__film_choice.get()) != l.get_film().get_title():
            #     continue
            if self.__date_entry.get_date() != l.get_date():
                continue

            self.__listings.append(l)
        if not self.__listings:
            self.__listings
            return 0

        # Command doesnt work if we change date then change film, only works first time loaded thats why i hardcoded destroy widget in the update_film_and_show function.
        self.__film_choice = tk.StringVar()
        self.__film_choice.set(self.__listings[0])
        self.__film_options = tk.OptionMenu(
            self.__app.body_frame, self.__film_choice, *self.__listings, command=self.update_shows)

        # Shows
        self.__show = self.__listings[0].get_shows()[0]
        self.__show_choice = tk.StringVar()
        self.__show_choice.set(self.__show)
        self.__show_options = tk.OptionMenu(
            self.__app.body_frame, self.__show_choice, *self.__listings[0].get_shows(), command=lambda show: [self.set_show(show)])

        # Ticket type & Number of tickets entry
        self.__book_now_btn = tk.Button(
            self.__app.body_frame, text='Book now', command=lambda: self.__controller.add_booking(str(self.__city_choice.get()), self.__show, str(self.__seat_type_btn.get()), int(self.__num_of_ticket_choice.get())))

        # Placing interactive widgets
        self.__film_options.place(x=100, y=150)
        self.__show_options.place(x=100, y=200)
        self.__book_now_btn.place(x=50, y=350)


        
    def update_cinemas(self, func):
        try:
            #Anytime we update city, these should be removed
            self.__film_options.destroy()
            self.__show_options.destroy()
            self.__book_now_btn.destroy()
        except:
            pass
        self.__cinema_choice.set("choose cinema")
        self.__cinema_options.destroy()
        self.__cinema_options = tk.OptionMenu(
            self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cities()[self.__city_choice.get()].get_cinemas(), command=func)
        self.__cinema_options.place(x=400, y=50)



    def view_film_listings(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "View film listings"

    def cancel_booking(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1030, y=130)
        self.__app.page_label["text"] = "Cancel booking"


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

    def set_show(self, show):
        self.__show = show

    def set_cinema(self, cinema):
        self.__cinema = cinema
