rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

bombs = [x for x in input().split()]

alive_cells = 0
total_sum = 0

directions = {
    'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1],
    'upper_left_d': [-1, -1], 'upper_right_d': [-1, 1],
    'lower_left_d': [1, -1], 'lower_right_d': [1, 1]
}

for b in bombs:
    row = int(b[0])
    col = int(b[2])
    current_bomb = matrix[row][col]
    if current_bomb > 0:
        for way in directions.values():
            row += way[0]
            col += way[1]
            if 0 <= row < rows and 0 <= col < rows:
                if matrix[row][col] > 0:
                    matrix[row][col] -= current_bomb

            row = int(b[0])
            col = int(b[2])
        matrix[int(b[0])][int(b[2])] = 0


for i in matrix:
    for num in i:
        if num > 0:
            alive_cells += 1
            total_sum += num

print(f'Alive cells: {alive_cells}')
print(f'Sum: {total_sum}')
[print(*el) for el in matrix]
