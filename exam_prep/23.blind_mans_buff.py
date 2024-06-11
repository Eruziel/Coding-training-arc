r, c = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(r)]

start = []

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for row in range(r):
    for col in range(c):
        if matrix[row][col] == 'B':
            start = [row, col]
            break
moves = 0
touched = 0

while True:
    if touched == 3:
        break
    command = input()
    if command == 'Finish':
        break
    if command in directions:
        direction = directions[command]

        row = start[0] + direction[0]
        col = start[1] + direction[1]

        if 0 <= row < r and 0 <= col < c:
            if matrix[row][col] == "O":
                continue
            elif matrix[row][col] == '-':
                matrix[start[0]][start[1]] = '-'
                moves += 1

            elif matrix[row][col] == 'P':
                touched += 1
                moves += 1
                matrix[start[0]][start[1]] = '-'
                matrix[row][col] = '-'

            start = [row, col]

print('Game over!')
print(f"Touched opponents: {touched} Moves made: {moves}")