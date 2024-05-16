size = int(input())

matrix = [[x for x in input()] for _ in range(size)]

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
start = []
for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'S':
            start = [row, col]

collected = 0
while True:
    command = input()
    if command == 'collect the nets':
        break

    move = directions[command]
    row = start[0] + move[0]
    col = start[1] + move[1]

    if row < 0:
        row = size - 1
    elif row >= size:
        row = 0

    if col < 0:
        col = size - 1
    elif col >= size:
        col = 0

    new_position = matrix[row][col]
    if new_position == 'W':
        collected = 0
        print(f"You fell into a whirlpool! "
              f"The ship sank and you lost the fish you caught. Last coordinates of the ship: [{row},{col}]")
        exit()
    elif new_position.isdigit():
        collected += int(new_position)

    matrix[start[0]][start[1]] = '-'
    matrix[row][col] = 'S'
    start = [row, col]

if collected >= 20:
    print('Success! You managed to reach the quota!')
elif collected < 20:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - collected} tons of fish more.")

if collected > 0:
    print(f'Amount of fish caught: {collected} tons.')


[print("".join(el)) for el in matrix]