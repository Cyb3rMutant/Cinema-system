from customer import Customer
from datetime import datetime
from seat import Seat
from show import Show


class Booking():
    def __init__(self, booking_reference: str, showing: Show, seats: Seat, number_of_tickets: int, date_of_booking: datetime, price: int, customer: Customer):

        self.__booking_reference = booking_reference

        self.__showing = showing

        self.__seats = seats

        self.__number_of_tickets = number_of_tickets

        self.__date_of_booking = date_of_booking

        self.__price = price

        self.__customer = customer

    def get_reciept(self):
        pass

    def get_ticket(self):
        pass

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

    def get_customer(self):
        return self.__customer
