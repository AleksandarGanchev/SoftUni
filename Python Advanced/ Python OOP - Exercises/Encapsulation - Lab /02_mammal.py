class Mammal:
    __kingdom = "animals"

    def __init__(self, name: str, type: str, sound: str):
        self.sound = sound
        self.type = type
        self.name = name

    def make_sound(self) -> str:
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self) -> str:
        return Mammal.__kingdom

    def info(self) -> str:
        return f"{self.name} is of type {self.type}"
