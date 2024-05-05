from collections import deque

rows = int(input())

commands = deque(input().split())

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

matrix = [[x for x in input().split()] for _ in range(rows)]

start = []
coal_collected = 0
coal_pieces = 0
for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == 's':
            start = [row, col]
        elif matrix[row][col] == 'c':
            coal_pieces += 1

while commands:

    current_direction = commands.popleft()
    row = start[0] + directions[current_direction][0]
    col = start[1] + directions[current_direction][1]

    if 0 <= row < rows and 0 <= col < rows:
        if matrix[row][col] == 'c':
            matrix[row][col] = '*'
            coal_collected += 1
            if coal_collected == coal_pieces:
                start = [row, col]
                print(f'You collected all coal! ({start[0]}, {start[1]})')
                exit()
        elif matrix[row][col] == 'e':
            start = [row, col]
            print(f'Game over! ({start[0]}, {start[1]})')
            exit()
        start = [row, col]

print(f'{coal_pieces - coal_collected} pieces of coal left. ({start[0]}, {start[1]})')