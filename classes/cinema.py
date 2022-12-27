import listing
import screen
from dbfunc import conn
import film_container
import film


class Cinema(object):
    def __init__(self, cinema_id, address):

        self.__cinema_id = cinema_id

        self.__address = address
        self.__screens = dict()
        self.__listings = dict()

        screens = conn.select(
            "SELECT * FROM screens WHERE CINEMA_ID=%s ORDER BY SCREEN_NUMBER;", self.__cinema_id)
        for s in screens:
            self.__screens[s["SCREEN_ID"]] = screen.Screen(
                s["SCREEN_ID"], s["SCREEN_NUM_VIP_SEATS"], s["SCREEN_NUM_UPPER_SEATS"], s["SCREEN_NUM_LOWER_SEATS"], s["SCREEN_NUMBER"])

        listings = conn.select(
            "SELECT * FROM listings WHERE CINEMA_ID=%s", self.__cinema_id)
        for l in listings:
            self.__listings[l["LISTING_ID"]] = listing.Listing(
                l["LISTING_ID"], l["LISTING_TIME"], film_container.Films.get_film(l["FILM_TITLE"]), self)

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

    def add_listing(self, listing_id, date, film: film.Film):
        # add listing to database (ben)
        self.__listings[listing_id] = listing.Listing(
            listing_id, date, film, self)  # end paramter is cinema

    def __str__(self):
        return f"cinema_id: {self.__cinema_id} address: {self.__address}"
