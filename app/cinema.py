"""
Authors:
    Rohaan Aslam (21017718)
    Benjamin Hussey (21022768)
    Yazeed Abu-Hummous (21014295)
Date: 08/01/2023
Module: Advanced Software Development 22/23
"""

import listing


class Cinema(object):
    def __init__(self, cinema_id, address, screens):

        self.__cinema_id = cinema_id

        self.__address = address
        self.__screens = screens
        self.__listings = dict()

    def get_cinema_id(self):
        return self.__cinema_id

    def get_address(self):
        return self.__address

    def get_screens(self):
        return self.__screens

    def get_listings(self):
        return self.__listings

    def update_listing(self, listing_id, date, film):
        listing = self.__listings[listing_id]
        listing.set_date(date)
        listing.set_film(film)

    def remove_listing(self, listing_id):
        self.__listings.pop(listing_id)

    def add_listing(self, listing_id, date, film):
        # add listing to database (ben)
        self.__listings[listing_id] = listing.Listing(
            listing_id, date, film, self
        )  # end paramter is cinema

    def __str__(self):
        return f"cinema_id: {self.__cinema_id} address: {self.__address}"
