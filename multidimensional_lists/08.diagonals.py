rows = int(input())

matrix = [[int(x) for x in input().split(', ')]for _ in range(rows)]

primary = 0
secondary = 0
primary_list = []
secondary_list = []
for i in range(rows):
    primary += matrix[i][i]
    primary_list.append(matrix[i][i])

index = -1
for j in range(rows):
    secondary += matrix[j][index]
    secondary_list.append(matrix[j][index])
    index -= 1

print(f'Primary diagonal: {", ".join(str(x) for x in primary_list)}. Sum: {primary}')
print(f'Secondary diagonal: {", ".join(str(x) for x in secondary_list)}. Sum: {secondary}')

