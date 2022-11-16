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

        self.__booking_reference = None

        self.__show = None

        self.__number_of_seats = None

        self.__date_of_booking = None

        self.__price = None

        self.__customer = None

        self.__ticket_generator = None

        self.__receipt_generator = None

        # ˅
        pass
        # ˄

    def get_booking_reference(self):
        # ˅
        pass
        # ˄

    def get_show(self):
        # ˅
        pass
        # ˄

    def get_number_of_seats(self):
        # ˅
        pass
        # ˄

    def get_date_of_booking(self):
        # ˅
        pass
        # ˄

    def get_price(self):
        # ˅
        pass
        # ˄

    def get_customer(self):
        # ˅
        pass
        # ˄

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
