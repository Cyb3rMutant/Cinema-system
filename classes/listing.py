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

        self.__shows = dict()

        shows = conn.select("SELECT * FROM shows WHERE LISTING_ID=%s",
                            self.__listing_id)
        for s in shows:
            self.__shows[s["SHOW_ID"]] = show.Show(
                s["SHOW_ID"], s["SHOW_TIME"], cinema.get_screens()[s["SCREEN_ID"]], self)

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
        self.__date = date

    def set_film(self, film):
        self.__film = film

    def add_show(self, show_id, time, screen):
        self.__shows[show_id] = show.Show(show_id, time, screen, self)

    def remove_show(self, show_id):
        self.__shows.pop(show_id)

    def __str__(self):
        return f"listing_id: {self.__listing_id} date: {self.__date} film: {self.__film}"

    def as_list(self):
        return [self.__listing_id, self.__date, self.__film, "\n".join([str(s) for s in self.__shows.values()])]
