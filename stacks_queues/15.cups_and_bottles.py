from collections import deque

cup_capacity = deque(int(x) for x in input().split())
bottle_capacity = deque(int(x) for x in input().split())
wasted_water = 0
while True:
    current_bottle = bottle_capacity[-1]
    current_cup = cup_capacity[0]

    if current_cup - current_bottle <= 0:
        wasted_water += current_bottle - current_cup
        cup_capacity.popleft()
        bottle_capacity.pop()
        if not cup_capacity:
            print(f"Bottles: {' '.join(str(x) for x in reversed(bottle_capacity))}")
            print(f"Wasted litters of water: {wasted_water}")
            break
        if not bottle_capacity:
            print(f"Cups: {' '.join(str(x) for x in cup_capacity)}")
            print(f"Wasted litters of water: {wasted_water}")
            break
    elif current_cup - current_bottle > 0:
        cup_capacity[0] -= bottle_capacity[-1]
        bottle_capacity.pop()
        if not bottle_capacity:
            print(f"Cups: {' '.join(str(x) for x in cup_capacity)}")
            print(f"Wasted litters of water: {wasted_water}")
            break
