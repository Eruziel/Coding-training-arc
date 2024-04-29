some_string = input()

symbols = {}

for el in some_string:
    if el not in symbols.keys():
        symbols[el] = 0

    symbols[el] += 1


for key, value in sorted(symbols.items()):
    print(f'{key}: {value} time/s')