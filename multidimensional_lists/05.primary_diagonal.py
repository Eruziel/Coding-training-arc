row = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(row)]

total_sum = 0

for i in range(row):
    total_sum += matrix[i][i]

print(total_sum)