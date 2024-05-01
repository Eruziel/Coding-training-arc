rows = int(input())

matrix = [[x for x in input()] for _ in range(rows)]

symbol = input()

for i in range(rows):
    for y in range(rows):
        if matrix[i][y] == symbol:
            print(f"({i}, {y})")
            exit()

print(f'{symbol} does not occur in the matrix')