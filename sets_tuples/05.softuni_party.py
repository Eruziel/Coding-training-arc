n = int(input())
guests = set()

for _ in range(n):
    guest = input()
    guests.add(guest)


while True:
    arrival = input()
    if arrival == 'END':
        break

    if arrival in guests:
        guests.discard(arrival)

print(len(guests))

print(*sorted(guests), sep='\n')