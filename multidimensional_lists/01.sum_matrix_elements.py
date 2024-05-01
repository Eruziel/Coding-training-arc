row, col = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split(', ')]for _ in range(row)]

total_sum = 0

for row in matrix:
    total_sum += sum(row)

print(total_sum)
print(matrix)