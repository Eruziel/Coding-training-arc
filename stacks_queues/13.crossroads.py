from collections import deque

green_light = int(input())
free_window = int(input())
green_light_reset = green_light
free_window_reset = free_window
passed_cars = 0
cars = deque()

while True:
    command = input()
    if command == 'END':
        print('Everyone is safe.')
        print(f'{passed_cars} total cars passed the crossroads.')
        break
    elif command == 'green':
        passed_cars = 0
        green_light = green_light_reset
        free_window = free_window_reset
        for car in cars:
            if green_light < 0:
                passed_cars += 1
                break
            for el in range(1, len(car)+1):
                green_light -= 1
                if green_light < 0:
                    free_window -= 1
                    if free_window == 0:
                        print('A crash happened!')
                        print(f'{car} was hit at {car[el]}.')
                        exit()

                passed_car = car[:el]
            passed_cars += 1
        for p in range(passed_cars):
            cars.popleft()
    else:
        cars.append(command)
