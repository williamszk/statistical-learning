
from dataclasses import dataclass
import concrete

@dataclass
class AbstractFactoryPolygon:
    def create_factory(self, color: str) -> concrete.FactoryPolygonColor:
        if color == "blue":
            return concrete.FactoryPolygonBlue()
        elif color == "red":
            return concrete.FactoryPolygonRed()
        elif color == "green":
            return concrete.FactoryPolygonGreen()
        else:
            raise Exception("Sorry, we've got a problem...")
