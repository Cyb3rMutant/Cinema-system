#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import show
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

        shows = conn.select("SELECT * FROM shows WHERE SCREEN_ID=%s",
                            self.__screen_id)

        for s in shows:
            self.__shows.append(
                show.Show(s["SHOW_ID"], s["SHOW_TIME"], s["SHOW_AVAILABLE_VIP_SEATS"], s["SHOW_AVAILABLE_UPPER_SEATS"], s["SHOW_AVAILABLE_LOWER_SEATS"], s["FILM_TITLE"], s["SCREEN_ID"],))

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
        conn.insert("INSERT INTO shows VALUES(%s, %s, %s, %s, %s, %s);", show_id, time,
                    available_vip_seats, available_upper_seats, available_lower_seats, film)

        self.__shows.append(
            show.Show(show_id, time, available_vip_seats, available_upper_seats, available_lower_seats, self, film))

    def remove_show(self, show_id):
        # remove show from
        show = None
        for s in self.__shows:
            if s.get_show_id() == show_id:
                show = s
                conn.delete("DELETE FROM shows WHERE SHOW_ID = %s;",
                            (s.get_show_id()))  # delete from db
                self.__shows.remove(s)  # should remove from the list of shows
                break

    # ˅

    # ˄


# ˅

# ˄
