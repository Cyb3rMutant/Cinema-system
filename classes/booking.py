from datetime import datetime
from seat import Seat
from show import Show


class Booking(object):
    def __init__(self, booking_reference: str, showing: Show, seats: Seat, number_of_tickets: int, date_of_booking: datetime, price: int, name: str, phone: str, email: str):

        self.__booking_reference = booking_reference

        self.__showing = showing

        self.__seats = seats

        self.__number_of_tickets = number_of_tickets

        self.__date_of_booking = date_of_booking

        self.__price = price

        self.__name = name

        self.__phone = phone

        self.__email = email

    def get_reciept(self):
        return self.__reciept

    def get_ticket(self):
        return self.__ticket

    def get_booking_reference(self):
        return self.__booking_reference

    def get_showing(self):
        return self.__showing

    def get_seats(self):
        return self.__seats

    def get_number_of_tickets(self):
        return self.__number_of_tickets

    def get_date_of_booking(self):
        return self.__date_of_booking

    def get_price(self):
        return self.__price

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email
