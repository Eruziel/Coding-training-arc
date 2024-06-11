from collections import deque

supplies = [int(x) for x in input().split(', ')]
stamina = deque(int(x) for x in input().split(', '))
peaks = {'Vihren': 80, 'Kutelo': 90, 'Banski Suhodol': 100, 'Polezhan': 60, 'Kamenitza': 70}
climbed = []
current_peak = ''
while supplies and stamina:
    current_supply = supplies.pop()
    current_stamina = stamina.popleft()

    for i in peaks.keys():
        current_peak = i
        break

    if current_stamina + current_supply >= peaks[current_peak]:
        climbed.append(current_peak)
        peaks.pop(current_peak)
        if not peaks:
            print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK\nConquered peaks:')
            print('\n'.join(p for p in climbed))
            exit()

print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')
if climbed:
    print('Conquered peaks:')
    print('\n'.join(p for p in climbed))

