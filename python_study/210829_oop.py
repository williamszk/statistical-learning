# https://pynative.com/python-object-oriented-programming-oop-exercise/

# OOP Exercise 1: Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
    def __init__(self, max_speed, mileage) -> None:
        self.max_speed = max_speed
        self.mileage = mileage


modelX = Vehicle(240, 18)
# print(modelX)

# -----------------------------------------------------------------------
# OOP Exercise 2: Create a Vehicle class without any variables and methods
class Vehicle2:
    pass

# -----------------------------------------------------------------------
# OOP Exercise 3: Create a child class Bus that will inherit all of the 
# variables and methods of the Vehicle class

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

an_example_bus = Bus("yellow bus", 180, 20)
print(an_example_bus)


# -----------------------------------------------------------------------
# OOP Exercise 4: Class Inheritance

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

my_bus = Bus("Mercedez Bus", 180, 20)
# print(my_bus.seating_capacity())

# -----------------------------------------------------------------------
# OOP Exercise 5: Define property that should have the same value for every class instance
class Vehicle:
    # Class attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

my_car = Car("Volks Golf", 120, 30)
my_bus = Bus("Mercedez Bus", 120, 30)

# print(f"{my_bus.color}, Vehicle name: {my_bus.name}, Speed: {my_bus.max_speed}, Milage: {my_bus.mileage}")
# print(f"{my_car.color}, Vehicle name: {my_car.name}, Speed: {my_car.max_speed}, Milage: {my_car.mileage}")

# -----------------------------------------------------------------------
# OOP Exercise 6: Class Inheritance

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        return super().fare()*1.1

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

# -----------------------------------------------------------------------
# OOP Exercise 7: Determine which class a given Bus object belongs to (Check type of an object)

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

# print(type(School_bus))

# -----------------------------------------------------------------------
# OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(isinstance(School_bus, Vehicle))






















