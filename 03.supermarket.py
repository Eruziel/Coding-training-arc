from collections import deque
supermarket = deque()
while True:

    command = input()
    if command == 'End':
        print(f'{len(supermarket)} people remaining.')
        break
    elif command == 'Paid':
        while len(supermarket) > 0:
            print(supermarket.popleft())
        continue
    supermarket.append(command)