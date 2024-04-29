n = int(input())

odd_set = set()
even_set = set()

for i in range(1, n+1):
    name = input()
    result = 0
    for letter in name:
        result += ord(letter)

    final_result = result // i
    if final_result % 2 == 0:
        even_set.add(final_result)
    else:
        odd_set.add(final_result)

if sum(even_set) == sum(odd_set):
    print(f"{', '.join(str(x) for x in even_set.union(odd_set))}")
elif sum(odd_set) > sum(even_set):
    print(f"{', '.join(str(x) for x in odd_set.difference(even_set))}")
elif sum(even_set) > sum(odd_set):
    print(f"{', '.join(str(x) for x in even_set.symmetric_difference(odd_set))}")
