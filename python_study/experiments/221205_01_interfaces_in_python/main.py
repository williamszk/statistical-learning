""" How can we implement interfaces in Python?
"""
from abc import ABC, abstractmethod 

def main():
    boeing = Airplane()
    volkswagen = Car()

class Vehicle(ABC):
    @abstractmethod
    def turn_on():
        pass

    @abstractmethod
    def accelerate():
        pass

class Airplane(Vehicle):
    def turn_on():
        print("The airplane is turning on.")

    def accelerate():
        print("The airplane is accelerating.")

class Car(Vehicle):
    def turn_on():
        print("The car is turning on.")

    def accelerate():
        print("The car is accelerating.")

if __name__ == "__main__":
    main()