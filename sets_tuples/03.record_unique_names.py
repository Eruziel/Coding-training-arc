n = int(input())
names = []
for _ in range(n):
    name = input()
    names.append(name)

for n in set(names):
    print(n)