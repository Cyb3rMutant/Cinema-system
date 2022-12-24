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

    def get_bookings(self, cinema, booking_staff=1):
        if booking_staff:
            return self.__model.get_bookings(self, cinema)

        else:
            return

    def add_city(self, name, morning_price, afternoon_price, evening_price):
        print(type(name), type(morning_price), type(
            afternoon_price), type(evening_price))
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

    def get_films(self):
        return self.__model.get_films()

    def add_booking(self, city, show, seat_type, num_of_tickets):
        seat_availability = False

        # For every listing in the cinema

        if seat_type == "lower":
            seat_availability = show.get_available_lower_seats() > num_of_tickets
        elif seat_type == "upper":
            seat_availability = show.get_available_upper_seats() > num_of_tickets
        elif seat_type == "vip":
            seat_availability = show.get_available_vip_seats() > num_of_tickets

        if (not seat_availability):
            self.__view.show_error("no available seats")
            return

        print("available seats")
        # Now there are seats available for the show, check price
        # Price --> Dependant on SHIW TIME and CITY and TICKET TYPE

        # Generate price of ticket
        # 12:00:00 turned to 120000

        # Generate random booking reference

        self.__model.add_booking(city, show, seat_type,
                                 num_of_tickets, "poop@gmail.com")

    def get_city(self, cinema):
        return self.__model.get_city(cinema)
