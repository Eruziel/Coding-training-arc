from collections import deque

rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input()] for _ in range(rows)]
start = []
game_won = False

directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

commands = deque(input())


def bunny_spread(diction: dict, some_rows: int, some_cols: int, matrx: list):
    bunny_coordinates = []
    for roww in range(some_rows):
        for coll in range(some_cols):
            if matrx[roww][coll] == 'B':
                bunny_start = [roww, coll]
                for key, value in diction.items():
                    roww = bunny_start[0] + diction[key][0]
                    coll = bunny_start[1] + diction[key][1]
                    if 0 <= roww < some_rows and 0 <= coll < some_cols and matrx[roww][coll] != 'B':
                        bunny_coordinates.append([roww, coll])

    for coordinates in bunny_coordinates:
        matrx[coordinates[0]][coordinates[1]] = 'B'


for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == 'P':
            start = [row, col]

while commands:

    current_direction = commands.popleft()
    current_position = matrix[start[0]][start[1]]
    row = start[0] + directions[current_direction][0]
    col = start[1] + directions[current_direction][1]

    if current_position == 'B':
        break

    elif row < 0 or row >= rows or col < 0 or col >= cols:
        game_won = True
        matrix[start[0]][start[1]] = '.'
        bunny_spread(directions, rows, cols, matrix)
        break

    elif matrix[row][col] == 'B':
        start = [row, col]
        bunny_spread(directions, rows, cols, matrix)
        break

    matrix[row][col] = 'P'
    matrix[start[0]][start[1]] = '.'
    start = [row, col]
    bunny_spread(directions, rows, cols, matrix)


[print(*x, sep='') for x in matrix]

if game_won:
    print(f'won: {start[0]} {start[1]}')

elif game_won is False:
    print(f'dead: {start[0]} {start[1]}')



