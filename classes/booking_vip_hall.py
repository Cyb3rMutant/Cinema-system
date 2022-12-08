#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import booking


# ˄


class Booking_vip_hall(booking.Booking):
    # ˅

    # ˄

    def __init__(self, show, number_of_seats, date_of_booking, price, customer):

        self.__booking_reference = None

        self.__show = show

        self.__number_of_seats = number_of_seats

        self.__date_of_booking = date_of_booking

        self.__price = price

        self.__customer = customer

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

    # ˅

    # ˄


# ˅

# ˄
