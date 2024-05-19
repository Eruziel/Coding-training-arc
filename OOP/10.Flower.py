class Flower:
    is_happy = False

    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements

    def water(self, quantity):

        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self):

        return f"{self.name} is happy" if self.is_happy else f"{self.name} is not happy"



tulip = Flower('Jack', 100)
tulip.water(50)
print(tulip.status())

