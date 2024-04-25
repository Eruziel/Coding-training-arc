from collections import deque
from datetime import timedelta, datetime

robots = deque(input().split(';'))
start = input().split(':')
products = deque()
timer = datetime(2024, 4, 22, int(start[0]), int(start[1]), int(start[2]))
delta = timedelta(seconds=1)
readiness_timer = deque()

for r in robots:
    rob = r.split('-')
    readiness = int(rob[1])
    readiness_timer.append(readiness)


while True:
    command = input()
    if command == 'End':
        break
    products.append(command)


while products:
    timer += delta
    current_product = products.popleft()

    for i, current_robot in enumerate(robots):

        current_robot = current_robot.split('-')
        robot_name = current_robot[0]
        robot_time_needed = int(current_robot[1])
        robot_time_left = readiness_timer[i]

        if readiness_timer[i] < robot_time_needed:
            readiness_timer[i] += 1

        if readiness_timer[i] == robot_time_needed:
            print(f"{robot_name} - {current_product} [{timer.strftime('%H:%M:%S')}]")
            readiness_timer[i] = 0
            break

    else:
        products.append(current_product)



