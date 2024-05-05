n = 5
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

matrix = []

position = []
total_targets = 0
hit_targets = []

for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == 'A':
            position = [row, col]
        elif matrix[row][col] == 'x':
            total_targets += 1

commands = int(input())
current_position = ''
for _ in range(commands):

    action = input().split()

    if action[0] == 'move':
        steps = int(action[2])
        way = action[1]
        if way == 'up':
            row = position[0] - steps
            col = position[1]
        elif way == 'down':
            row = position[0] + steps
            col = position[1]
        elif way == 'left':
            row = position[0]
            col = position[1] - steps
        else:
            row = position[0]
            col = position[1] + steps

        if 0 <= row < n and 0 <= col < n and matrix[row][col] == '.':
            matrix[row][col] = 'A'
            matrix[position[0]][position[1]] = '.'
            position = [row, col]

    elif action[0] == 'shoot':
        row = position[0] + directions[action[1]][0]
        col = position[1] + directions[action[1]][1]
        while 0 <= row < 5 and 0 <= col < 5:
            if matrix[row][col] == 'x':
                total_targets -= 1
                hit_targets.append([row, col])
                matrix[row][col] = '.'
                break

            row += directions[action[1]][0]
            col += directions[action[1]][1]

        if total_targets == 0:
            print(f'Training completed! All {len(hit_targets)} targets hit.')
            break

if total_targets > 0:
    print(f'Training not completed! {total_targets} targets left.')

[print(x) for x in hit_targets]