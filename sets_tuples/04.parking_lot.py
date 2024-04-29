n = int(input())
cars = {}
for _ in range(n):

    direction, number = input().split(', ')

    if direction == 'IN':
        if number not in cars:
            cars[number] = 0
            cars[number] += 1
    elif direction == 'OUT':
        if number in cars:
            cars.pop(number)

if cars:
    print('\n'.join(x for x in cars.keys()))
else:
    print('Parking Lot is Empty')