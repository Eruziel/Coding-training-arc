size = int(input())

matrix = [[x for x in input()]for _ in range(size)]
start = []
destroyed = 0
hits = 3
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for r in range(size):
    for c in range(size):
        if matrix[r][c] == 'S':
            start = [r, c]

while True:

    direction = input()
    way = directions[direction]

    row = start[0] + way[0]
    col = start[1] + way[1]

    if not (0 > row or row >= size or 0 > col or col >= size):
        new_position = matrix[row][col]

        if new_position == '*':
            hits -= 1
            if hits == 0:
                matrix[start[0]][start[1]] = '-'
                matrix[row][col] = 'S'
                print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
                break
        elif new_position == 'C':
            destroyed += 1
            if destroyed == 3:
                matrix[start[0]][start[1]] = '-'
                matrix[row][col] = 'S'
                print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                break

        matrix[start[0]][start[1]] = '-'
        matrix[row][col] = 'S'
        start = [row, col]

[print(*el, sep='') for el in matrix]

