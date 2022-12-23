import listing
import screen
from dbfunc import conn
import film


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
                screen.Screen(s["SCREEN_NUMBER"], s["SCREEN_NUM_VIP_SEATS"], s["SCREEN_NUM_UPPER_SEATS"], s["SCREEN_NUM_LOWER_SEATS"]))

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
        listing.set_film(film)

    def remove_listing(self, listing_id):
        for l in self.__listings:
            if l.get_listing_id() == listing_id:
                self.__listings.remove(l)
                break

    def add_listing(self, listing_id, date, film: film.Film):
        # add listing to database (ben)
        self.__listings.append(listing.Listing(
            listing_id, date, film, self))  # end paramter is cinema

    def __str__(self):
        return f"cinema_id: {self.__cinema_id} address: {self.__address}"
