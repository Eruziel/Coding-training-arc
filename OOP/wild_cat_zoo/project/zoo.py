from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget - price >= 0 and self.__animal_capacity > len(self.animals):
            self.__budget -= price

            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price and self.__animal_capacity > len(self.animals):
            return 'Not enough budget'

        return 'Not enough space for animal'

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= len(self.workers):
            return 'Not enough space for worker'

        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name):
        try:
            fired = next(filter(lambda w: w.name == worker_name, self.workers))
            self.workers.remove(fired)
            return f'{worker_name} fired successfully'
        except StopIteration:
            return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        total_salary = sum([i.salary for i in self.workers])
        if self.__budget - total_salary < 0:
            return 'You have no budget to pay your workers. They are unhappy'
        self.__budget -= total_salary
        return f'You payed your workers. They are happy. Budget left: {self.__budget}'

    def tend_animals(self):
        total_money = sum([i.money_for_care for i in self.animals])
        if self.__budget >= total_money:
            self.__budget -= total_money
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):

        lions = []
        for i in self.animals:
            if i.__class__.__name__ == 'Lion':
                lions.append(i)

        result = f"You have {len(self.animals)} animals\n"
        result += f'----- {len(lions)} Lions:\n'
        for lion in lions:
            result += f"{lion}\n"

        tigers = []
        for i in self.animals:
            if i.__class__.__name__ == 'Tiger':
                tigers.append(i)
        result += f'----- {len(tigers)} Tigers:\n'
        for tiger in tigers:
            result += f"{tiger}\n"

        cheetahs = []
        for i in self.animals:
            if i.__class__.__name__ == 'Cheetah':
                cheetahs.append(i)
        result += f'----- {len(cheetahs)} Cheetahs:\n'
        for cheetah in cheetahs:
            result += f"{cheetah}\n"

        return result[:-1]

    def workers_status(self):
        keepers = []
        for i in self.workers:
            if i.__class__.__name__ == 'Keeper':
                keepers.append(i)

        result = f"You have {len(self.workers)} workers\n"
        result += f'----- {len(keepers)} Keepers:\n'
        for keeper in keepers:
            result += f"{keeper}\n"

        caretakers = []
        for i in self.workers:
            if i.__class__.__name__ == 'Caretaker':
                caretakers.append(i)
        result += f'----- {len(caretakers)} Caretakers:\n'
        for care in caretakers:
            result += f"{care}\n"

        vets = []
        for i in self.workers:
            if i.__class__.__name__ == 'Vet':
                vets.append(i)
        result += f'----- {len(vets)} Vets:\n'
        for vet in vets:
            result += f"{vet}\n"

        return result[:-1]
