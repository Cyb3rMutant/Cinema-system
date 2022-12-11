import booking
import booking_factory
import film
import film_container


class Show(object):
    # ˅

    # ˄

    def __init__(self, show_id, time, available_vip_seats, available_upper_seats, available_lower_seats, screen, listing):

        self.__show_id = show_id

        self.__time = time

        self.__available_vip_seats = available_vip_seats

        self.__available_upper_seats = available_upper_seats

        self.__available_lower_seats = available_lower_seats

        self.__bookings = list()

        self.__screen = screen

        self.__listing = listing

    def get_show_id(self):
        return self.__show_id

    def get_time(self):
        return self.__time

    def get_available_vip_seats(self):
        return self.__available_vip_seats

    def get_available_upper_seats(self):
        return self.__available_upper_seats

    def get_available_lower_seats(self):
        return self.__available_lower_seats

    def get_film(self):
        return self.__film

    def get_bookings(self):
        return self.__bookings

    def get_screen(self):
        return self.__screen

    def get_listing(self):
        return self.__listing

    def set_time(self, time):
        # ˅
        pass
        # ˄

    def add_booking(self, show, number_of_seats, date_of_booking, price, customer):
        # ˅
        pass
        # ˄

    def cancel_booking(self, Booking_reference):
        # ˅
        pass
        # ˄

    # ˅

    # ˄


# ˅

# ˄
