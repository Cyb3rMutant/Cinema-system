from datetime import datetime
from film import Film


class Show():
    def __init__(self, show_number: int, time: datetime, seats_available_vip: int, seats_available_upper: int, seats_available_lower: int, film: Film):
        self.__show_number = show_number

        self.__time = time

        self.__seats_available_vip = seats_available_vip

        self.__seats_available_upper = seats_available_upper

        self.__seats_available_lower = seats_available_lower

        self.__film = film

    def get_show_number(self):
        return self.__show_number

    def get_time(self):
        return self.__time

    def get_seats_available_vip(self):
        return self.__seats_available_vip

    def get_seats_available_lower(self):
        return self.__seats_available_upper

    def get_seats_available_lower(self):
        return self.__seats_available_lower

    def get_film(self):
        return self.__film
