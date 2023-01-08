"""
Authors:
    Rohaan Aslam (21017718)
    Benjamin Hussey (21022768)
    Yazeed Abu-Hummous (21014295)
Date: 08/01/2023
Module: Advanced Software Development 22/23
"""
import booking


class Booking_lower_hall(booking.Booking):
    seat_type = "lower"

    def __init__(self, booking_reference, show, number_of_seats, date_of_booking, city_price, customer):
        super(Booking_lower_hall, self).__init__(booking_reference, show,
                                                 number_of_seats, date_of_booking, city_price, customer)
        show.set_available_lower_seats(number_of_seats)

    def calc_price(self, city_price):
        return city_price

    def check_seats(self):
        return self._show.get_available_lower_seats() < 0

    def as_list(self):
        return [self._booking_reference, self._number_of_seats, self._date_of_booking, self._price, self._show.get_show_id(), "lower"]

    def __del__(self):
        self._show.set_available_lower_seats(-self._number_of_seats)
