from collections import deque
textiles = deque(int(x) for x in input().split())
medicament = [int(x) for x in input().split()]

items = {'Patch': 0, 'Bandage': 0, 'MedKit': 0}

while textiles and medicament:
    current_textile = textiles.popleft()
    current_medicament = medicament.pop()

    result = current_medicament + current_textile

    if result == 30:
        items['Patch'] += 1
    elif result == 40:
        items['Bandage'] += 1
    elif result == 100:
        items['MedKit'] += 1
    elif result > 100:
        items['MedKit'] += 1
        medicament[-1] += result - 100
    else:
        medicament.append(current_medicament + 10)


if not medicament and not textiles:
    print('Textiles and medicaments are both empty.')
elif not textiles:
    print('Textiles are empty.')
elif not medicament:
    print('Medicaments are empty.')


sorted_items = sorted(items.items(), key=lambda v: (-v[1], v[0]))

for key, value in sorted_items:
    if value > 0:
        print(f'{key} - {value}')

if medicament:
    print(f'Medicaments left: {", ".join(str(x) for x in reversed(medicament))}')

if textiles:
    print(f'Textiles left: {", ".join(str(x) for x in textiles)}')

