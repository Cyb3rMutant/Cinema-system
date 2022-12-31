from booking_factory import Booking_factory
from dbfunc import conn
from customer import Customer


class Show(object):
    def __init__(self, show_id, time, screen, listing):

        self.__show_id = show_id

        self.__time = time

        self.__available_vip_seats = screen.get_num_vip_seats()

        self.__available_upper_seats = screen.get_num_upper_seats()

        self.__available_lower_seats = screen.get_num_lower_seats()

        self.__bookings = dict()

        bookings = conn.select(
            "SELECT * FROM bookings WHERE SHOW_ID=%s AND ISNULL(REFUND)", self.__show_id)
        for b in bookings:
            self.__bookings[b["BOOKING_REFERENCE"]] = Booking_factory.get_booking_seat_hall(b["SEAT_TYPE"])(
                b["BOOKING_REFERENCE"], self, b["BOOKING_SEAT_COUNT"], b["BOOKING_DATE"], b["BOOKING_PRICE"], Customer("Someone", "7829748", b["CUSTOMER_EMAIL"]))

        self.__screen = screen

        self.__listing = listing

    def get_show_id(self):
        return self.__show_id

    def get_time(self):
        return self.__time

    def get_available_vip_seats(self):
        return self.__available_vip_seats

    def get_available_upper_seats(self):
        return self.__available_upper_seats

    def get_available_lower_seats(self):
        return self.__available_lower_seats

    def get_film(self):
        return self.__film

    def get_bookings(self):
        return self.__bookings

    def get_screen(self):
        return self.__screen

    def get_listing(self):
        return self.__listing

    def set_time(self, time):
        pass

    def set_available_vip_seats(self, seats):
        self.__available_vip_seats -= seats

    def set_available_upper_seats(self, seats):
        self.__available_upper_seats -= seats

    def set_available_lower_seats(self, seats):
        self.__available_lower_seats -= seats

    def add_booking(self, booking_reference, seat_hall, number_of_seats, date_of_booking, price, customer):
        booking = Booking_factory.get_booking_seat_hall(seat_hall)(
            booking_reference, self, number_of_seats, date_of_booking, price, customer)
        self.__bookings[booking_reference] = booking
        if booking.check_seats():
            del self.__bookings[booking_reference]
            return 0
        return booking

    def cancel_booking(self, Booking_reference):
        del self.__bookings[Booking_reference]

    def __str__(self):
        return str(self.__time)
