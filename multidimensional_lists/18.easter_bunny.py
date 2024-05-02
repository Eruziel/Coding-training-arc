rows = int(input())
matrix = []
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
max_eggs = float('-inf')
correct_way = ''
correct_path = []
bunny = []

for row in range(rows):
    matrix.append(input().split())
    for col in range(rows):
        if matrix[row][col] == 'B':
            bunny = [row, col]

for direction, move in directions.items():
    eggs = 0
    curr_egg_matrix = []
    row = bunny[0] + move[0]
    col = bunny[1] + move[1]

    while 0 <= row < rows and 0 <= col < rows:
        if matrix[row][col] == 'X':
            break
        eggs += int(matrix[row][col])
        curr_egg_matrix.append([row, col])
        row += move[0]
        col += move[1]

    if eggs > max_eggs and curr_egg_matrix:
        max_eggs = eggs
        correct_way = direction
        correct_path = curr_egg_matrix


print(correct_way)

[print(el) for el in correct_path]

print(max_eggs)