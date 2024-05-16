size = int(input())

matrix = [[x for x in input()] for _ in range(size)]

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
start = []
for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'G':
            start = [row, col]

money = 100

while True:
    direction = input()
    if direction == 'end':
        print(f'End of the game. Total amount: {money}$')
        break
    way = directions[direction]

    row = start[0] + way[0]
    col = start[1] + way[1]

    if row >= size or col >= size:
        money = 0
        matrix[start[0]][start[1]] = '-'
        print('Game over! You lost everything!')

    if 0 <= row < size and 0 <= col < size:
        new_position = matrix[row][col]

        if new_position == 'W':
            money += 100
        elif new_position == 'P':
            money -= 200
            if money <= 0:
                print('Game over! You lost everything!')
                matrix[start[0]][start[1]] = '-'
                matrix[row][col] = 'G'
                break
        elif new_position == 'J':
            money += 100000
            print('You win the Jackpot!')
            print(f'End of the game. Total amount: {money}$')

            matrix[start[0]][start[1]] = '-'
            matrix[row][col] = 'G'
            break

        matrix[start[0]][start[1]] = '-'
        matrix[row][col] = 'G'
        start = [row, col]

if money > 0:
    [print("".join(el)) for el in matrix]