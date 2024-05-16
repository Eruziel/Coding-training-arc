size = int(input())

matrix = [[x for x in input()] for _ in range(size)]

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

start = []
for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'P':
            start = [row, col]

health = 100

while True:
    current_direction = input()
    move = directions[current_direction]

    new_row = start[0] + move[0]
    new_col = start[1] + move[1]

    if 0 <= new_row < size and 0 <= new_col < size:
        new_position = matrix[new_row][new_col]
        if new_position == 'M':
            health -= 40
            if health <= 0:
                health = 0
                matrix[start[0]][start[1]] = '-'
                matrix[new_row][new_col] = 'P'
                print(f"Player is dead. Maze over!\nPlayer's health: {health} units")
                break

        elif new_position == 'H':
            health += 15
            if health > 100:
                health = 100
        elif new_position == 'X':
            matrix[start[0]][start[1]] = '-'
            matrix[new_row][new_col] = 'P'
            print(f"Player escaped the maze. Danger passed!\nPlayer's health: {health} units")
            break

        matrix[start[0]][start[1]] = '-'
        matrix[new_row][new_col] = 'P'
        start = [new_row, new_col]

[print("".join(el)) for el in matrix]