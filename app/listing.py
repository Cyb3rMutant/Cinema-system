"""
Authors:
    Rohaan Aslam (21017718)
    Benjamin Hussey (21022768)
    Yazeed Abu-Hummous (21014295)
Date: 08/01/2023
Module: Advanced Software Development 22/23
"""

import show


class Listing(object):
    def __init__(self, listing_id, date, film, cinema):
        self.__listing_id = listing_id

        self.__date = date

        self.__film = film

        self.__cinema = cinema

        self.__shows = dict()

    def __getitem__(self, key):
        return self.__shows[key]

    def __setitem__(self, key, value):
        self.__shows[key] = value

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
        return (
            f"listing_id: {self.__listing_id} date: {self.__date} film: {self.__film}"
        )

    def as_list(self):
        return [
            self.__listing_id,
            self.__date,
            self.__film,
            "\n".join([str(s) for s in self.__shows.values()]),
        ]
