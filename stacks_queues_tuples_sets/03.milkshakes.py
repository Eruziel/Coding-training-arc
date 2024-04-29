from collections import deque

chocolates = deque(int(x) for x in input().split(', '))
milk_cups = deque(int(x) for x in input().split(', '))

milkshakes = 0

while milkshakes != 5 and chocolates and milk_cups:

    current_choco = chocolates.pop()
    current_cup = milk_cups.popleft()

    if current_choco <= 0 and current_cup <= 0:
        continue
    elif current_choco <= 0:
        milk_cups.appendleft(current_cup)
        continue
    elif current_cup <= 0:
        chocolates.append(current_choco)
        continue

    if current_choco == current_cup:
        milkshakes += 1

    else:
        chocolates.append(current_choco - 5)
        milk_cups.append(current_cup)

if milkshakes != 5:
    print('Not enough milkshakes.')
else:
    print('Great! You made all the chocolate milkshakes needed!')

if not chocolates:
    print('Chocolate: empty')
else:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")

if not milk_cups:
    print('Milk: empty')
else:
    print(f"Milk: {', '.join(str(x) for x in milk_cups)}")
