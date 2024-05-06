def rectangle(a, b):
    result = 0
    if not isinstance(a, int) or not isinstance(b, int):
        return 'Enter valid values!'

    def area():
        return a * b

    def perimeter():
        return 2 * a + 2 * b

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


print(rectangle('2', 10))

