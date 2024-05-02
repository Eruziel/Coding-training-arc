rows = int(input())

board = [[x for x in input()] for _ in range(rows)]

moves = [(2, 1), (1, 2), (1, -2), (-2, 1), (2, -1), (-1, 2), (-1, -2), (-2, -1)]

knight_to_remove = []

removed_knights = 0

while True:
    total_attacks = 0
    max_attacks = 0
    for row in range(rows):
        for col in range(rows):
            current_el = board[row][col]
            if current_el == 'K':
                current_attacks = 0
                for move in moves:
                    new_row = row + move[0]
                    new_col = col + move[1]
                    if (0 <= new_row <= rows - 1) and (0 <= new_col <= rows - 1):

                        new_pos = board[new_row][new_col]

                        if new_pos == 'K':
                            current_attacks += 1
                            total_attacks += 1
                if current_attacks > max_attacks:
                    max_attacks = current_attacks
                    knight_to_remove.clear()
                    knight_to_remove.append(row)
                    knight_to_remove.append(col)

    if knight_to_remove:
        board[knight_to_remove[0]][knight_to_remove[1]] = '0'
        removed_knights += 1
        knight_to_remove.clear()

    if total_attacks == 0:
        break

print(removed_knights)



