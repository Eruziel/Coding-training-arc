from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())
matches = 0
while holes and worms:

    current_worm = worms.pop()
    current_hole = holes.popleft()

    if current_worm != current_hole:
        current_worm -= 3
        if current_worm > 0:
            worms.append(current_worm)
    else:
        matches += 1

if matches:
    print(f"Matches: {matches}")
else:
    print('There are no matches.')

if not worms and matches == 4:
    print('Every worm found a suitable hole!')
elif not worms:
    print('Worms left: none')
elif worms:
    print(f'Worms left: {", ".join(str(x) for x in worms)}')

if not holes:
    print('Holes left: none')
else:
    print(f'Holes left: {", ".join(str(x) for x in holes)}')