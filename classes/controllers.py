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

    def get_cities(self):
        return self.__model.get_cities()

    def get_films(self):
        return self.__model.get_films()
