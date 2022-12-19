import tkinter as tk
import tkinter.messagebox
from tkcalendar import DateEntry
from datetime import datetime, date
from admin import Admin
from manager import Manager
from dbfunc import conn
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
        self.__back_to_dashboard.place(x=1000, y=600)
        self.__app.page_label["text"] = "View booking"
        if (isinstance(self.__user, Admin)):
            pass
        else:
            self.__controller.get_bookings(self.__user.get_branch())


    def update_films_and_shows_based_on_date(self,*args):
        
        #Clearing both options
        menu = self.film_options["menu"]
        menu.delete(0, "end")
        menu2 = self.show_options["menu"]
        menu2.delete(0, "end")        
        self.film_choice.set('')
        self.show_choice.set('')


        self.__film_list_titles_update = []
        #For every listing in the selected cinema on the date chosen, add it to an array
        for listing_on_date in self.__controller.get_cities()[self.cinema_choice.get()].get_cinemas()[0].get_listings():
            temp_date = str(self.selected_date.get())
            temp_date = temp_date.replace("/","-")
            if temp_date == str(listing_on_date.get_date()): 
                self.__film_list_titles_update.append(str(listing_on_date.get_film()))
        


        #If there are listings airing at the cinema on the date then
        if len(self.__film_list_titles_update) > 0:
            #Placing film titles into optionsmenu
            # for film_title in self.__film_list_titles_update:
            #     self.film_choice.set(film_title)
            #     # menu.add_command(label=film_title,command=self.update_shows_based_on_film) #Command doesn't work to set the actual value. It still works without the i.
            #     menu.add_command(label=film_title, command=lambda value=film_title: self.film_choice.set(value)) #Command doesn't work to set the actual value. It still works without the i.
            
            #Hardcoded way just replacing the widget with a new one.
            #The code above works, the only problem is that the command attached to film_options to update the show_options gets removed when we change the date. e.g. load page --> change date --> 2 films airing --> click other film --> [Doesn't display showings for newly clicked film, still showing previous film showings]
            #But if we, load page --> dont change date --> change film, it works

            #Add all the choices to film options
            self.film_choice.set(self.__film_list_titles_update[0])
            self.film_options.destroy()
            self.film_options = tk.OptionMenu(self.__app.body_frame, self.film_choice, *self.__film_list_titles_update, command=self.update_shows_based_on_film)
            self.film_options.place(x=100, y=150)


            #Shows
            #Gets the shows for film listing selected. It puts it into a list size of 1. e.g. len(show_times_list_object) = 1. len(show_times_list_object[0]) = 4 because 4 shows for the listing
            film_title = self.film_choice.get() #Gets film selected
            self.show_times_list_object = []
            #For every listing in the cinema
            for listing_on_date in (self.__controller.get_cities()[self.cinema_choice.get()].get_cinemas()[0].get_listings()):
                temp_date = str(self.selected_date.get())
                temp_date = temp_date.replace("/","-")
                #If the listings date is the same as date selected
                if temp_date == str(listing_on_date.get_date()):  
                    #If the listings date is the same as date selected AND the listings title is equal to the one chosen            
                    if str(film_title) == str(listing_on_date.get_film()): 
                        self.show_times_list_object.append(listing_on_date.get_shows()) #Gets list of show times for selected film (the time because __str__ returns time)
            
                        #Retrieving the values from the objects (times) and putting it into a list to pass to OptionsMenu
                        self.show_times_list = []
                        for i in range (len(self.show_times_list_object[0])):
                            self.show_times_list.append(str(self.show_times_list_object[0][i]))
                        
                        #Outputting the shows into optionsmenu
                        for show_time in self.show_times_list:
                            self.show_choice.set(show_time)
                            menu2.add_command(label=show_time, command=lambda value=show_time: self.show_choice.set(value))
                
            print(self.show_times_list)

        else:
            print("no films airing today") #Debug

    
    def update_shows_based_on_film(self,film_title):
        print("poo")
        #Does the same as the code above. Just updating show options when a different film is selected.
        menu = self.show_options["menu"]
        menu.delete(0, "end")
        film_title = self.film_choice.get()
        self.show_choice.set('')
        self.show_times_list_object = []
        #For every listing in the cinema
        for listing_on_date in (self.__controller.get_cities()[self.cinema_choice.get()].get_cinemas()[0].get_listings()):
            temp_date = str(self.selected_date.get())
            temp_date = temp_date.replace("/","-")
            #If the listings date is the same as date selected
            if temp_date == str(listing_on_date.get_date()):  
                #If the listings date is the same as date selected AND the listings title is equal to the one chosen  
                if str(film_title) == str(listing_on_date.get_film()): 
                    self.show_times_list_object.append(listing_on_date.get_shows()) #Gets list of show times for selected film (the time because __str__ returns time)
                
                    #Retrieving the values from the objects (times) and putting it into a list to pass to OptionsMenu
                    self.show_times_list = []
                    for i in range (len(self.show_times_list_object[0])):
                        self.show_times_list.append(str(self.show_times_list_object[0][i]))
                        
                    for show_time in self.show_times_list:
                        self.show_choice.set(show_time)
                        menu.add_command(label=show_time, command=lambda value=show_time: self.show_choice.set(value))    



    def create_booking(self):


        #When we change cinema option value --> update_films_and_shows_based_on_date. (Because we fill in the rest of paramaeters using city chosen)
        #When we change date value --> update_films_and_shows_based_on_date (We fetch all listings showing at a specific day at the cinema)
        #When we change a film value -->  update_shows_based_on_film (We fetch all showing times for the listing)
        #When we chang ea show --> Nothing

        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1000, y=600)
        self.__app.page_label["text"] = "Create booking"

        #Hardcoded cities for dynamic - will look at it later
        if (isinstance(self.__user, Admin)):
            self.__select_cinema_label = tk.Label(self.__app.body_frame, text="Select Cinema").place(x=0,y=50)
            self.cinema_list = ["Bristol","Birmingham","Cardiff","London"]
            self.cinema_choice = tk.StringVar()
            self.cinema_choice.set(self.cinema_list[0])
            self.cinema_options = tk.OptionMenu(self.__app.body_frame, self.cinema_choice, *self.cinema_list, command=self.update_films_and_shows_based_on_date) #Command doesnt work if we change date then change film.
            self.cinema_options.place(x=100,y=50)
        else:
            self.cinema_choice = tk.StringVar()
            self.cinema_choice.set("Bristol")

        #Standard labels
        self.__date_label = tk.Label(self.__app.body_frame, text="Select Date").place(x=0,y=100)
        self.__select_film_label = tk.Label(self.__app.body_frame, text="Select Film").place(x=0, y=150)
        self.__select_show_label = tk.Label(self.__app.body_frame, text="Select Show").place(x=0, y=200)

        #Date
        self.selected_date=tk.StringVar()
        self.__date_today = datetime.now()
        self.__date_entry = DateEntry(self.__app.body_frame,date_pattern='y/mm/dd', mindate=self.__date_today,textvariable=self.selected_date)
        self.selected_date.trace('w',self.update_films_and_shows_based_on_date) #Event listener

        #Films - Gets all listing titles (film titles) based on the date selected. Only here for first loadup of page, as after the first load whenever date is changed it goes to function
        self.film_choice = tk.StringVar()
        self.film_choice.set('')         
        self.film_list_titles = ['']

        #For every listing in the cinema
        for listing_on_date in self.__controller.get_cities()[self.cinema_choice.get()].get_cinemas()[0].get_listings():
            temp_date = str(self.selected_date.get())
            temp_date = temp_date.replace("/","-")
            #If the listings date is the same as date selected -> Add it to array for options menu
            if temp_date == str(listing_on_date.get_date()):
                self.film_list_titles.append(str(listing_on_date.get_film()))

        #Formatting crap -ignore
        try:
            self.film_choice.set(self.film_list_titles[1])
            self.film_list_titles.pop(0)
        except: 
            pass
        
        self.film_options = tk.OptionMenu(self.__app.body_frame, self.film_choice, *self.film_list_titles, command=self.update_shows_based_on_film) #Command doesnt work if we change date then change film, only works first time loaded thats why i hardcoded destroy widget in the update_film_and_show function.
        

        #Shows

        self.show_times_list = ['']
        film_title = self.film_choice.get()
        self.show_times_list_object = []
        
        #For every listing in the cinema
        for listing_on_date in (self.__controller.get_cities()[self.cinema_choice.get()].get_cinemas()[0].get_listings()):
            temp_date = str(self.selected_date.get())
            temp_date = temp_date.replace("/","-")
            #If the listings date is the same as date selected
            if temp_date == str(listing_on_date.get_date()):  
                #If the listings date is the same as date selected AND the listings title is equal to the one chosen  
                if str(film_title) == str(listing_on_date.get_film()): 
                    self.show_times_list_object.append(listing_on_date.get_shows())

                    for i in range (len(self.show_times_list_object[0])):
                        self.show_times_list.append(str(self.show_times_list_object[0][i]))
                    
                    self.show_times_list.pop(0)
                

        self.show_choice = tk.StringVar()
        self.show_choice.set('') 
        self.show_choice.set(self.show_times_list[0])
        self.show_options = tk.OptionMenu(self.__app.body_frame, self.show_choice, *self.show_times_list)




        self.__date_entry.place(x=100,y=100)
        self.film_options.place(x=100, y=150)
        self.show_options.place(x=100, y=200)


    def view_film_listings(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1000, y=600)
        self.__app.page_label["text"] = "View film listings"

    def cancel_booking(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1000, y=600)
        self.__app.page_label["text"] = "Cancel booking"

    def update_cinemas(self, city):
        menu = self.__cinema_options["menu"]
        menu.delete(0, "end")
        self.__cinema_choice.set(
            self.__controller.get_cities()[city].get_cinemas()[0])
        for cinema in self.__controller.get_cities()[city].get_cinemas():
            menu.add_command(
                label=cinema, command=lambda value=cinema: self.__cinema_choice.set(value))

        self.clear_frame(self.__screens_box)
        for screen in self.__controller.get_cities()[city].get_cinemas()[0].get_screens():
            l = tk.Checkbutton(
                self.__screens_box, text=screen).pack(sid=tk.BOTTOM)

    def add_listing(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1000, y=600)
        self.__app.page_label["text"] = "Add listings"

        # city
        self.__city_choice = tk.StringVar()
        self.__city_choice.set(list(self.__controller.get_cities().keys())[0])
        self.__city_options_lable = tk.Label(
            self.__app.body_frame, text="choose city: ")
        self.__city_options = tk.OptionMenu(
            self.__app.body_frame, self.__city_choice, *self.__controller.get_cities().keys(), command=self.update_cinemas)  # , command=self.set_cinema(self.__city_choice.get()))

        # cinema
        self.__cinema = self.__controller.get_cities()[self.__city_choice.get()].get_cinemas()[
        0]
        self.__cinema_choice = tk.StringVar()
        self.__cinema_choice.set(self.__cinema)
        self.__cinema_options_label = tk.Label(
            self.__app.body_frame, text="choose cinema: ")
        self.__cinema_options = tk.OptionMenu(
            self.__app.body_frame, self.__cinema_choice, *self.__controller.get_cities()[self.__city_choice.get()].get_cinemas())

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
            self.__app.body_frame, mindate=datetime.now())

        # screens
        self.__screens_label = tk.Label(
            self.__app.body_frame, text="Select screens: ")
        self.__screens_box = tk.Frame(self.__app.body_frame)
        for screen in self.__controller.get_cities()[self.__city_choice.get()].get_cinemas()[0].get_screens():
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
        self.__back_to_dashboard.place(x=1000, y=600)
        self.__app.page_label["text"] = "Remove listings"

    def update_listing(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1000, y=600)
        self.__app.page_label["text"] = "Update listings"

    def generate_report(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1000, y=600)
        self.__app.page_label["text"] = "Generate report"

    def add_new_cinema(self):
        self.clear_frame(self.__app.body_frame)
        self.__back_to_dashboard.place(x=1000, y=600)
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
        self.__back_to_dashboard.place(x=1000, y=600)
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
