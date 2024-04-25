from collections import deque

stations = deque([int(x) for x in input().split()] for _ in range(int(input())))

stations_copy = stations.copy()

current_petrol = 0
current_index = 0

while stations_copy:
    petrol, distance = stations_copy.popleft()

    current_petrol += petrol
    if current_petrol >= distance:
        current_petrol -= distance

    else:
        stations.rotate(-1)
        current_petrol = 0
        stations_copy = stations.copy()
        current_index += 1

print(current_index)