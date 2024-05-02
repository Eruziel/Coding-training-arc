rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    command = input()
    if command == 'END':
        for i in matrix:
            print(*i)

        break

    action, *data = command.split()

    if action == 'Add':
        row = int(data[0])
        col = int(data[1])
        value = int(data[2])

        if 0 <= row <= len(matrix) - 1 and 0 <= col <= len(matrix) - 1:

            if matrix[row][col]:
                matrix[row][col] += value

        else:
            print('Invalid coordinates')
            continue

    elif action == 'Subtract':
        row = int(data[0])
        col = int(data[1])
        value = int(data[2])

        if 0 <= row <= len(matrix) - 1 and 0 <= col <= len(matrix) - 1:

            if matrix[row][col]:
                matrix[row][col] -= value

        else:
            print('Invalid coordinates')
            continue



