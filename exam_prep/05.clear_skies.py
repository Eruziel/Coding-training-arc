size = int(input())

matrix = []
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
for row in range(size):
    matrix.append([el for el in input()])
start = []
enemies = 0
for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'J':
            start = [row, col]
        elif matrix[row][col] == 'E':
            enemies += 1

armor = 300

while True:
    command = input()
    way = directions[command]

    row = start[0] + way[0]
    col = start[1] + way[1]

    if 0 <= row < size and 0 <= col < size:
        new_position = matrix[row][col]

        if new_position == 'E':
            enemies -= 1
            if enemies == 0:
                matrix[start[0]][start[1]] = '-'
                matrix[row][col] = 'J'
                print(f'Mission accomplished, you neutralized the aerial threat!')
                break
            else:
                armor -= 100
                if armor <= 0:
                    print(f'Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!')
                    matrix[start[0]][start[1]] = '-'
                    matrix[row][col] = 'J'
                    break

        elif new_position == 'R':
            armor = 300

        matrix[start[0]][start[1]] = '-'
        matrix[row][col] = 'J'
        start = [row, col]

[print(''.join(x)) for x in matrix]