n, m = [int(x) for x in input().split()]

first_set = set()
second_set = set()

for f in range(n):
    num = int(input())
    first_set.add(num)

for z in range(m):
    num = int(input())
    second_set.add(num)

print(*first_set.intersection(second_set), sep='\n')
