from project.food.main_dish import MainDish


class Salmon(MainDish):
    GRAMS = 22

    def __init__(self, name, price, grams):
        super().__init__(name, price, Salmon.grams)
