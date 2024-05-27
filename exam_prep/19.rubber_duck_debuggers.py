from collections import deque

programmer_time = deque(int(x) for x in input().split())
programmer_tasks = [int(x) for x in input().split()]

darth_vader_ducky = 0
thor_ducky = 0
big_blue_rubber_ducky = 0
small_yellow_rubber_ducky = 0

while programmer_tasks and programmer_time:
    current_time = programmer_time.popleft()
    current_task = programmer_tasks.pop()

    result = current_task * current_time

    if 0 <= result <= 60:
        darth_vader_ducky += 1
    elif 61 <= result <= 120:
        thor_ducky += 1
    elif 121 <= result <= 180:
        big_blue_rubber_ducky += 1
    elif 181 <= result <= 240:
        small_yellow_rubber_ducky += 1

    else:
        current_task -= 2
        programmer_tasks.append(current_task)
        programmer_time.append(current_time)


print('Congratulations, all tasks have been completed! Rubber ducks rewarded:')
print(f"Darth Vader Ducky: {darth_vader_ducky}")
print(f'Thor Ducky: {thor_ducky}')
print(f'Big Blue Rubber Ducky: {big_blue_rubber_ducky}')
print(f'Small Yellow Rubber Ducky: {small_yellow_rubber_ducky}')

