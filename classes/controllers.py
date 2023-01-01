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

    def get_bookings_as_list(self):
        return self.__model.get_bookings_as_list()

    def get_all_bookings_as_list(self):
        return self.__model.get_all_bookings_as_list()

    def get_all_listings_as_list(self):
        return self.__model.get_all_listings_as_list()

    def max_shows(self):
        return self.__model.max_shows()

    def add_city(self, name, morning_price, afternoon_price, evening_price):
        self.__model.add_city(name, morning_price,
                              afternoon_price, evening_price)

    def add_cinema(self, address, number_of_screens):
        self.__model.add_cinema(address, number_of_screens)

    def remove_listing(self, listings):
        self.__model.remove_listing(listings)

    def add_listing(self, film):
        self.__model.add_listing(film)

    def update_listing(self, film):
        self.__model.update_listing(film)

    def get_films(self):
        return self.__model.get_films()

    def validate_booking(self, seat_type, num_of_tickets):
        ret = self.__model.validate_booking(seat_type, num_of_tickets)
        if ret == -1:
            self.__view.show_error("no seat type selected")
        elif (ret == 0):
            self.__view.show_error("no available seats")
        else:
            self.__view.show_info("seats available")
            self.__view.book_now(
                ret.as_list(), ret.get_ticket(), ret.get_receipt())

    def add_booking(self, customer_name, customer_email, customer_phone, name_on_card, card_number, cvv, expiry_date):
        return self.__model.add_booking(customer_name, customer_email, customer_phone, name_on_card, card_number, cvv, expiry_date)

    def get_cinema_city(self):
        return self.__model.get_cinema_city()

    def cancel_booking(self, booking_reference, customer_email, name_on_card, card_number, cvv, expiry_date):
        match (self.__model.cancel_booking(booking_reference, customer_email, name_on_card, card_number, cvv, expiry_date)):
            case -2:
                self.__model.show_error("Unable to cancel, show is tomorrow")
            case -1:
                self.__model.show_error("")
            case 0:
                self.__model.show_error("")

    def add_show(self, time):
        if not self.__model.add_show(time):
            self.__view.show_error("no available screens")

    def get_booking(self, booking_ref):
        return self.__model.get_booking(booking_ref)

    def get_booking_roh_tree(self, booking_ref):
        return self.__model.get_booking_roh_tree(booking_ref)

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
