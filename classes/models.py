from dbfunc import conn
from admin import Admin
from passlib.hash import sha256_crypt
from user_factory import User_factory
from city_container import Cities
from film_container import Films
from customer_container import Customers
from city import City
from film import Film
import datetime
from customer import Customer
from payment import Payment
import random
from cinema import Cinema
from screen import Screen
from receipt_generator import Receipt_generator
from ticket_generator import Ticket_generator


class Model():
    def __init__(self):
        self.__films = Films()
        films = conn.select("SELECT * FROM films;")
        for f in films:
            self.__films[f["FILM_TITLE"]] = Film(f["FILM_TITLE"], f["FILM_RATING"], f["FILM_GENRE"],
                                                 f["FILM_YEAR"], f["FILM_AGE_RATING"], f["FILM_DURATION"], f["FILM_DESCRIPTION"], f["FILM_CAST"])

        self.__customers = Customers()
        customers = conn.select("SELECT * FROM customers;")
        for c in customers:
            self.__customers[c["CUSTOMER_EMAIL"]] = Customer(
                c["CUSTOMER_NAME"], c["CUSTOMER_PHONE"], c["CUSTOMER_EMAIL"])

        self.__cities = Cities()
        cities = conn.select("SELECT * FROM cities;")
        for c in cities:
            c = City(
                c["CITY_NAME"], c["CITY_MORNING_PRICE"], c["CITY_AFTERNOON_PRICE"], c["CITY_EVENING_PRICE"])

            cinemas = conn.select(
                "SELECT * FROM cinemas WHERE CITY_NAME=%s;", c.get_city_name())
            for ci in cinemas:
                screens = dict()
                s_data = conn.select(
                    "SELECT * FROM screens WHERE CINEMA_ID=%s ORDER BY SCREEN_NUMBER;", ci["CINEMA_ID"])
                for s in s_data:
                    screens[s["SCREEN_ID"]] = Screen(s["SCREEN_ID"], s["SCREEN_NUM_VIP_SEATS"],
                                                     s["SCREEN_NUM_UPPER_SEATS"], s["SCREEN_NUM_LOWER_SEATS"], s["SCREEN_NUMBER"])

                c.add_cinema(ci["CINEMA_ID"], ci["CINEMA_ADDRESS"], screens)

            self.__cities[c.get_city_name()] = c

        self.__booking_info = None
        self.__city = None
        self.__cinema = None
        self.__listing = None
        self.__show = None
        self.__date = None

    def validate_login(self, user_id, password):
        data = conn.select(
            "SELECT * FROM users u \
                LEFT JOIN cinemas c ON c.CINEMA_ID=u.CINEMA_ID \
                    WHERE USER_ID=%s", user_id)

        if (data):
            data = data[0]
            hash = data["USER_PASSWORD_HASH"]
        else:
            return -1

        if (sha256_crypt.verify(password, hash)):
            cinema = self.__cities[data["CITY_NAME"]][data["CINEMA_ID"]]

            self.__user = User_factory.get_user_type(data["USER_TYPE"])(
                data["USER_NAME"], data["USER_ID"], cinema)

            return self.__user
        else:
            return 0

    def logout(self):
        self.__user = None

    def get_bookings_as_list(self):
        bookings = []
        for b in self.__show.get_bookings().values():
            bookings.append(b.as_list())
        return bookings

    def get_all_bookings_as_list(self):
        bookings = []
        data = conn.select("SELECT b.BOOKING_REFERENCE, b.BOOKING_SEAT_COUNT, b.BOOKING_DATE, b.BOOKING_PRICE, b.SHOW_ID, b.SEAT_TYPE FROM bookings b\
                            LEFT JOIN shows s ON b.`SHOW_ID`=s.`SHOW_ID`\
                            LEFT JOIN listings l ON s.`LISTING_ID`=l.`LISTING_ID`\
                            LEFT JOIN cinemas c ON l.`CINEMA_ID`=c.`CINEMA_ID`\
                        WHERE c.`CINEMA_ID`=%s AND ISNULL(b.`REFUND`);", self.__cinema.get_cinema_id())
        for b in data:
            bookings.append(list(b.values()))
        return bookings

    def get_cinema_listings_as_list(self):
        listings = []
        for l in self.__cinema.get_listings().values():
            listings.append(l.as_list())
        return listings

    def get_shows_for_listing(self, listing_id):
        # quick way of doing it
        data = conn.select(
            "SELECT `SHOW_ID`, `SHOW_TIME`, `SCREEN_ID` FROM shows WHERE LISTING_ID = %s;", listing_id)
        try:
            sh_list = []
            for sh in data:
                sh_list.append(list(sh.values()))
            return sh_list
        except:
            print("no shows airing for listing")

    def add_city(self, city_name, morning_price, afternoon_price, evening_price):
        try:
            # needs these
            morning_price = float(morning_price)
            afternoon_price = float(afternoon_price)
            evening_price = float(evening_price)
            conn.insert("INSERT INTO cities VALUES (%s, %s, %s, %s);",
                        city_name, morning_price, afternoon_price, evening_price,)

            self.__cities.add_city(city_name, morning_price,
                                   afternoon_price, evening_price)

            return 1
        except:
            return 0

    def add_film(self, film_title, film_rating, film_genre, film_year, film_age_rating, film_duration, film_description, film_cast):
        try:
            film_rating = float(film_rating)
            film_year = int(film_year)
            film_duration = int(film_duration)
            if film_rating > 10 or film_rating < 1:
                return -1
            if film_year > 2023 or film_year < 1800:
                return -2
            if film_duration > 400 or film_duration < 20:
                return -3

            conn.insert("INSERT INTO films VALUES(%s, %s, %s, %s, %s, %s, %s, %s);", film_title, film_rating,
                        film_genre, film_year, film_age_rating, film_duration, film_description, film_cast)

            self.__films.add_film(film_title, film_rating, film_genre, film_year,
                                  film_age_rating, film_duration, film_description, film_cast)

            return 1
        except:
            return 0

    def add_cinema(self,  address, number_of_screens):
        try:
            number_of_screens = int(number_of_screens)
            if number_of_screens > 6 or number_of_screens < 1:
                return 0
            else:
                pass

            conn.insert(
                "INSERT INTO cinemas (CINEMA_ADDRESS, CITY_NAME) VALUES (%s, %s);", address, self.__city.get_city_name())
            cinema_id = conn.select("SELECT MAX(CINEMA_ID) as CINEMA_ID FROM cinemas;")[
                0]["CINEMA_ID"]

            screens = dict()
            for screen in range(number_of_screens):
                conn.insert("INSERT INTO screens(SCREEN_NUM_VIP_SEATS,SCREEN_NUM_UPPER_SEATS,SCREEN_NUM_LOWER_SEATS,CINEMA_ID, SCREEN_NUMBER) VALUES (%s, %s, %s, %s, %s);",
                            10, 74, 36, cinema_id, screen)

                s = conn.select(
                    "SELECT * FROM screens WHERE CINEMA_ID=%s ORDER BY SCREEN_NUMBER;", cinema_id)[0]

                screens[s["SCREEN_ID"]] = Screen(s["SCREEN_ID"], s["SCREEN_NUM_VIP_SEATS"],
                                                 s["SCREEN_NUM_UPPER_SEATS"], s["SCREEN_NUM_LOWER_SEATS"], s["SCREEN_NUMBER"])

            self.__city.add_cinema(cinema_id, address, screens)
            return 1
        except:
            return 0

    def get_films(self):
        return self.__films.get_films()

    def validate_booking(self, seat_type, num_of_tickets):
        if not seat_type:
            return -1

        booking_reference = str(random.randint(100000, 999999))

        city_price = self.get_city_price()

        if not city_price:
            return -2  # -2 is only returned if no show is selected

        self.__booking_info = self.__show.add_booking(booking_reference, seat_type, num_of_tickets,
                                                      datetime.date.today(), city_price, None)
        if not self.__booking_info:
            return 0

        return Ticket_generator.gen_ticket(self.__booking_info, self.__cinema)

    def add_booking(self, customer_email, name_on_card, card_number, cvv, expiry_date):
        customer = self.__customers[customer_email]
        customer.set_payment(
            Payment(name_on_card, card_number, expiry_date, cvv))
        self.__booking_info.set_customer(customer)

        conn.insert("INSERT INTO bookings(BOOKING_REFERENCE, BOOKING_SEAT_COUNT, BOOKING_DATE, BOOKING_PRICE, SHOW_ID, SEAT_TYPE, CUSTOMER_EMAIL, USER_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
                    self.__booking_info.get_booking_reference(), self.__booking_info.get_number_of_seats(), self.__booking_info.get_date_of_booking(), self.__booking_info.get_price(), self.__show.get_show_id(), self.__booking_info.get_seat_type(), self.__booking_info.get_customer().get_email(), self.__user.get_id())

        self.__booking_info.get_customer().get_payment().pay(
            self.__booking_info.get_price())

        print(Receipt_generator.gen_receipt(self.__booking_info, self.__user))
        print(Ticket_generator.gen_ticket(self.__booking_info, self.__cinema))
        self.__booking_info = None

    def check_customer(self, customer_email):
        return customer_email in self.__customers.get_customers()

    def update_customer(self, customer_name, customer_email, customer_phone, card_number):
        self.__customers.update_customer(
            customer_email, customer_name, customer_phone)
        conn.update("UPDATE customers SET CUSTOMER_NAME=%s, CUSTOMER_PHONE=%s, CARD_ENDING_DIGITS=%s",
                    customer_name, customer_phone, card_number[-4:])

    def add_customer(self, customer_name, customer_email, customer_phone, card_number):
        self.__customers.add_customer(
            customer_email, customer_name, customer_phone)

        conn.insert("INSERT INTO customers VALUES (%s, %s, %s, %s);",
                    customer_email, customer_name, customer_phone, card_number[-4:])

    def remove_listing(self):
        try:
            id = self.__listing.get_listing_id()
            conn.delete("DELETE FROM shows WHERE LISTING_ID=%s", id)
            conn.delete(
                "DELETE FROM listings WHERE LISTING_ID=%s;", id)
            self.__cinema.remove_listing(id)
            return 1
        except:
            return 0

    def remove_show(self):
        try:
            id = self.__show.get_show_id()
            conn.delete("DELETE FROM shows WHERE SHOW_ID=%s;", id)
            self.__listing.remove_show(id)
            return 1
        except:
            return 0

    def add_listing(self, film):
        conn.insert("INSERT INTO listings (LISTING_TIME, FILM_TITLE, CINEMA_ID) VALUES (%s, %s, %s);",
                    self.__date, film, self.__cinema.get_cinema_id())
        # now get the listing id from database
        listing_id = conn.select(
            "SELECT MAX(LISTING_ID) as LISTING_ID FROM listings")[0]["LISTING_ID"]

        self.__cinema.add_listing(listing_id, self.__date, self.__films[film])
        return 1

    def update_listing(self, film):
        listing_id = self.__listing.get_listing_id()
        film = self.__films[film]
        conn.update("UPDATE listings SET LISTING_TIME=%s, FILM_TITLE=%s WHERE LISTING_ID=%s;",
                    self.__date, film.get_title(), listing_id)

        self.__cinema.update_listing(listing_id, self.__date, film)
        return 1

    def listing_number_of_bookings(self, start, end):
        return conn.select("SELECT\
                        l.`LISTING_ID`, COUNT(`BOOKING_REFERENCE`) as cnt\
                    FROM listings l\
                        LEFT JOIN shows s ON l.`LISTING_ID` = s.`LISTING_ID`\
                        LEFT JOIN bookings b ON s.`SHOW_ID` = b.`SHOW_ID`\
                    WHERE\
                        `CINEMA_ID` = %s\
                        AND ISNULL(b.`REFUND`)\
                        AND l.`LISTING_TIME` BETWEEN %s AND %s\
                    GROUP BY l.`LISTING_ID`\
                    ORDER BY cnt DESC;", self.__cinema.get_cinema_id(), start, end)

    def cinema_revenue(self, start, end):
        return conn.select("SELECT\
                    c.*,\
                        SUM(b.`BOOKING_PRICE`) as tot\
                    FROM cinemas c\
                    LEFT JOIN listings l ON c.`CINEMA_ID` = l.`CINEMA_ID`\
                        LEFT JOIN shows s ON l.`LISTING_ID` = s.`LISTING_ID`\
                        LEFT JOIN bookings b ON s.`SHOW_ID` = b.`SHOW_ID`\
                    WHERE\
                        ISNULL(b.`REFUND`)\
                        AND l.`LISTING_TIME` BETWEEN %s AND %s\
                    GROUP BY c.`CINEMA_ID`\
                    ORDER BY tot DESC", start, end)

    def film_revenue(self):
        return conn.select("SELECT\
                    f.`FILM_TITLE`,\
                        SUM(b.`BOOKING_PRICE`) as tot\
                    FROM films f\
                    LEFT JOIN listings l ON f.`FILM_TITLE` = l.`FILM_TITLE`\
                        LEFT JOIN shows s ON l.`LISTING_ID` = s.`LISTING_ID`\
                        LEFT JOIN bookings b ON s.`SHOW_ID` = b.`SHOW_ID`\
                    WHERE ISNULL(b.`REFUND`)\
                    GROUP BY f.`FILM_TITLE`\
                    ORDER BY tot DESC")

    def staff_number_of_bookings(self, start, end):
        return conn.select("SELECT u.`USER_ID`, u.`USER_NAME`, COUNT(b.`BOOKING_REFERENCE`) as tot\
                    FROM users u\
                    LEFT JOIN bookings b ON u.`USER_ID` = b.`USER_ID`\
                        LEFT JOIN shows s ON b.`SHOW_ID` = s.`SHOW_ID`\
                        LEFT JOIN listings l ON s.`LISTING_ID` = l.`LISTING_ID`\
                    WHERE ISNULL(b.`REFUND`)\
                        AND l.`LISTING_TIME` BETWEEN %s AND %s\
                    GROUP BY u.`USER_ID`\
                    ORDER BY tot DESC", start, end)

    def get_city_price(self):
        try:  # Throws an error if no show is selected, returning -1 prevents
            time = conn.select(
                "SELECT NAME FROM times_of_day WHERE %s BETWEEN START_TIME AND END_TIME;", self.__show.get_time())[0]["NAME"]
        except:
            return
        if time == "morning":
            return self.__city.get_morning_price()
        elif time == "afternoon":
            return self.__city.get_afternoon_price()
        elif time == "evening":
            return self.__city.get_evening_price()

    def get_cinema_city(self):
        city_name = conn.select("SELECT CITY_NAME FROM cinemas WHERE CINEMA_ID = %s;",
                                self.__cinema.get_cinema_id())[0]["CITY_NAME"]
        self.__city = self.__cities[city_name]
        return self.__city

    def cancel_booking(self, booking_reference, customer_email, name_on_card, card_number, cvv, expiry_date):
        b = self.__show.get_bookings()[booking_reference]
        timedelta = b.get_show().get_listing().get_date()-datetime.date.today()
        if (timedelta.days) <= 0:
            return -2

        data = conn.select(
            "SELECT `CARD_ENDING_DIGITS` FROM bookings b LEFT JOIN customers c ON b.`CUSTOMER_EMAIL`=c.`CUSTOMER_EMAIL`\
                WHERE c.`CUSTOMER_EMAIL`=%s;", customer_email)

        if not data:
            return -1
        if data[0]["CARD_ENDING_DIGITS"] != card_number[-4:]:
            return 0

        b.get_customer().set_payment(Payment(name_on_card, card_number, cvv, expiry_date))
        conn.update(
            "UPDATE bookings SET REFUND=%s WHERE BOOKING_REFERENCE=%s;", self.__show.get_bookings()[booking_reference].get_price()/2, booking_reference)
        b.get_customer().get_payment().refund(b.get_price()/2)
        self.__show.cancel_booking(booking_reference)

    def add_show(self, time):
        try:
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

            if not data:
                return 0

            screen_id = data[0]["SCREEN_ID"]
            conn.insert(
                "INSERT INTO shows(SHOW_TIME, SCREEN_ID, LISTING_ID) VALUES (%s, %s, %s);", time, screen_id, self.__listing.get_listing_id())

            show_id = conn.select(
                "SELECT MAX(SHOW_ID) as SHOW_ID FROM shows")[0]["SHOW_ID"]

            screen = self.__cinema.get_screens()[screen_id]

            self.__listing.add_show(show_id, time, screen)

            return 1
        except:
            return -1

    def add_user(self, name, password, user_type):
        password = sha256_crypt.hash(password)
        conn.insert(
            "INSERT INTO users(USER_NAME, USER_PASSWORD_HASH, USER_TYPE, CINEMA_ID) VALUES (%s, %s, %s, %s);", name, password, user_type, self.__cinema.get_cinema_id())
        return 1

    def get_booking(self, booking_ref):
        try:
            if (isinstance(self.__user, Admin)):
                data = conn.select("SELECT b.`BOOKING_REFERENCE`, b.`SHOW_ID`, s.`LISTING_ID`, l.`CINEMA_ID`, c.`CITY_NAME`\
                                    FROM bookings b\
                                        LEFT JOIN shows s ON b.`SHOW_ID` = s.`SHOW_ID`\
                                        LEFT JOIN listings l ON s.`LISTING_ID` = l.`LISTING_ID`\
                                        LEFT JOIN cinemas c ON l.`CINEMA_ID` = c.`CINEMA_ID`\
                                        LEFT JOIN cities ON c.`CITY_NAME` = cities.`CITY_NAME`\
                                    WHERE\
                                        b.`BOOKING_REFERENCE` = %s;", booking_ref)[0]

            else:
                data = conn.select("SELECT b.`BOOKING_REFERENCE`, b.`SHOW_ID`, s.`LISTING_ID`, l.`CINEMA_ID`, c.`CITY_NAME`\
                                    FROM bookings b\
                                        LEFT JOIN shows s ON b.`SHOW_ID` = s.`SHOW_ID`\
                                        LEFT JOIN listings l ON s.`LISTING_ID` = l.`LISTING_ID`\
                                        LEFT JOIN cinemas c ON l.`CINEMA_ID` = c.`CINEMA_ID`\
                                        LEFT JOIN cities ON c.`CITY_NAME` = cities.`CITY_NAME`\
                                    WHERE\
                                        b.`BOOKING_REFERENCE` = %s AND c.`CINEMA_ID` = %s;", booking_ref, self.__user.get_branch().get_cinema_id())[0]
        except IndexError:
            return 0
        self.set_city(self.__cities[data["CITY_NAME"]])
        self.set_cinema(self.__city[data["CINEMA_ID"]])
        self.set_listing(self.__cinema.get_listings()[data["LISTING_ID"]])
        self.set_show(self.__listing.get_shows()[data["SHOW_ID"]])

        return self.__show.get_bookings()[data["BOOKING_REFERENCE"]]

    def get_user_types(self):
        return [t["USER_TYPE"] for t in conn.select("SELECT USER_TYPE FROM user_types;")]

    def get_cities(self):
        return self.__cities.get_cities().values()

    def get_city(self, name=None):
        if name:
            city = self.__cities[name]
        else:
            city = list(self.__cities.get_cities().values())[0]
        self.set_city(city)
        return self.__city

    def get_cinemas(self):
        cinemas = list(self.__city.get_cinemas().values())
        return cinemas if cinemas else ["no cinemas"]

    def get_cinema(self, id=None):
        if id:
            cinema = self.__city[id]
        else:
            cinema = self.get_cinemas()[0]
        self.set_cinema(cinema)
        return self.__cinema

    def get_listings(self):
        if self.__cinema == "no cinemas":
            return ["no listings"]
        listings = [l for l in list(
            self.__cinema.get_listings().values()) if l.get_date() == self.__date]
        # for l in list(self.__cinema.get_listings().values()):
        #     if l.get_date() == self.__date:
        #         listings.append(l)
        if not listings:
            listings.append("no listings")
        return listings

    def get_listing(self, id=None):
        if id:
            listing = self.__cinema.get_listings()[id]
        else:
            listing = self.get_listings()[0]
        self.set_listing(listing)
        return self.__listing

    def get_shows(self):
        if self.__listing == "no listings":
            return ["no shows"]
        shows = list(self.__listing.get_shows().values())
        if not shows:
            shows.append("no shows")
        return shows

    def get_show(self, id=None):
        if id:
            show = self.__listing.get_shows()[id]
        else:
            show = self.get_shows()[0]
        self.set_show(show)
        return self.__show

    def set_city(self, city):
        self.__city = city

    def set_cinema(self, cinema):
        if self.__cinema and not isinstance(self.__cinema, str):
            self.__cinema.get_listings().clear()

        self.__cinema = cinema

        if isinstance(cinema, str):
            return

        listings = conn.select(
            "SELECT * FROM listings WHERE CINEMA_ID=%s", self.__cinema.get_cinema_id())
        for l in listings:
            self.__cinema.add_listing(
                l["LISTING_ID"], l["LISTING_TIME"], self.__films[l["FILM_TITLE"]])

    def set_listing(self, listing):
        if self.__listing and not isinstance(self.__listing, str):
            self.__listing.get_shows().clear()

        self.__listing = listing

        if isinstance(listing, str):
            return

        shows = conn.select(
            "SELECT * FROM shows WHERE LISTING_ID=%s", self.__listing.get_listing_id())
        for s in shows:
            print(self.__cinema, self.__cinema.get_screens())
            self.__listing.add_show(
                s["SHOW_ID"], s["SHOW_TIME"], self.__cinema.get_screens()[s["SCREEN_ID"]])

    def set_show(self, show):
        if self.__show and not isinstance(self.__show, str):
            self.__show.get_bookings().clear()

        self.__show = show

        if isinstance(show, str):
            return

        bookings = conn.select(
            "SELECT * FROM bookings WHERE SHOW_ID=%s AND ISNULL(REFUND)", self.__show.get_show_id())
        for b in bookings:
            self.__show.add_booking(b["BOOKING_REFERENCE"], b["SEAT_TYPE"], b["BOOKING_SEAT_COUNT"],
                                    b["BOOKING_DATE"], b["BOOKING_PRICE"], self.__customers[b["CUSTOMER_EMAIL"]])

    def set_date(self, date):
        try:
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
            self.__date = date.date()
        except:
            pass
        print(self.__date)

    def clear_data(self):
        self.__date = None
        self.__booking_info = None
        self.__show = None
        self.__listing = None
        self.__cinema = None
        self.__city = None
