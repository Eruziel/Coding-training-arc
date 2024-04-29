from collections import deque

doll = 0
train = 0
bear = 0
bycycle = 0
template = {'Doll': 150, 'Wooden  train': 250, 'Teddy bear': 300, 'Bicycle': 400}
presents = {'Doll': 0, 'Wooden  train': 0, 'Teddy bear': 0, 'Bicycle': 0}
materials = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())

while materials and magic:

    total_magic = magic[0] * materials[-1]

    if total_magic in template.values():
        if total_magic == 150:
            presents['Doll'] += 1
        elif total_magic == 250:
            presents['Wooden  train'] += 1
        elif total_magic == 300:
            presents['Teddy bear'] += 1
        elif total_magic == 400:
            presents['Bicycle'] += 1
        magic.popleft()
        materials.pop()

    elif total_magic < 0:

        materials.append(materials.pop() + magic.popleft())

    elif magic[0] == 0 and materials[-1] == 0:
        magic.popleft()
        materials.pop()
    elif magic[0] == 0:
        magic.popleft()
    elif materials[-1] == 0:
        materials.pop()
    else:
        magic.popleft()
        materials[-1] += 15


if (presents['Doll'] >= 1 and presents['Wooden  train'] >= 1) or (presents['Teddy bear'] >= 1 and presents['Bicycle'] >=1):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')


if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")

if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for key, value in sorted(presents.items()):
    if value > 0:
        print(f'{key}: {value}')
