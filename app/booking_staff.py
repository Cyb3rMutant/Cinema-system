"""
Authors:
    Rohaan Aslam (21017718)
    Benjamin Hussey (21022768)
    Yazeed Abu-Hummous (21014295)
Date: 08/01/2023
Module: Advanced Software Development 22/23
"""

import user
import cinema


class Booking_staff(user.User):
    def __init__(self, name: str, id: int, branch: cinema.Cinema):
        super(Booking_staff, self).__init__(name, id, branch)
