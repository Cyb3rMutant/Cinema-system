from dbfunc import conn
from passlib.hash import sha256_crypt
from user_factory import User_factory
from city_container import Cities
from film_container import Films
from city import City
from film import Film


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

    def add_booking(self, booking_reference, num_of_tickets, date, final_ticket_price, show_id, seat_type, customer_email):
        conn.insert("INSERT INTO bookings(BOOKING_REFERENCE,BOOKING_SEAT_COUNT,BOOKING_DATE,BOOKING_PRICE,SHOW_ID,SEAT_TYPE,CUSTOMER_EMAIL) VALUES (%s, %s, %s, %s, %s, %s, %s);",
                    booking_reference, num_of_tickets, date, final_ticket_price,show_id,seat_type,customer_email)

        if seat_type == "Lower": query = "UPDATE shows SET SHOW_AVAILABLE_LOWER_SEATS = SHOW_AVAILABLE_LOWER_SEATS - (%s) WHERE SHOW_ID = (%s);"
        if seat_type == "Upper": query = "UPDATE shows SET SHOW_AVAILABLE_UPPER_SEATS = SHOW_AVAILABLE_UPPER_SEATS - (%s) WHERE SHOW_ID = (%s);" 
        if seat_type == "VIP": query = "UPDATE shows SET SHOW_AVAILABLE_VIP_SEATS = SHOW_AVAILABLE_VIP_SEATS - (%s) WHERE SHOW_ID = (%s);"

        conn.update(query, num_of_tickets, show_id,)
        
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

    def update_listing(self, city, original_city, date, film, cinema_id, original_cinema_id, listing_id):
        id_list = []  #ugly way of being able to pass listing id to remove listing
        id_list.append(listing_id)
        if cinema_id != original_cinema_id:  #if they have changed the cinema 
            self.remove_listing(original_city, original_cinema_id, id_list)   #listing id needs to be a list to be passed to remove listing
            self.add_listing(date, film, city, cinema_id)
        else:  
            self.__cities[city][cinema_id].update_listing(
                listing_id, date, self.__films[film])
            
      

        
        
