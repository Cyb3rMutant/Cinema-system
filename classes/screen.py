from seat import Seat
from show import Show


class Screen():
    def __init__(self, screen_number: int, shows: list):

        self.__screen_number = screen_number

        self.__seats = dict()

        self.__shows = shows

    def get_screen_number(self):
        return self.__screen_number

    def get_seats(self):
        return self.__seats

    def get_shows(self):
        return self.__shows
