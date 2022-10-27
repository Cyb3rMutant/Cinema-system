from datetime import datetime
from film import Film


class Show():
    def __init__(self, show_number: int, time: datetime, available_vip_seats: int, available_upper_seats: int, available_lower_seats: int, film: Film):
        self.__show_number = show_number

        self.__time = time

        self.__available_vip_seats = available_vip_seats

        self.__available_upper_seats = available_upper_seats

        self.__available_lower_seats = available_lower_seats

        self.__film = film

    def get_show_number(self):
        return self.__show_number

    def get_time(self):
        return self.__time

    def get_available_vip_seats(self):
        return self.__available_vip_seats

    def get_available_lower_seats(self):
        return self.__available_upper_seats

    def get_available_lower_seats(self):
        return self.__available_lower_seats

    def get_film(self):
        return self.__film
