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
            "SELECT * FROM SCREEENS WHERE CINEMA_ID=%d", (self.__cinema_id,))
        for screen in screens:
            self.__screens.append(
                screen.Screen(screen[0], screen[1], screen[2], screen[3]))

        listings = conn.select(
            "SELECT * FROM SCREENS WHERE CINEMA_ID=%d", (self.__cinema_id,))
        for listing in listings:
            self.__listings.append(listing.Listing(
                listing[0], listing[1], listing[2], listing[3]))

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

        conn.update("UPDATE LISTINGS SET LISTING_DATE=%s, FILM_TITLE=%s WHERE LISTING_ID=%d;",
                    (date, film.get_title(), listing.get_listing_id(),))

    def remove_listing(self, listing_id):
        listing = None
        for l in self.__listings:
            if l.get_listing_id() == listing_id:
                listing = l
                break

        conn.delete("DELETE FROM LISTINGS WHERE LISTING_ID=%d;",
                    (listing.get_listing_id(),))

    def add_listing(self, date, film: film.Film):
        # add listing to database (ben)
        film_title = film.get_title()
        conn.insert("INSERT INTO LISTINGS VALUES (%s, %s, %d);",
                    (date, film_title, self.__cinema_id))
<<<<<<< HEAD
        #now get the listing id from database
        listingID = conn.select("SELECT MAX(LISTING_ID) FROM LISTINGS;")
        self.__listings.append(listing.Listing(listingID, date, film, self))   #end paramter is cinema


    # ˅

    # ˄


# ˅

# ˄
=======
        # now get the listing id from database
        listingID = conn.select("SELECT MAX(LISTING_ID) FROM LISTINGS")
        self.__listings.append(listing.Listing(
            listingID, date, film, self))  # end paramter is cinema
>>>>>>> 23e954c (cinema dbfunc and listing)
