"""
Authors:
    Rohaan Aslam (21017718)
    Benjamin Hussey (21022768)
    Yazeed Abu-Hummous (21014295)
Date: 08/01/2023
Module: Advanced Software Development 22/23
"""
import cinema


class City(object):
    def __init__(self, city_name: str, morning_price: int, afternoon_price: int, evening_price: int):

        self.__city_name = city_name

        self.__morning_price = morning_price

        self.__afternoon_price = afternoon_price

        self.__evening_price = evening_price

        self.__cinemas = dict()

    def __getitem__(self, key):
        return self.__cinemas[key]

    def __setitem__(self, key, value):
        self.__cinemas[key] = value

    def get_city_name(self):
        return self.__city_name

    def get_morning_price(self):
        return self.__morning_price

    def get_afternoon_price(self):
        return self.__afternoon_price

    def get_evening_price(self):
        return self.__evening_price

    def get_cinemas(self):
        return self.__cinemas

    def set_morning_price(self, morning_prince: int):
        self.__morning_price = morning_prince

    def set_afternoon_price(self, afternoon_price: int):
        self.__afternoon_price = afternoon_price

    def set_evening_price(self, evening_price: int):
        self.__evening_price = evening_price

    def add_cinema(self, cinema_id, cinema_address, screens):
        self.__cinemas[cinema_id] = cinema.Cinema(
            cinema_id, cinema_address, screens)

    def __str__(self):
        return self.__city_name
