
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        ...

    @abstractmethod
    def refuel(self, fuel: int):
        ...


class Car(Vehicle):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        self.air_con_consumptions = 0.9

    def drive(self, distance) -> None:
        consumption = distance * (self.fuel_consumption + self.air_con_consumptions)
        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        self.air_con_consumptions = 1.6
        self.fuel_leak = 0.95

    def drive(self, distance) -> None:
        consumption = distance * (self.fuel_consumption + self.air_con_consumptions)
        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel) -> None:
        self.fuel_quantity += fuel * self.fuel_leak
        