import customer
from receipt_generator import Receipt_generator
import show
from ticket_generator import Ticket_generator
import random


class Booking():
    def __init__(self, show, number_of_seats, date_of_booking, city_price, customer):
        # generate a custom one later on
        self.__booking_reference = random.randint(100000, 999999)

        self.__show = show

        self.__number_of_seats = number_of_seats

        self.__date_of_booking = date_of_booking

        self.__customer = customer

        self.__price = self.calc_price(city_price) * number_of_seats

    def get_booking_reference(self):
        return self.__booking_reference

    def get_show(self):
        return self.__show

    def get_number_of_seats(self):
        return self.__number_of_seats

    def get_date_of_booking(self):
        return self.__date_of_booking

    def get_price(self):
        return self.__price

    def get_customer(self):
        return self.__customer

    def get_ticket(self):
        return Receipt_generator.gen_receipt(self)

    def get_receipt(self):
        return Ticket_generator.gen_ticket(self)

    def calc_price(self, city_price):
        pass
