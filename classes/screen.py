#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from show import Show
from dbfunc import conn

# ˄


class Screen(object):
    # ˅

    # ˄

    def __init__(self, screen_id, num_vip_seats, num_upper_seats, num_lower_seats):

        self.__screen_id = screen_id

        self.__num_vip_seats = num_vip_seats

        self.__num_upper_seats = num_upper_seats

        self.__num_lower_seats = num_lower_seats

        self.__shows = list()

        shows = conn.select("SELECT * FROM SHOWS WHERE SCREEN_ID=%d",
                            (self.__screen_id,))

        for show in shows:
            self.__shows.append(
                Show(show[0], show[1], show[2], show[3], show[4], show[5], show[6],))

    def get_screen_id(self):
        return self.__screen_id

    def get_num_vip_seats(self):
        return self.__num_vip_seats

    def get_num_upper_seats(self):
        return self.__num_upper_seats

    def get_num_lower_seats(self):
        return self.__num_lower_seats

    def get_shows(self):
        return self.__shows

    def add_show(self, show_id, time, available_vip_seats, available_upper_seats, available_lower_seats, film):
        conn.insert("INSERT INTO SHOWS VALUES(%d, %s, %d, %d, %d, %s)", (show_id, time,
                    available_vip_seats, available_upper_seats, available_lower_seats, film,))

        self.__shows.append(
            Show(show_id, time, available_vip_seats, available_upper_seats, available_lower_seats, self, film))

    def remove_show(self, show_id):
        # ˅
        pass
        # ˄

    # ˅

    # ˄


# ˅

# ˄
