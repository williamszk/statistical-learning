"""This is the concrete implementation of the Polygon types.
"""
from dataclasses import dataclass

class Polygon:
    pass

@dataclass
class Triangle(Polygon):
    def get(self):
        print("Hello from Triangle")

@dataclass
class Rectangle(Polygon):
    def get(self):
        print("Hello from Rectangle")

@dataclass
class Pentagon(Polygon):
    def get(self):
        print("Hello from Pentagon")