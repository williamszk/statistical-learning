from dataclasses import dataclass
from abc import ABC, abstractmethod
import polygon


class FactoryPolygonColor(ABC):
    @abstractmethod
    def create(self, num_sides: int) -> polygon.Polygon:
        pass

@dataclass
class FactoryPolygonBlue(FactoryPolygonColor):
    def create(self, num_sides: int) -> polygon.Polygon:
        if num_sides == 3:
            return polygon.BlueTriangle()
        elif num_sides == 4:
            return polygon.BlueRectangle()
        elif num_sides == 5:
            return polygon.BluePentagon()
        else:
            raise Exception("Sorry, we've got a problem...")


@dataclass
class FactoryPolygonRed(FactoryPolygonColor):
    def create(self, num_sides: int) -> polygon.Polygon:
        if num_sides == 3:
            return polygon.RedTriangle()
        elif num_sides == 4:
            return polygon.RedRectangle()
        elif num_sides == 5:
            return polygon.RedPentagon()
        else:
            raise Exception("Sorry, we've got a problem...")


@dataclass
class FactoryPolygonGreen(FactoryPolygonColor):
    def create(self, num_sides: int) -> polygon.Polygon:
        if num_sides == 3:
            return polygon.GreenTriangle()
        elif num_sides == 4:
            return polygon.GreenRectangle()
        elif num_sides == 5:
            return polygon.GreenPentagon()
        else:
            raise Exception("Sorry, we've got a problem...")
