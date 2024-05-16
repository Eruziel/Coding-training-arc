from collections import deque

contestants = deque(int(x) for x in input().split())
pies = [int(x) for x in input().split()]


while contestants and pies:
    current_contestant = contestants.popleft()
    current_pie = pies.pop()

    if current_contestant >= current_pie:
        current_contestant -= current_pie

        if current_contestant > 0:
            contestants.append(current_contestant)
    elif current_pie > current_contestant:
        current_pie -= current_contestant

        if pies and current_pie == 1:
            pies[-1] += current_pie
        else:
            pies.append(current_pie)


if not pies and not contestants:
    print('We have a champion!')

elif contestants:
    print('We will have to wait for more pies to be baked!')
    print(f'Contestants left: {", ".join(str(x) for x in contestants)}')

elif pies:
    print('Our contestants need to rest!')
    print(f'Pies left: {", ".join(str(x) for x in pies)}')
