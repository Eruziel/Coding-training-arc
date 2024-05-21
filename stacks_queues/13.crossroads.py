from collections import deque

green_light = int(input())
free_window = int(input())
green_copy = green_light
free_copy = free_window
cars = deque()
passed = False
passed_cars = 0
while True:
    command = input()

    if command == 'END':
        print('Everyone is safe.')
        print(f"{passed_cars} total cars passed the crossroads.")
        break

    if command != 'green':
        cars.append(command)

    elif command == 'green':
        green_light = green_copy
        free_window = free_copy
        while cars:
            current_car = cars.popleft()
            if green_light > 0:
                passed_car = ''
                for symbol in range(len(current_car)):

                    if passed:
                        break

                    passed_car += current_car[symbol]
                    if passed_car == current_car:
                        passed_cars += 1
                    green_light -= 1

                    if green_light == 0 and passed_car != current_car:
                        start = symbol + 1

                        car_check = current_car[start:]
                        passed = False
                        for s in car_check:

                            if free_window == 0 and passed_car != current_car:
                                print('A crash happened!')
                                print(f"{current_car} was hit at {s}.")
                                exit()
                            passed_car += s
                            free_window -= 1
                            if passed_car == current_car:
                                passed_cars += 1
                                passed = True
            else:
                cars.appendleft(current_car)
                break






