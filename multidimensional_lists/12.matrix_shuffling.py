rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()]for _ in range(rows)]

while True:
    is_valid = True
    command = input()
    if command == 'END':
        break
    action, *data = command.split()
    if action == 'swap' and len(data) == 4:
        for nums in data:
            if int(nums) > len(matrix) or int(nums) < 0:
                print('Invalid input!')
                is_valid = False
                break
        if is_valid:
            matrix[int(data[0])][int(data[1])], matrix[int(data[2])][int(data[3])] = matrix[int(data[2])][int(data[3])], matrix[int(data[0])][int(data[1])]
            for rows in matrix:
                print(f'{" ".join(str(x) for x in rows)}')
    else:
        print('Invalid input!')
        continue
