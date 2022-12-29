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

    def get_bookings_as_list(self, show):
        return self.__model.get_bookings_as_list(show)

    def add_city(self, name, morning_price, afternoon_price, evening_price):
        self.__model.add_city(name, morning_price,
                              afternoon_price, evening_price)

    def add_cinema(self, city, address, number_of_screens):
        self.__model.add_cinema(city, address, number_of_screens)

    def remove_listing(self, city, cinema, listings):
        self.__model.remove_listing(city, cinema, listings)

    def add_listing(self, date, film, city, cinema):
        self.__model.add_listing(date, film, city, cinema)

    def update_listing(self, city, cinema_id, listing_id, date, film):
        self.__model.update_listing(city, cinema_id, listing_id, date, film)

    def get_cities(self):
        return self.__model.get_cities()

    def get_city(self, name=None):
        return self.__model.get_city(name)

    def get_films(self):
        return self.__model.get_films()

    def add_booking(self, city, show, seat_type, num_of_tickets):
        seat_availability = False

        # For every listing in the cinema
        if seat_type == "lower":
            print(show.get_available_lower_seats(), num_of_tickets)
            seat_availability = show.get_available_lower_seats() >= num_of_tickets
        elif seat_type == "upper":
            print(show.get_available_upper_seats(), num_of_tickets)
            seat_availability = show.get_available_upper_seats() >= num_of_tickets
        elif seat_type == "vip":
            print(show.get_available_vip_seats(), num_of_tickets)
            seat_availability = show.get_available_vip_seats() >= num_of_tickets
        else:
            self.__view.show_error("no seat type selected")

        if (not seat_availability):
            self.__view.show_error("no available seats")
            return

        print("available seats")

        self.__model.add_booking(city, show, seat_type,
                                 num_of_tickets, "poop@gmail.com")

    def get_cinema_city(self, cinema):
        return self.__model.get_cinema_city(cinema)

    def cancel_booking(self, booking_reference, show):
        self.__model.cancel_booking(booking_reference, show)

    def add_show(self, listing_id, cinema, time):
        if not self.__model.add_show(listing_id, cinema, time):
            self.__view.show_error("no available screens")

    def get_booking(self, booking_ref):
        return self.__model.get_booking(booking_ref)
