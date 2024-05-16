r, c = [int(x) for x in input().split(',')]

matrix = [[x for x in input()] for _ in range(r)]


directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
start = []
cheese = 0
for row in range(r):
    for col in range(c):
        if matrix[row][col] == 'M':
            start = [row, col]
        elif matrix[row][col] == 'C':
            cheese += 1

while True:
    command = input()

    if command == 'danger':
        print('Mouse will come back later!')
        break

    way = directions[command]

    row = start[0] + way[0]
    col = start[1] + way[1]

    if row < 0 or row >= r or col < 0 or col >= c:
        print('No more cheese for tonight!')
        break

    new_position = matrix[row][col]

    if new_position == 'C':
        cheese -= 1
        matrix[row][col] = '*'
        if cheese == 0:
            matrix[start[0]][start[1]] = '*'
            matrix[row][col] = 'M'
            print('Happy mouse! All the cheese is eaten, good night!')
            break
    elif new_position == 'T':
        matrix[start[0]][start[1]] = '*'
        matrix[row][col] = 'M'
        print('Mouse is trapped!')
        break
    elif new_position == '@':
        continue

    matrix[start[0]][start[1]] = '*'
    matrix[row][col] = 'M'
    start = [row, col]


[print(*el, sep='') for el in matrix]
