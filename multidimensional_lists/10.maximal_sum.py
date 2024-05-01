rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()]for _ in range(rows)]

max_sum = float('-inf')
max_matrix = []
for i in range(rows-2):

    for j in range(cols-2):
        current_sum = 0
        current_sum += (matrix[i][j] + matrix[i+1][j+1] + matrix[i+1][j] + matrix[i][j+1] + matrix[i+2][j+2]
                        + matrix[i+2][j+1] + matrix[i+1][j+2] + matrix[i+2][j] + matrix[i][j+2])
        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix.clear()

            max_matrix.append([matrix[i][j], matrix[i][j+1], matrix[i][j+2]])
            max_matrix.append([matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j+2]])
            max_matrix.append([matrix[i+2][j], matrix[i+2][j+1], matrix[i+2][j+2]])


print(f'Sum = {max_sum}')

for row in max_matrix:
    print(f'{" ".join(str(el) for el in row) }')
