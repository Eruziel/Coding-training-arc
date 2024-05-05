rows = int(input())

matrix = [[x for x in input().split()] for _ in range(rows)]

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}


alice_pos = []
for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == 'A':
            alice_pos = [row, col]
            matrix[row][col] = '*'

total_tea = 0
row = alice_pos[0]
col = alice_pos[1]


while total_tea < 10:
    current_direction = input()
    move = directions[current_direction]

    row = alice_pos[0] + move[0]
    col = alice_pos[1] + move[1]

    if row < 0 or row >= rows or col < 0 or col >= rows:
        break

    if matrix[row][col].isdigit():
        total_tea += int(matrix[row][col])
        matrix[row][col] = '*'

    elif matrix[row][col] == 'R':
        matrix[row][col] = '*'
        break

    matrix[row][col] = '*'
    alice_pos = [row, col]

if total_tea >= 10:
    print('She did it! She went to the party.')
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(f"{' '.join(x for x in row)}")