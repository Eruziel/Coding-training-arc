from project.food import Food


class Fruit(Food):
    def __init__(self, name, expiration_date):
        self.name = name
        Food.__init__(self, expiration_date)
