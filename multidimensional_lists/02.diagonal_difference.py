rows = int(input())

matrix = [[int(x) for x in input().split()]for _ in range(rows)]

primary = 0
secondary = 0

for i in range(rows):
    primary += matrix[i][i]

index = -1
for j in range(rows):
    secondary += matrix[j][index]
    index -= 1

print(f'{abs(primary-secondary)}')