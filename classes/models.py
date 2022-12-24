from dbfunc import conn
from passlib.hash import sha256_crypt
from user_factory import User_factory
from city_container import Cities
from film_container import Films
from city import City
from film import Film
import datetime


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

    def get_bookings(self, cinema):
        bookings = []
        for show in cinema:
            bookings += show.get_bookings()
        return bookings

    def add_city(self, city_name, morning_price, afternoon_price, evening_price):
        conn.insert("INSERT INTO cities VALUES (%s, %s, %s, %s);",
                    city_name, morning_price, afternoon_price, evening_price,)

        self.__cities.add_city(city_name, morning_price,
                               afternoon_price, evening_price)

    def add_cinema(self, city, address, number_of_screens):
        conn.insert(
            "INSERT INTO cinemas (CINEMA_ADDRESS, CITY_NAME) VALUES (%s, %s);", address, city)
        cinema_id = conn.select("SELECT MAX(CINEMA_ID) as CINEMA_ID FROM cinemas;")[
            0]["CINEMA_ID"]

        for screen in range(number_of_screens):
            conn.insert("INSERT INTO screens(SCREEN_NUM_VIP_SEATS,SCREEN_NUM_UPPER_SEATS,SCREEN_NUM_LOWER_SEATS,CINEMA_ID, SCREEN_NUMBER) VALUES (%s, %s, %s, %s, %s);",
                        10, 74, 36, cinema_id, screen)

        self.__cities[city].add_cinema(cinema_id, address)

    def get_cities(self):
        return self.__cities.get_cities()

    def get_films(self):
        return self.__films.get_films()

    def add_booking(self, city, show, seat_type, num_of_tickets, customer_email):
        date_today = datetime.date.today()

        city_price = self.get_city_price(city, show.get_time())

        booking_info = show.add_booking(seat_type, num_of_tickets, date_today,
                                        city_price, customer_email)

        conn.update(
            f"UPDATE shows SET SHOW_AVAILABLE_{seat_type.upper()}_SEATS = SHOW_AVAILABLE_{seat_type.upper()}_SEATS - %s WHERE SHOW_ID = (%s);", num_of_tickets, show.get_show_id())

        conn.insert("INSERT INTO bookings(BOOKING_REFERENCE,BOOKING_SEAT_COUNT,BOOKING_DATE,BOOKING_PRICE,SHOW_ID,SEAT_TYPE,CUSTOMER_EMAIL) VALUES (%s, %s, %s, %s, %s, %s, %s);",
                    booking_info.get_booking_reference(), booking_info.get_number_of_seats(), booking_info.get_date_of_booking(), booking_info.get_price(), show.get_show_id(), seat_type, customer_email)

        print("successfully done booking")
        print("booking info: ")
        print(f'{booking_info.get_booking_reference()}\n{booking_info.get_number_of_seats()}\n{booking_info.get_date_of_booking()}\n{booking_info.get_price()}\n{show.get_show_id()}\n{seat_type}\n{customer_email}\n')

    def remove_listing(self, city, cinema, listings):
        print(f"\n\n{listings}\n\n")
        for id in listings:
            conn.delete("DELETE FROM shows WHERE LISTING_ID=%s", id)
            conn.delete(
                "DELETE FROM listings WHERE LISTING_ID=%s AND CINEMA_ID=%s;", id, cinema)
            print(f"\n{cinema}")
            self.__cities[city][cinema].remove_listing(id)

    def add_listing(self, date, film, city, cinema):
        conn.insert("INSERT INTO listings (LISTING_TIME, FILM_TITLE, CINEMA_ID) VALUES (%s, %s, %s);",
                    date, film, cinema)
        # now get the listing id from database
        listing_id = conn.select(
            "SELECT MAX(LISTING_ID) as LISTING_ID FROM listings")[0]["LISTING_ID"]
        self.__cities[city][cinema].add_listing(
            listing_id, date, self.__films[film])

    def update_listing(self, city, cinema_id, listing_id, date, film):
        film = self.__films[film]
        conn.update("UPDATE listings SET LISTING_TIME=%s, FILM_TITLE=%s WHERE LISTING_ID=%s;",
                    date, film.get_title(), listing_id)

        self.__cities[city][cinema_id].update_listing(listing_id, date, film)

    def get_city_price(self, city, show_time):
        time = conn.select(
            "SELECT NAME FROM times_of_day WHERE %s BETWEEN START_TIME AND END_TIME;", show_time)[0]["NAME"]

        if time == "morning":
            return self.__cities[city].get_morning_price()
        elif time == "afternoon":
            return self.__cities[city].get_afternoon_price()
        elif time == "evening":
            return self.__cities[city].get_evening_price()

    def get_city(self, cinema):
        for city in self.__cities:
            if cinema in self.__cities[city].get_cinemas():
                return city
