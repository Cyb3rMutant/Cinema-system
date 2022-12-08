#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *
import customer
import receipt_generator
import show
import ticket_generator


# ˄


class Booking(object, metaclass=ABCMeta):
    # ˅

    # ˄

    def __init__(self, show, number_of_seats, date_of_booking, price, customer):

        self.__booking_reference = None   #is this meant to be a parameter in constructor or does it get pulled from db?

        self.__show = show

        self.__number_of_seats = number_of_seats

        self.__date_of_booking = date_of_booking

        self.__price = price

        self.__customer = customer

        self.__ticket_generator = None

        self.__receipt_generator = None

        # ˅
        pass
        # ˄

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

    @abstractmethod
    def get_ticket(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def get_receipt(self):
        # ˅
        pass
        # ˄

    # ˅

    # ˄


# ˅

# ˄
