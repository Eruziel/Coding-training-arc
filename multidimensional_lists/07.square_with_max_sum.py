row, col = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split(', ')] for _ in range(row)]

max_value = float('-inf')
max_matrix = []
for i in range(row-1):

    for j in range(col-1):
        total_sum = 0
        total_sum += matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1]

        if total_sum > max_value:
            max_value = total_sum
            max_matrix.clear()
            max_matrix.append(matrix[i][j])
            max_matrix.append(matrix[i][j+1])
            max_matrix.append(matrix[i+1][j])
            max_matrix.append(matrix[i+1][j+1])


print(f"{' '.join(str(x) for x in max_matrix[:2])}")
print(f"{' '.join(str(x) for x in max_matrix[2:])}")
print(max_value)


