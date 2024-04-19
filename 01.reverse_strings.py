some_list = input().split()

reversed_list = []

for el in some_list[::-1]:
    reversed_list.append(el[::-1])

print(*reversed_list)


