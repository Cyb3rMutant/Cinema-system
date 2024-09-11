"""
Authors:
    Rohaan Aslam (21017718)
    Benjamin Hussey (21022768)
    Yazeed Abu-Hummous (21014295)
Date: 08/01/2023
Module: Advanced Software Development 22/23
"""

from booking_staff import Booking_staff
from admin import Admin
from manager import Manager


class User_factory:
    @staticmethod
    def get_user_type(type: str):
        types = {"booking_staff": Booking_staff, "admin": Admin, "manager": Manager}

        if type not in types:
            raise Exception("%s user type does not exist" % type)

        return types[type]


if __name__ == "__main__":
    admin = User_factory.get_user_type("admin")("yazee", 1, None)
