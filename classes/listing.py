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

        shows = conn.select("SELECT * FROM SHOWS WHERE LISTING_ID=%d",
                            self.__listing_id)
        for show in shows:
            self.__shows.append(
                show.Show(show[0], show[1], show[2], show[3], show[4], show[5], show[6]))

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
        conn.update("UPDATE LISTINGS SET LISTING_DATE=%s WHERE LISTING_ID=%d",
                    (date, self.__listing_id,))
        self.__date = date

    def set_film(self, film):
        conn.update("UPDATE LISTINGS SET FILM_TITLE=%s WHERE LISTING_ID=%d",
                    (film.get_title(), self.__listing_id,))
        self.__film = film

        for show in self.__shows:
            show.set_film(film)

    def update_show_time(self, show_id, time):
        conn.update("UPDATE SHOWS SET SHOW_TIME=%s WHERE SHOW_ID=%d",
                    (time, show_id,))
        self.__time
