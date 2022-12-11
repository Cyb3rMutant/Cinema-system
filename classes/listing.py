#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import film
import show
from dbfunc import conn

# ˄


class Listing(object):
    def __init__(self, listing_id, date, film, cinema):

        self.__listing_id = listing_id

        self.__date = date

        self.__film = film

        self.__cinema = cinema

        self.__shows = list()

        shows = conn.select("SELECT * FROM shows WHERE LISTING_ID=%s",
                            self.__listing_id)
        for s in shows:
            self.__shows.append(
                show.Show(s["SHOW_ID"], s["SHOW_TIME"], s["SHOW_AVAILABLE_VIP_SEATS"], s["SHOW_AVAILABLE_UPPER_SEATS"], s["SHOW_AVAILABLE_LOWER_SEATS"], s["FILM_TITLE"], s["SCREEN_ID"]))

    def get_listing_id(self):
        return self.__listing_id

    def get_date(self):
        return self.__date

    def get_film(self):
        return self.__film

    def get_cinema(self):
        return self.__cinema

    def get_shows(self):
        return self.__shows

    def set_date(self, date):
        conn.update("UPDATE listings SET LISTING_DATE=%s WHERE LISTING_ID=%s",
                    date, self.__listing_id)
        self.__date = date

    def set_film(self, film):
        conn.update("UPDATE listings SET FILM_TITLE=%s WHERE LISTING_ID=%s",
                    film.get_title(), self.__listing_id)
        self.__film = film

    def update_show_time(self, show_id, time):
        conn.update("UPDATE shows SET SHOW_TIME=%s WHERE SHOW_ID=%s",
                    time, show_id)
        self.__time
