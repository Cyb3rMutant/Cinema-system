#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from cinema import Cinema
from dbfunc import conn

# ˄


class City(object):
    def __init__(self, city_name, morning_price, afternoon_price, evening_price):

        self.__city_name = city_name

        self.__morning_price = morning_price

        self.__afternoon_price = afternoon_price

        self.__evening_price = evening_price

        cinemas = conn.select(
            "SELECT * FROM CINEMAS WHERE CITY_NAME=%s;", (self.__city_name,))
        for cinema in cinemas:
            self.__cinemas.append(Cinema(cinema[0], cinema[1]))

    def get_city_name(self):
        return self._city_name

    def get_morning_price(self):
        return self._morning_price

    def get_afternoon_price(self):
        return self._afternoon_price

    def get_evening_price(self):
        return self._evening_price

    def get_cinemas(self):
        return self._cinemas

    def set_morning_price(self, morning_prince):
        # ˅
        pass
        # ˄

    def set_afternoon_price(self, afternoon_price):
        # ˅
        pass
        # ˄

    def set_evening_price(self, evening_price):
        # ˅
        pass
        # ˄

    def add_cinema(self, cinema_id, cinema_address):

        conn.insert("INSERT INTO CINEMAS VALUES (%d, %s);",
                    (cinema_id, cinema_address,))

        self.__cinemas.append(Cinema(cinema_id, cinema_address))
