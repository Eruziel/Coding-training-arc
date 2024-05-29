from functools import reduce


class Calculator:
    def add(*args):
        result = reduce(lambda x, y: x + y, args)
        return result

    def multiply(*args):
        result = reduce(lambda x, y: x * y, args)
        return result

    def divide(*args):
        result = reduce(lambda x, y: x / y if y != 0 else None, args)
        return result

    def subtract(*args):
        result = reduce(lambda x, y: x - y, args)
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 0))
print(Calculator.subtract(90, 20, -50, 43, 7))
