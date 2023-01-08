"""
Authors:
    Rohaan Aslam (21017718)
    Benjamin Hussey (21022768)
    Yazeed Abu-Hummous (21014295)
Date: 08/01/2023
Module: Advanced Software Development 22/23
"""
class Controller():
    def __init__(self):
        self.__model = None
        self.__view = None

    def set_model(self, model):
        self.__model = model

    def set_view(self, view):
        self.__view = view

    def login(self, user_id, password):
        user = self.__model.validate_login(user_id, password)
        if (user == -1):
            self.__view.show_error("User doesnt exist.")

        elif (user == 0):
            self.__view.show_error("Incorrect user_id or password.")

        else:
            self.__view.show_info("You have successfully logged in.")

            self.__view.logged_in(user)

    def logout(self):
        self.__view.login()
        self.__model.logout()

    def get_bookings_as_list(self):
        return self.__model.get_bookings_as_list()

    def get_all_bookings_as_list(self):
        return self.__model.get_all_bookings_as_list()

    def add_city(self, name, morning_price, afternoon_price, evening_price):
        match(self.__model.add_city(name, morning_price, afternoon_price, evening_price)):
            case 1:
                self.__view.show_info("Successfully added city.")
                self.__view.dashboard()
            case 0:
                self.__view.show_error(
                    "Enter numerical values for city prices.")

    def add_film(self, film_title, film_rating, film_genre, film_year, film_age_rating, film_duration, film_description, film_cast):
        match(self.__model.add_film(film_title, film_rating, film_genre, film_year, film_age_rating, film_duration, film_description, film_cast)):
            case 1:
                self.__view.show_info("Successfully Added Film.")
                self.__view.dashboard()
            case 0:
                self.__view.show_error(
                    "Please enter valid rating(1-10), year(1800-2023) & duration(20-400).")
            case -1:
                self.__view.show_error("Please enter a rating between 1-10.")
            case -2:
                self.__view.show_error("Please enter valid year parameters.")
            case -3:
                self.__view.show_error(
                    "Please enter a film duration between 20 & 400 minutes.")
            case -4:
                self.__view.show_error("This film already_exists")

    def add_cinema(self, address, number_of_screens):
        match(self.__model.add_cinema(address, number_of_screens)):
            case 1:
                self.__view.show_info("Successfully Added Cinema.")
                self.__view.dashboard()
            case 0:
                self.__view.show_error("Please enter an integer between 1-6.")

    def remove_listing(self, cinema):
        match(self.__model.remove_listing()):
            case 1:
                self.__view.show_info("Successfully Removed Listing")
                self.__view.dashboard()
            case 0:
                self.__view.show_error("No Listing Selected")

    def remove_show(self):
        match(self.__model.remove_show()):
            case 1:
                self.__view.show_info("Successfully Removed Show.")
                self.__view.dashboard()
            case 0:
                self.__view.show_error("No Show Selected.")

    def add_listing(self, film, cinema):
        match(self.__model.add_listing(film)):
            case 1:
                self.__view.show_info("Successfully Added Listing.")
                self.__view.dashboard()

    def update_listing(self, film):
        match(self.__model.update_listing(film)):
            case 1:
                self.__view.show_info("Successfully updated listing")
                self.__view.dashboard()

    def listing_number_of_bookings(self, start, end):
        try:
            if start < end:
                self.__view.report_tree(
                    self.__model.listing_number_of_bookings(start, end))
            else:
                self.__view.show_error("Start-date has to be before end-date!")
        except IndexError:
            self.__view.show_error("no bookings")

    def cinema_revenue(self, start, end):
        try:
            if start < end:
                self.__view.report_tree(self.__model.cinema_revenue(start, end))
            else:
                self.__view.show_error("Start-date has to be before end-date!")
        except IndexError:
            self.__view.show_error("no bookings")

    def film_revenue(self,):
        try:
            self.__view.report_tree(self.__model.film_revenue())
        except IndexError:
            self.__view.show_error("no films")

    def staff_number_of_bookings(self, start, end):
        try:
            if start < end:
                self.__view.report_tree(
                    self.__model.staff_number_of_bookings(start, end))
            else:
                self.__view.show_error("Start-date has to be before end-date!")
        except IndexError:
            self.__view.show_error("no staff members")

    def get_films(self):
        return self.__model.get_films()

    def validate_booking(self, seat_type, num_of_tickets):
        ret = self.__model.validate_booking(seat_type, num_of_tickets)
        if ret == -2:
            self.__view.show_error("No show selected.")
        elif ret == -1:
            self.__view.show_error("No seat type selected.")
        elif (ret == 0):
            self.__view.show_error("No available seats.")
        else:
            self.__view.show_info("Seats available.")
            self.__view.book_now(ret)

    def add_booking(self, customer_name, customer_email, customer_phone, name_on_card, card_number, cvv, expiry_date):
        if self.__model.check_customer(customer_email):
            self.__view.askquestion(
                "customer email exists, do you want to update data")
        else:
            self.__model.add_customer(
                customer_name, customer_email, customer_phone, card_number)

        self.__model.add_booking(
            customer_email, name_on_card, card_number, cvv, expiry_date)
        self.__view.show_info("Booking Successful.")
        self.__view.dashboard()  # Take to receipt or ticket or smth

    def update_customer(self, customer_name, customer_email, customer_phone, card_number):
        self.__model.update_customer(
            customer_name, customer_email, customer_phone, card_number)

    def get_cinema_city(self):
        return self.__model.get_cinema_city()

    def cancel_booking(self, booking_reference, customer_email, name_on_card, card_number, cvv, expiry_date):
        match (self.__model.cancel_booking(booking_reference, customer_email, name_on_card, card_number, cvv, expiry_date)):
            case -2:
                self.__view.show_error("Unable to cancel, show is tomorrow.")
            case -1:
                self.__view.show_error("E-mail does not match any records.")
            case 0:
                self.__view.show_error("Card info is incorrect.")
            case _:
                self.__view.show_info("Booking successfully cancelled.")
                self.__view.dashboard()

    def add_show(self, time, cinema):
        match(self.__model.add_show(time)):
            case 1:
                self.__view.show_info("Successfully Added Show.")
                self.__view.dashboard()
            case 0:
                self.__view.show_error("No available screens.")
            case -1:
                self.__view.show_error("Select a Listing or Cinema.")

    def add_user(self, name, password, user_type, cinema):
        if len(password) < 5:
            self.__view.show_error("Password must be atleast 5 characters long")
            return
        if len(name) < 5:
            self.__view.show_error("Username must be atleast 5 characters long")
            return
        match(data:=self.__model.add_user(name, password, user_type)):
            case _:
                self.__view.show_info(f"Successfully Added User.\nUser_ID = {data}")
                self.__view.dashboard()

    def get_user_types(self):
        return self.__model.get_user_types()

    def get_booking(self, booking_ref):
        booking = self.__model.get_booking(booking_ref)
        if booking:
            return booking
        else:
            self.__view.show_error("booking not found")
            return []

    def clear_data(self):
        return self.__model.clear_data()

    def get_cinema_listings_as_list(self):
        return self.__model.get_cinema_listings_as_list()

    def get_shows_for_listing(self, listing_id):
        return self.__model.get_shows_for_listing(listing_id)

    def get_cities(self):
        return self.__model.get_cities()

    def get_city(self, name=None):
        return self.__model.get_city(name)

    def get_cinemas(self):
        return self.__model.get_cinemas()

    def get_cinema(self, id=None):
        return self.__model.get_cinema(id)

    def get_listings(self):
        return self.__model.get_listings()

    def get_listing(self, id=None):
        return self.__model.get_listing(id)

    def get_shows(self):
        return self.__model.get_shows()

    def get_show(self, id=None):
        return self.__model.get_show(id)

    def set_city(self, city):
        return self.__model.set_city(city)

    def set_cinema(self, cinema):
        return self.__model.set_cinema(cinema)

    def set_listing(self, listing):
        return self.__model.set_listing(listing)

    def set_show(self, show):
        return self.__model.set_show(show)

    def set_date(self, date):
        return self.__model.set_date(date)
