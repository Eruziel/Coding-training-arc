from collections import deque

kids = deque(input().split())

toss_counter = int(input())

counter = 1
while True:
    if len(kids) == 1:
        print(f'Last is {kids.pop()}')
        break
    if toss_counter == counter:
        print(f'Removed {kids.popleft()}')
        counter = 1
    else:
        kids.append(kids.popleft())
        counter += 1

