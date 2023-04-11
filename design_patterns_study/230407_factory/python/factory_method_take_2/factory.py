from dataclasses import dataclass
import polygon


@dataclass
class FactoryPolygon:
    def create(self, num_sides: int) -> polygon.Polygon:
        if num_sides == 3:
            return polygon.Triangle()
        elif num_sides == 4:
            return polygon.Rectangle()
        elif num_sides == 5:
            return polygon.Pentagon()
        else:
            raise Exception("Sorry, we've got a problem...")
