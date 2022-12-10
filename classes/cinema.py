#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import listing
import screen
import listing
from dbfunc import conn
import film
# ˄


class Cinema(object):
    def __init__(self, cinema_id, address):

        self.__cinema_id = cinema_id

        self.__address = address
        self.__screens = list()
        self.__listings = list()

        screens = conn.select(
            "SELECT * FROM screens WHERE CINEMA_ID=%s", self.__cinema_id)
        for s in screens:
            self.__screens.append(
                screen.Screen(s["SCREEN_ID"], s["SCREEN_NUM_VIP_SEATS"], s["SCREEN_NUM_UPPER_SEATS"], s["SCREEN_NUM_LOWER_SEATS"]))

        listings = conn.select(
            "SELECT * FROM listings WHERE CINEMA_ID=%s", self.__cinema_id)
        for l in listings:
            self.__listings.append(listing.Listing(
                l["LISTING_ID"], l["LISTING_TIME"], l["FILM_TITLE"], l["CINEMA_ID"]))

    def get_cinema_id(self):
        return self.__cinema_id

    def get_address(self):
        return self.__address

    def get_screens(self):
        return self.__screens

    def get_listings(self):
        return self.__listings

    def update_listing(self, listing_id, date, film):
        listing = None
        for l in self.__listings:
            if l.get_listing_id() == listing_id:
                listing = l
                break
        listing.set_date(date)
        listing.set_film = film

        conn.update("UPDATE listings SET LISTING_DATE=%s, FILM_TITLE=%s WHERE LISTING_ID=%s;",
                    date, film.get_title(), listing.get_listing_id())

    def remove_listing(self, listing_id):
        listing = None
        for l in self.__listings:
            if l.get_listing_id() == listing_id:
                listing = l
                break

        conn.delete("DELETE FROM listings WHERE LISTING_ID=%s;",
                    listing.get_listing_id)

    def add_listing(self, date, film: film.Film):
        # add listing to database (ben)
        film_title = film.get_title()
        conn.insert("INSERT INTO LISTINGS VALUES (%s, %s, %s);",
                    date, film_title, self.__cinema_id)
        # now get the listing id from database
        listingID = conn.select("SELECT MAX(LISTING_ID) FROM listings")
        self.__listings.append(listing.Listing(
            listingID, date, film, self))  # end paramter is cinema
