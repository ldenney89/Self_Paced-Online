#!/usr/bin/env python3

from math import pi


class Circle:

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError("A positive radius value is required.")
        self._radius = val

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, val):
        if val < 0:
            raise ValueError("A positive radius value is required.")
        self._radius = val / 2

    @property
    def area(self):
        return self.radius * self.radius * pi

    @classmethod
    def from_diameter(cls, val):
        self = cls(val / 2)
        return self
