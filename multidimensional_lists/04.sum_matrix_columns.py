row, col = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split()] for _ in range(row)]

for i in range(col):
    col_total = 0
    for y in range(row):
        col_total += matrix[y][i]
    print(col_total)