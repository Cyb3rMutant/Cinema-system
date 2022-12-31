from dbfunc import conn
from passlib.hash import sha256_crypt
from user_factory import User_factory
from city_container import Cities
from film_container import Films
from city import City
from film import Film
import datetime
from customer import Customer
import random


class Model():
    def __init__(self):
        self.__films = Films()
        films = conn.select("SELECT * FROM films;")
        for f in films:
            self.__films[f["FILM_TITLE"]] = (
                Film(f["FILM_TITLE"], f["FILM_RATING"], f["FILM_GENRE"], f["FILM_YEAR"], f["FILM_AGE_RATING"], f["FILM_DURATION"], f["FILM_DESCRIPTION"], f["FILM_CAST"]))

        self.__cities = Cities()
        cities = conn.select("SELECT * FROM cities;")
        for c in cities:
            self.__cities[c["CITY_NAME"]] = (
                City(c["CITY_NAME"], c["CITY_MORNING_PRICE"], c["CITY_AFTERNOON_PRICE"], c["CITY_EVENING_PRICE"]))

    def validate_login(self, username, password):
        data = conn.select(
            "SELECT * FROM users u \
                LEFT JOIN cinemas c ON c.CINEMA_ID=u.CINEMA_ID \
                    WHERE USER_NAME=%s", username)

        if (data):
            data = data[0]
            hash = data["USER_PASSWORD_HASH"]
        else:
            return -1

        if (sha256_crypt.verify(password, hash)):
            cinema = self.__cities[data["CITY_NAME"]][data["CINEMA_ID"]]

            user = User_factory.get_user_type(data["USER_TYPE"])(
                data["USER_NAME"], data["USER_ID"], cinema)

            return user
        else:
            return 0

    def get_bookings_as_list(self):
        bookings = []
        for b in self.__show.get_bookings().values():
            bookings.append(b.as_list())
        return bookings

    def get_all_bookings_as_list(self):
        bookings = []
        for l in self.get_listings():
            for s in l.get_shows().values():
                for b in s.get_bookings().values():
                    bookings.append(b.as_list())
        return bookings

    def add_city(self, city_name, morning_price, afternoon_price, evening_price):
        conn.insert("INSERT INTO cities VALUES (%s, %s, %s, %s);",
                    city_name, morning_price, afternoon_price, evening_price,)

        self.__cities.add_city(city_name, morning_price,
                               afternoon_price, evening_price)

    def add_cinema(self,  address, number_of_screens):
        conn.insert(
            "INSERT INTO cinemas (CINEMA_ADDRESS, CITY_NAME) VALUES (%s, %s);", address, self.__city.get_city_name())
        cinema_id = conn.select("SELECT MAX(CINEMA_ID) as CINEMA_ID FROM cinemas;")[
            0]["CINEMA_ID"]

        for screen in range(number_of_screens):
            conn.insert("INSERT INTO screens(SCREEN_NUM_VIP_SEATS,SCREEN_NUM_UPPER_SEATS,SCREEN_NUM_LOWER_SEATS,CINEMA_ID, SCREEN_NUMBER) VALUES (%s, %s, %s, %s, %s);",
                        10, 74, 36, cinema_id, screen)

        self.__city.add_cinema(cinema_id, address)

    def get_films(self):
        return self.__films.get_films()

    def add_booking(self, seat_type, num_of_tickets, customer_email):
        if not seat_type:
            return -1

        booking_reference = str(random.randint(100000, 999999))

        city_price = self.get_city_price()

        booking_info = self.__show.add_booking(booking_reference, seat_type, num_of_tickets,
                                               datetime.date.today(), city_price, Customer("Someone", "798405324542", customer_email))
        if not booking_info:
            return 0
        conn.insert("INSERT INTO bookings(BOOKING_REFERENCE, BOOKING_SEAT_COUNT, BOOKING_DATE, BOOKING_PRICE, SHOW_ID, SEAT_TYPE, CUSTOMER_EMAIL) VALUES (%s, %s, %s, %s, %s, %s, %s);",
                    booking_info.get_booking_reference(), booking_info.get_number_of_seats(), booking_info.get_date_of_booking(), booking_info.get_price(), self.__show.get_show_id(), seat_type, customer_email)

        print("successfully done booking")
        print("booking info: ")
        print(f'{booking_info.get_booking_reference()}\n{booking_info.get_number_of_seats()}\n{booking_info.get_date_of_booking()}\n{booking_info.get_price()}\n{self.__show.get_show_id()}\n{seat_type}\n{customer_email}\n')

    def remove_listing(self, listings):
        for id in listings:
            conn.delete("DELETE FROM shows WHERE LISTING_ID=%s", id)
            conn.delete(
                "DELETE FROM listings WHERE LISTING_ID=%s AND CINEMA_ID=%s;", id, self.__cinema.get_cinema_id())
            self.__cinema.remove_listing(id)

    def add_listing(self, film):
        conn.insert("INSERT INTO listings (LISTING_TIME, FILM_TITLE, CINEMA_ID) VALUES (%s, %s, %s);",
                    self.__date, film, self.__cinema.get_cinema_id())
        # now get the listing id from database
        listing_id = conn.select(
            "SELECT MAX(LISTING_ID) as LISTING_ID FROM listings")[0]["LISTING_ID"]

        self.__cinema.add_listing(listing_id, self.__date, self.__films[film])

    def update_listing(self, film):
        listing_id = self.__listing.get_listing_id()
        film = self.__films[film]
        conn.update("UPDATE listings SET LISTING_TIME=%s, FILM_TITLE=%s WHERE LISTING_ID=%s;",
                    self.__date, film.get_title(), listing_id)

        self.__cinema.update_listing(listing_id, self.__date, film)

    def get_city_price(self):
        time = conn.select(
            "SELECT NAME FROM times_of_day WHERE %s BETWEEN START_TIME AND END_TIME;", self.__show.get_time())[0]["NAME"]

        if time == "morning":
            return self.__city.get_morning_price()
        elif time == "afternoon":
            return self.__city.get_afternoon_price()
        elif time == "evening":
            return self.__city.get_evening_price()

    def get_cinema_city(self):
        city_name = conn.select("SELECT CITY_NAME FROM CINEMAS WHERE CINEMA_ID = %s;",
                                self.__cinema.get_cinema_id())[0]["CITY_NAME"]
        self.__city = self.__cities[city_name]
        return self.__city

    def cancel_booking(self, booking_reference):
        conn.update(
            "UPDATE bookings SET REFUND=%s WHERE BOOKING_REFERENCE=%s;", self.__show.get_bookings()[booking_reference].get_price()/2, booking_reference)
        self.__show.cancel_booking(booking_reference)

    def add_show(self, time):

        duration = datetime.timedelta(
            minutes=self.__listing.get_film().get_duration()+30)

        data = conn.select("SELECT `SCREEN_ID` FROM screens WHERE `SCREEN_ID` NOT IN ( (\
                                        SELECT s2.`SCREEN_ID` FROM screens s2\
                                            LEFT JOIN shows sh2 ON s2.`SCREEN_ID` = sh2.`SCREEN_ID`\
                                            LEFT JOIN listings l2 ON sh2.`LISTING_ID` = l2.`LISTING_ID`\
                                        WHERE s2.`SCREEN_ID` AND s2.`CINEMA_ID` = %s AND l2.`LISTING_TIME` = %s\
                                        GROUP BY s2.`SCREEN_ID` HAVING COUNT(sh2.`SCREEN_ID`) >= 4\
                                    )\
                                    UNION (\
                                        SELECT s1.`SCREEN_ID` FROM screens s1\
                                            LEFT JOIN shows sh1 ON s1.`SCREEN_ID` = sh1.`SCREEN_ID`\
                                            LEFT JOIN listings l1 ON sh1.`LISTING_ID` = l1.`LISTING_ID`\
                                            LEFT JOIN films f1 ON l1.`FILM_TITLE` = f1.`FILM_TITLE`\
                                        WHERE s1.`CINEMA_ID` = %s AND l1.`LISTING_TIME` = %s\
                                            AND (\
                                                (ADDTIME(%s, '-00:30:00') BETWEEN `SHOW_TIME` AND ADDTIME(`SHOW_TIME`, SEC_TO_TIME(`FILM_DURATION` * 60)))\
                                                OR (`SHOW_TIME` BETWEEN ADDTIME(%s, '-00:30:00') AND ADDTIME(%s, %s))\
                                            )\
                                    )\
                                )\
                                AND `CINEMA_ID` = %s;\
    ", self.__cinema.get_cinema_id(), self.__listing.get_date(), self.__cinema.get_cinema_id(), self.__listing.get_date(), time, time, time, duration, self.__cinema.get_cinema_id())
        print(data)
        if not data:
            return 0

        screen_id = data[0]["SCREEN_ID"]
        conn.insert(
            "INSERT INTO shows(SHOW_TIME, SCREEN_ID, LISTING_ID) VALUES (%s, %s, %s);", time, screen_id, self.__listing.get_listing_id())

        show_id = conn.select(
            "SELECT MAX(SHOW_ID) as SHOW_ID FROM shows")[0]["SHOW_ID"]
        print(show_id)
        screen = self.__cinema.get_screens()[screen_id]

        self.__listing.add_show(show_id, time, screen)

        return 1

    def get_booking(self, booking_ref):
        data = conn.select("SELECT b.`BOOKING_REFERENCE`, b.`SHOW_ID`, s.`LISTING_ID`, l.`CINEMA_ID`, c.`CITY_NAME`\
                            FROM bookings b\
                                LEFT JOIN shows s ON b.`SHOW_ID` = s.`SHOW_ID`\
                                LEFT JOIN listings l ON s.`LISTING_ID` = l.`LISTING_ID`\
                                LEFT JOIN cinemas c ON l.`CINEMA_ID` = c.`CINEMA_ID`\
                                LEFT JOIN cities ON c.`CITY_NAME` = cities.`CITY_NAME`\
                            WHERE\
                                b.`BOOKING_REFERENCE` = %s;", booking_ref)[0]
        print(data)
        return self.__cities[
            data["CITY_NAME"]][
                data["CINEMA_ID"]].get_listings()[
                    data["LISTING_ID"]].get_shows()[
                        data["SHOW_ID"]].get_bookings()[
                            data["BOOKING_REFERENCE"]]

    def get_cities(self):
        return self.__cities.get_cities().values()

    def get_city(self, name=None):
        if name:
            self.__city = self.__cities[name]
        else:
            self.__city = list(self.__cities.get_cities().values())[0]
        return self.__city

    def get_cinemas(self):
        return self.__city.get_cinemas().values()

    def get_cinema(self, id=None):
        if id:
            self.__cinema = self.__city[id]
        else:
            self.__cinema = list(self.__city.get_cinemas().values())[0]
        return self.__cinema

    def get_listings(self):
        listings = []
        for l in list(self.__cinema.get_listings().values()):
            if l.get_date() == self.__date:
                listings.append(l)
        return listings

    def get_listing(self, id=None):
        if id:
            self.__listing = self.__cinema.get_listings()[id]
        else:
            self.__listing = list(self.__cinema.get_listings().values())[0]
        print(self.__listing)
        return self.__listing

    def get_shows(self):
        return self.__listing.get_shows().values()

    def get_show(self, id=None):
        if id:
            self.__show = self.__listing.get_shows()[id]
        else:
            self.__show = list(self.__listing.get_shows().values())[0]
        return self.__show

    def set_city(self, city):
        self.__city = city

    def set_cinema(self, cinema):
        self.__cinema = cinema

    def set_listing(self, listing):
        self.__listing = listing

    def set_show(self, show):
        self.__show = show

    def set_date(self, date):
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        self.__date = date.date()
        print(self.__date, type(self.__date))
