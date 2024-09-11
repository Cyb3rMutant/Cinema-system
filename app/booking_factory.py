"""
Authors:
    Rohaan Aslam (21017718)
    Benjamin Hussey (21022768)
    Yazeed Abu-Hummous (21014295)
Date: 08/01/2023
Module: Advanced Software Development 22/23
"""

from booking_lower_hall import Booking_lower_hall
from booking_upper_hall import Booking_upper_hall
from booking_vip_hall import Booking_vip_hall


class Booking_factory(object):
    @staticmethod
    def get_booking_seat_hall(type: str):
        types = {
            "lower": Booking_lower_hall,
            "upper": Booking_upper_hall,
            "vip": Booking_vip_hall,
        }

        if type not in types:
            raise Exception("%s booking type does not exist" % type)

        return types[type]
