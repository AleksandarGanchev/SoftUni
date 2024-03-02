class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: str, price: int) -> str:
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price

            return f"{animal.name} the {type(animal).__name__} added to the zoo"

        if self.__budget < price:
            return f"Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: str) -> str:
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary

        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        needed_budget = sum([a.money_for_care for a in self.animals])
        if self.__budget >= needed_budget:
            self.__budget -= needed_budget
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self):
        output = f"You have {len(self.animals)} animals"'\n'

        lions = [x for x in self.animals if x.__class__.__name__ == "Lion"]
        tigers = [x for x in self.animals if x.__class__.__name__ == "Tiger"]
        cheetahs = [x for x in self.animals if x.__class__.__name__ == "Cheetah"]

        output += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            output += f"{lion}\n"

        output += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            output += f"{tiger}\n"

        output += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            output += f"{cheetah}\n"

        return output[:-1]

    def workers_status(self):
        output = f"You have {len(self.workers)} workers\n"

        keepers = [x for x in self.workers if x.__class__.__name__ == "Keeper"]
        caretakers = [x for x in self.workers if x.__class__.__name__ == "Caretaker"]
        vets = [x for x in self.workers if x.__class__.__name__ == "Vet"]

        output += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            output += f"{keeper}\n"

        output += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            output += f"{caretaker}\n"

        output += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            output += f"{vet}\n"

        return output[:-1]
