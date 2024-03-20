from project import Bird
from project import Meat, Seed, Fruit, Vegetable


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)
        self.desired_food = [Meat]

    @property
    def weight_gain(self):
        return 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)
        self.desired_food = [Meat, Vegetable, Fruit, Seed]

    @property
    def weight_gain(self):
        return 0.35

    def make_sound(self):
        return "Cluck"
