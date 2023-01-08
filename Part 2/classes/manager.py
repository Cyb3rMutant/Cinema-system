"""
Authors:
    Rohaan Aslam (21017718)
    Benjamin Hussey (21022768)
    Yazeed Abu-Hummous (21014295)
Date: 08/01/2023
Module: Advanced Software Development 22/23
"""
import admin
import cinema


class Manager(admin.Admin):
    def __init__(self, name: str, id: int, branch: cinema.Cinema):
        super(Manager, self).__init__(name, id, branch)
