from collections import deque

monsters = deque(int(x) for x in input().split(','))

soldiers = [int(x) for x in input().split(',')]
total_monsters = len(monsters)
while monsters and soldiers:
    current_monster = monsters.popleft()
    current_soldier = soldiers.pop()

    if current_soldier >= current_monster:
        current_soldier -= current_monster
        if current_soldier > 0 and soldiers:
            soldiers[-1] += current_soldier
        elif current_soldier > 0 and not soldiers:
            soldiers.append(current_soldier)

    elif current_soldier < current_monster:
        current_monster -= current_soldier
        monsters.append(current_monster)

if not monsters:
    print('All monsters have been killed!')

if not soldiers:
    print('The soldier has been defeated.')


print(f'Total monsters killed: {total_monsters - len(monsters)}')

