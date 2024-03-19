from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region):
        super().__init__(name, weight, living_region)
        self.desired_food = [Vegetable, Fruit]

    @property
    def weight_gain(self) -> float:
        return 0.10

    def make_sound(self) -> str:
        return "Squeak"


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region):
        super().__init__(name, weight, living_region)
        self.desired_food = [Meat]

    @property
    def weight_gain(self) -> float:
        return 0.40

    def make_sound(self) -> str:
        return "Woof!"


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region):
        super().__init__(name, weight, living_region)
        self.desired_food = [Vegetable, Meat]

    @property
    def weight_gain(self) -> float:
        return 0.30

    def make_sound(self) -> str:
        return "Meow"


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region):
        super().__init__(name, weight, living_region)
        self.desired_food = [Meat]

    @property
    def weight_gain(self) -> float:

        return 1.00

    def make_sound(self) -> str:
        return "ROAR!!!"
