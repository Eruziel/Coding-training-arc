n = int(input())

chems = set()

for _ in range(n):
    data = input().split()
    for el in data:
        chems.add(el)

print(*chems, sep='\n')