"""
Authors:
    Rohaan Aslam (21017718)
    Benjamin Hussey (21022768)
    Yazeed Abu-Hummous (21014295)
Date: 08/01/2023
Module: Advanced Software Development 22/23
"""

import customer


class Customers:
    __instance = None

    __customers = dict()

    def __init__(self):
        if Customers.__instance:
            raise Exception("there can only be one Conn instance!")

        Customers.__instance = self

    def __getitem__(self, key):
        return Customers.__customers[key]

    def __setitem__(self, key: str, value: customer.Customer):
        Customers.__customers[key] = value

    @staticmethod
    def get_customer(f):
        return Customers.__customers[f]

    def get_customers(self):
        return Customers.__customers

    def add_customer(self, customer_email, customer_name, customer_phone):
        Customers.__customers[customer_email] = customer.Customer(
            customer_name, customer_phone, customer_email
        )

    def update_customer(self, email, name, phone):
        Customers.__customers[email].set_name(name)
        Customers.__customers[email].set_phone(phone)
