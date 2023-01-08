"""
Authors:
    Rohaan Aslam (21017718)
    Benjamin Hussey (21022768)
    Yazeed Abu-Hummous (21014295)
Date: 08/01/2023
Module: Advanced Software Development 22/23
"""
import cinema


class User():
    def __init__(self, name: str, id: int, branch: cinema.Cinema):

        self._name = name

        self._id = id

        self._branch = branch

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_branch(self):
        return self._branch

    def __str__(self):
        return f"{self.get_id()}: {self.get_name()}[{self.__class__.__name__}]"
