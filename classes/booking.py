import customer
from receipt_generator import Receipt_generator
import show
from ticket_generator import Ticket_generator


class Booking():
    seat_type = None

    def __init__(self, booking_reference, show, number_of_seats, date_of_booking, city_price, customer):
        # generate a custom one later on
        self._booking_reference = booking_reference

        self._show = show

        self._number_of_seats = number_of_seats

        self._date_of_booking = date_of_booking

        self._customer = customer

        self._price = self.calc_price(city_price) * number_of_seats

    def get_booking_reference(self):
        return self._booking_reference

    def get_show(self):
        return self._show

    def get_number_of_seats(self):
        return self._number_of_seats

    def get_date_of_booking(self):
        return self._date_of_booking

    def get_price(self):
        return self._price

    def get_customer(self):
        return self._customer

    def get_ticket(self):
        return Receipt_generator.gen_receipt(self)

    def get_receipt(self):
        return Ticket_generator.gen_ticket(self)

    def get_seat_type(self):
        return self.__class__.seat_type

    def calc_price(self, city_price):
        pass

    def as_list(self):
        pass
