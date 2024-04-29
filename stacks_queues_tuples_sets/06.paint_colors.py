from collections import deque

colours = deque(input().split())

template = ['red', 'yellow', 'blue']
sec_template = ['orange', 'purple', 'green']

collected = []
secondary = []

while colours:

    first = colours.popleft()
    second = colours.pop() if colours else ''

    combo = first + second
    combo_2 = second + first

    if combo in template or combo in sec_template:
        collected.append(combo)
    elif combo_2 in template or combo_2 in sec_template:
        collected.append(combo_2)

    else:
        middle = len(colours) // 2
        if len(first) > 1:
            first = first[:-1]
            colours.insert(middle, first)
        if len(second) > 1:
            second = second[:-1]
            colours.insert(middle, second)


for color in collected:
    if color in sec_template:
        if color == 'orange':
            if 'red' not in collected or 'yellow' not in collected:
                collected.remove(color)
        elif color == 'purple':
            if 'red' not in collected or 'blue' not in collected:
                collected.remove(color)
        elif color == 'green':
            if 'yellow' not in collected or 'blue' not in collected:
                collected.remove(color)


print(collected)