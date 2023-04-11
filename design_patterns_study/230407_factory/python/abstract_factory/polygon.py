"""This is the concrete implementation of the Polygon types.
"""
from dataclasses import dataclass
from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def get(self):
        pass


@dataclass
class BlueTriangle(Polygon):
    def get(self):
        print("Hello from BlueTriangle")


@dataclass
class RedTriangle(Polygon):
    def get(self):
        print("Hello from RedTriangle")


@dataclass
class GreenTriangle(Polygon):
    def get(self):
        print("Hello from GreenTriangle")


@dataclass
class BlueRectangle(Polygon):
    def get(self):
        print("Hello from BlueRectangle")


@dataclass
class RedRectangle(Polygon):
    def get(self):
        print("Hello from RedRectangle")


@dataclass
class GreenRectangle(Polygon):
    def get(self):
        print("Hello from GreenRectangle")


@dataclass
class BluePentagon(Polygon):
    def get(self):
        print("Hello from BluePentagon")


@dataclass
class RedPentagon(Polygon):
    def get(self):
        print("Hello from RedPentagon")


@dataclass
class GreenPentagon(Polygon):
    def get(self):
        print("Hello from GreenPentagon")
