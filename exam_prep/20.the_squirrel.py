from collections import deque
size = int(input())
turns = deque(x for x in input().split(', '))
matrix = [[x for x in input()] for _ in range(size)]


directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
start = []
hazel = 0
for row in range(size):
    for col in range(size):
        if matrix[row][col] == 's':
            start = [row, col]

while turns:
    current_direction = turns.popleft()
    way = directions[current_direction]

    row = start[0] + way[0]
    col = start[1] + way[1]

    if row < 0 or row >= size or col < 0 or col >= size:
        print('The squirrel is out of the field.')
        print(f'Hazelnuts collected: {hazel}')
        exit()

    elif matrix[row][col] == 't':
        print('Unfortunately, the squirrel stepped on a trap...')
        print(f'Hazelnuts collected: {hazel}')
        exit()

    elif matrix[row][col] == 'h':
        hazel += 1
        matrix[row][col] = '*'
        if hazel == 3:
            print('Good job! You have collected all hazelnuts!')
            print(f'Hazelnuts collected: {hazel}')
            exit()
    start = [row, col]

print('There are more hazelnuts to collect.')
print(f'Hazelnuts collected: {hazel}')

