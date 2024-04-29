n = int(input())

longest_intersec = set()
longest_length = 0

for _ in range(n):
    data = input().split('-')
    first_set = [int(x) for x in data[0].split(',')]
    second_set = [int(x) for x in data[1].split(',')]

    first = set(range(first_set[0], first_set[1]+1))
    second = set(range(second_set[0], second_set[1]+1))

    if len(first.intersection(second)) > longest_length:
        longest_length = len(first.intersection(second))
        longest_intersec = first.intersection(second)

print(f'Longest intersection is [{", ".join(str(x) for x in longest_intersec)}] with length {longest_length}')