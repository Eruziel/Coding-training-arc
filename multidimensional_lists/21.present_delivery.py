presents = int(input())

n = int(input())
matrix = []
santa = []
nice_kids = 0
nice_presents = 0
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'S':
            santa = [row, col]
        elif matrix[row][col] == 'V':
            nice_kids += 1

while presents:
    command = input()

    if command == 'Christmas morning':
        break

    row = santa[0] + directions[command][0]
    col = santa[1] + directions[command][1]

    if 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == 'V':
            presents -= 1
            nice_kids -= 1
            nice_presents += 1
            matrix[santa[0]][santa[1]] = '-'
            matrix[row][col] = 'S'
            santa = [row, col]
            if nice_kids == 0:
                break
        elif matrix[row][col] == 'C':
            matrix[santa[0]][santa[1]] = '-'
            matrix[row][col] = 'S'
            santa = [row, col]
            for way, move in directions.items():
                row = santa[0] + move[0]
                col = santa[1] + move[1]
                if 0 <= row < n and 0 <= col < n:
                    if matrix[row][col] == 'V':
                        presents -= 1
                        nice_kids -= 1
                        nice_presents += 1
                        if nice_kids == 0:
                            break
                    elif matrix[row][col] == 'X':
                        presents -= 1

                    matrix[row][col] = '-'
        else:
            matrix[santa[0]][santa[1]] = '-'
            matrix[row][col] = 'S'
            santa = [row, col]

if presents == 0 and nice_kids > 0:
    print('Santa ran out of presents!')

[print(*x) for x in matrix]

if nice_kids == 0:
    print(f'Good job, Santa! {nice_presents} happy nice kid/s. ')
else:
    print(f'No presents for {nice_kids} nice kid/s.')