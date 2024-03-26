from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, 450.00)

    def drive(self, mileage: float):
        reduce_battery_by = round((mileage / self.max_mileage) * 100)
        self.battery_level -= reduce_battery_by





