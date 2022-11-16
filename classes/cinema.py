#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import screen
from dbfunc import conn

# ˄


class Cinema(object):
    # ˅

    # ˄

    def __init__(self, cinema_id, address):

        self.__cinema_id = cinema_id

        self.__address = address
        self.__screens = list()

        screens = conn.select(
            "SELECT * FROM SCREEENS WHERE CINEMA_ID=%d", (self.__cinema_id,))

        for screen in screens:

            self.__screens.append(
                screen.Screen(screen[0], screen[1], screen[2], screen[3]))

        self.__listings = list()
        ...

    def get_cinema_id(self):
        return self.__cinema_id

    def get_address(self):
        return self.__address

    def get_screens(self):
        return self.__screens

    def get_listings(self):
        return self.__listings

    def update_listing(self, listing_id, date, film):
        # ˅
        pass
        # ˄

    def remove_listing(self, listing_id):
        # ˅
        pass
        # ˄

    def add_listing(self, listing_id, date, film, cinema):
        # ˅
        pass
        # ˄

    # ˅

    # ˄


# ˅

# ˄
