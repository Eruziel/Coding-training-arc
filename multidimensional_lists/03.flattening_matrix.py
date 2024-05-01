rows = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

flattened = []

for row in matrix:
    for el in row:
        flattened.append(el)

print(flattened)