r, c = [int(x) for x in input().split()]

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

matrix = [[x for x in input()] for _ in range(r)]
start = []
boy = []

for row in range(r):
    for col in range(c):
        if matrix[row][col] == 'B':
            start = [row, col]
            boy = [row, col]
while True:
    command = input()
    way = directions[command]

    row = start[0] + way[0]
    col = start[1] + way[1]

    if row < 0 or row >= r or col < 0 or col >= c:
        print('The delivery is late. Order is canceled.')
        matrix[boy[0]][boy[1]] = ' '
        break

    if matrix[row][col] != '*' and (0 <= row < r and 0 <= col < c):
        new_position = matrix[row][col]
        if new_position == 'P':
            matrix[row][col] = 'R'

            print('Pizza is collected. 10 minutes for delivery.')

        elif new_position == 'A':
            print('Pizza is delivered on time! Next order...')
            matrix[row][col] = 'P'
            break

        if matrix[row][col] != 'R' and matrix[row][col] != 'P' and matrix[row][col] != 'B':
            matrix[row][col] = '.'
        start = [row, col]



[print(*el, sep='') for el in matrix]
