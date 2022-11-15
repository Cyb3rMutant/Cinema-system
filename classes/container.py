#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *


# ˄


class Container(object, metaclass=ABCMeta):
    __instance = None

    @abstractmethod
    def __init__(self):
        self.elements = dict()
        if Container.__instance:
            raise Exception("there can only be one Conn instance!")

        Container.__instance = self

    @abstractmethod
    def get_elements(self):
        return self.elements

    @abstractmethod
    def add_element(self):
        pass

    @abstractmethod
    def remove_element(self):
        pass
