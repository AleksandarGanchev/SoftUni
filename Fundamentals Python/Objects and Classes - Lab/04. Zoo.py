class Zoo:
    __animals = 0
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

    def get_info(self,species):

        total_length = len(self.mammals) + len(self.birds) + len(self.fishes)
        if species == 'mammal':
            return f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {total_length}"
        elif species == 'fish':
            return f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {total_length}"
        elif species == 'bird':
            return f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {total_length}"

name = input()
n = int(input())

zoo = Zoo(name)

for _ in range(n):
    species,name = input().split()
    zoo.add_animal(species, name)


species = input()
print(zoo.get_info(species))
