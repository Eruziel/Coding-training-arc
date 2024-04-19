from collections import deque

starting_water = int(input())

people = deque()

while True:
    command = input()
    if command == "Start":
        break
    people.append(command)

while True:
    action = input()

    if action == 'End':
        print(f'{starting_water} liters left')
        break
    if action.isdigit():
        liters = int(action)
        if starting_water - liters >= 0:
            print(f"{people.popleft()} got water")
            starting_water -= liters
        else:
            print(f"{people.popleft()} must wait")
    else:
        act = action.split()
        refill = int(act[1])
        starting_water += refill

