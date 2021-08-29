# https://www.youtube.com/watch?v=aIdzBGzaxUo&ab_channel=RealPython

# String Conversion in Python: When to Use __repr__ vs __str__

# Represent Python class as string

class Car:
    def __init__(self, color, mileage) -> None:
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"A {self.color} car, with {self.mileage} of mileage."

    def __repr__(self):
        return f"A {self.color} car, with {self.mileage} of mileage. From repr!"



my_car = Car('red', 8790)
# print(my_car)

# --------------------------------------

import datetime
today = datetime.date.today()

# repr(today)
# str(today)

# from the output of repr we can copy and paste the output
# and it is valid code



class Car:
    def __init__(self, color, mileage) -> None:
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"A {self.color} car, with {self.mileage} of mileage."

    def __repr__(self):
        return f"Car('{self.color}', {self.mileage})"


my_car = Car('red', 8790)
# print(repr(my_car))



# --------------------------------------

class Car:
    def __init__(self, color, mileage) -> None:
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"A {self.color} car, with {self.mileage} of mileage."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.color}', {self.mileage})"


my_car = Car('red', 8790)


[my_car, my_car, my_car]