class Controller():
    def __init__(self):
        self.__model = None
        self.__view = None

    def set_model(self, model):
        self.__model = model

    def set_view(self, view):
        self.__view = view

    def login(self, username, password):
        user = self.__model.validate_login(username, password)
        if (user == -1):
            self.__view.show_error("User doesnt exist.")

        elif (user == 0):
            self.__view.show_error("Incorrect username or password.")

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
        match(self.__model.add_city(name, morning_price,afternoon_price, evening_price)):
            case 1:
                self.__view.show_info("Successfully added city.")
                self.__view.dashboard()
            case 0:
                self.__view.show_error("Enter numerical values for city prices.")


    def add_film(self, film_title, film_rating, film_genre, film_year, film_age_rating, film_duration, film_description, film_cast):
        match(self.__model.add_film(film_title, film_rating, film_genre, film_year, film_age_rating, film_duration, film_description, film_cast)):
            case 1:
                self.__view.show_info("Successfully Added Film.")
                self.__view.dashboard()
            case 0:
                self.__view.show_error("Please enter valid rating(1-10), year(1800-2023) & duration(20-400).")
            case -1:
                self.__view.show_error("Please enter a rating between 1-10.")
            case -2:
                self.__view.show_error("Please enter valid year parameters.")
            case -3:
                self.__view.show_error("Please enter a film duration between 20 & 400 minutes.")
    def add_cinema(self, address, number_of_screens):
        match(self.__model.add_cinema(address, number_of_screens)):
            case 1:
                self.__view.show_info("Successfully Added Cinema.")
                self.__view.dashboard()
            case 0:
                self.__view.show_error("Please enter an integer between 1-6.")
    def remove_listing(self,cinema):
        if cinema == "choose cinema": self.__view.show_error("Choose a cinema."); return #quickfix for the choose cinema problem. (we do need this or an alternative)
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
        if cinema == "choose cinema":
            self.__view.show_error("Choose a cinema.")
            return
        match(self.__model.add_listing(film)):
            case 1:
                self.__view.show_info("Successfully Added Listing.")
                self.__view.dashboard() 
        

    def update_listing(self, film):

        match(self.__model.update_listing(film)):
            case 1:
                self.__view.show_info("Successfully updated listing")

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
            self.__view.book_now(
                ret.as_list(), ret.get_ticket(), ret.get_receipt())

    def add_booking(self, customer_name, customer_email, customer_phone, name_on_card, card_number, cvv, expiry_date):
        match(self.__model.add_booking(customer_name, customer_email, customer_phone, name_on_card, card_number, cvv, expiry_date)):
            case 1:
                self.__view.show_info("Booking Successful.")
                self.__view.dashboard() #Take to receipt or ticket or smth
            case 0:
                self.__view.show_error("Duplicate email.") #Needs to be fixed

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
        if cinema == "choose cinema":
            self.__view.show_error("Choose a cinema.")
            return
        match(self.__model.add_show(time)):
            case 1:
                self.__view.show_info("Successfully Added Show.")
                self.__view.dashboard()
            case 0:
                self.__view.show_error("No available screens.")
            case -1:
                self.__view.show_error("Select a Listing or Cinema.")

    def add_user(self, name, password, user_type,cinema):
        if cinema == "choose cinema":
            self.__view.show_error("Choose a cinema.")
            return
        match(self.__model.add_user(name, password, user_type)):
            case 1:
                self.__view.show_info("Successfully Added User.")
                self.__view.dashboard()


    def get_user_types(self):
        return self.__model.get_user_types()

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

    def get_booking(self, booking_ref):
        return self.__model.get_booking(booking_ref)

    def clear_data(self):
        return self.__model.clear_data()

    def get_cinema_listings_as_list(self):
        return self.__model.get_cinema_listings_as_list()

    def get_shows_for_listing(self, listing_id):
        return self.__model.get_shows_for_listing(listing_id)

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
