from collections import deque

initial_fuel = [int(x) for x in input().split()]

additional_consumption = deque(int(x) for x in input().split())

needed_fuel_deq = deque(int(x) for x in input().split())

n = 0
altitudes = []
while True:
    fuel = initial_fuel.pop()
    consumption = additional_consumption.popleft()

    fuel_needed = needed_fuel_deq.popleft()

    if fuel - consumption >= fuel_needed:
        n += 1
        altitudes.append(n)
        print(f'John has reached: Altitude {n}')
        if n == 4:
            print('John has reached all the altitudes and managed to reach the top!')
            exit()

    else:
        print(f'John did not reach: Altitude {n+1}')
        print('John failed to reach the top.')
        break


if 0 < n < 4:
    print(f"Reached altitudes: {', '.join(str(f'Altitude {x}') for x in altitudes)}")
elif n == 0:
    print("John didn't reach any altitude.")
