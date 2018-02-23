#!/bin/env python3


class Vehicle:

    def __init__(self, num_wheels):
        self.num_wheels = num_wheels

    def print_wheels(self):
        print("I'm running on", self.num_wheels, "wheels!")


my_vehicle = Vehicle(3)
my_vehicle.print_wheels()

other_vehicle = Vehicle(2)
other_vehicle.print_wheels()


class Car(Vehicle):
    def __init__(self, color):
        super().__init__(4)
        self.color = color


my_car = Car('red')
my_car.print_wheels()
print(my_car.color)
