#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import cinema
from dbfunc import conn

# ˄


class City(object):
    def __init__(self, city_name: str, morning_price: int, afternoon_price: int, evening_price: int):

        self.__city_name = city_name

        self.__morning_price = morning_price

        self.__afternoon_price = afternoon_price

        self.__evening_price = evening_price

        self.__cinemas = dict()

        cinemas = conn.select(
            "SELECT * FROM cinemas WHERE CITY_NAME=%s;", self.__city_name)
        for c in cinemas:
            self.__cinemas[c["CINEMA_ID"]] = cinema.Cinema(
                c["CINEMA_ID"], c["CINEMA_ADDRESS"])

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

    def __getitem__(self, cinema_id: int):
        return self.__cinemas[cinema_id]

    def set_morning_price(self, morning_prince: int):
        self.__morning_price = morning_prince

    def set_afternoon_price(self, afternoon_price: int):
        self.__afternoon_price = afternoon_price

    def set_evening_price(self, evening_price: int):
        self.__evening_price = evening_price

    def add_cinema(self, cinema_id: int, cinema_address: str):
        self.__cinemas[cinema_id] = cinema.Cinema(cinema_id, cinema_address)

    def __str__(self):
        return self.__city_name
