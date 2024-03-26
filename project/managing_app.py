from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    VALID_TYPES = {"PassengerCar": PassengerCar,
                   "CargoVan": CargoVan
                   }

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):

        if vehicle_type not in ManagingApp.VALID_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        vehicle = ManagingApp.VALID_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point:
                if route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."

                elif route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."

                elif route.length > length:
                    route.is_locked = True

        new_route = Route(start_point, end_point, length, len(self.routes) + 1)
        self.routes.append(new_route)


        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        route = [r for r in self.routes if r.route_id == route_id][0]

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()

        elif not is_accident_happened:
            user.increase_rating()

        return vehicle.__str__()

    def repair_vehicles(self, count: int):

        vehicles_for_repair = [v for v in self.vehicles if v.is_damaged]
        for vehicle in sorted(vehicles_for_repair, key=lambda x: (x.brand, x.model))[:count]:
            vehicle.recharge()
            vehicle.change_status()

        return f"{len(vehicles_for_repair[:count])} vehicles were successfully repaired!"

    def users_report(self):
        output = ["*** E-Drive-Rent ***"]

        for user in sorted(self.users, key=lambda x: -x.rating):
            output.append(user.__str__())

        return '\n'.join(output)


# app = ManagingApp()
# print(app.register_user( 'Tisha', 'Reenie', '7246506' ))
# print(app.register_user( 'Bernard', 'Remy', 'CDYHVSR68661'))
# print(app.register_user( 'Mack', 'Cindi', '7246506'))
# print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))
# print(app.upload_vehicle( 'PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))
# print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))
# print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))
# print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))
# print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))
# print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))
# print(app.allow_route('SOF', 'PLD', 144))
# print(app.allow_route('BUR', 'VAR', 87))
# print(app.allow_route('BUR', 'VAR', 87))
# print(app.allow_route('SOF', 'PLD', 184))
# print(app.allow_route('BUR', 'VAR', 86.999))
# print(app.make_trip('CDYHVSR68661', '5UNM315', 3, False))
# print(app.make_trip('7246506', 'CWP8032', 1, True))
# print(app.make_trip('7246506', 'COUN199728', 1, False))
# print(app.make_trip('CDYHVSR68661', 'CWP8032', 3, False))
# print(app.make_trip('CDYHVSR68661', '5UNM315', 2, False))
# print(app.repair_vehicles(2))
# print(app.repair_vehicles(20))
# print(app.users_report())
