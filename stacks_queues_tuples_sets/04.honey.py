from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(x for x in input().split())

total_nectar = 0
while working_bees and nectar:

    bee = working_bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar >= bee:
        current_symbol = symbols.popleft()
        if current_symbol == '+':
            total_nectar += abs(bee + current_nectar)
        elif current_symbol == '-':
            total_nectar += abs(bee - current_nectar)
        elif current_symbol == '/':
            if current_nectar == 0:
                continue
            total_nectar += abs(bee / current_nectar)
        elif current_symbol == '*':
            total_nectar += abs(bee * current_nectar)
    elif current_nectar < bee:
        working_bees.appendleft(bee)

print(f"Total honey made: {total_nectar}")

if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")