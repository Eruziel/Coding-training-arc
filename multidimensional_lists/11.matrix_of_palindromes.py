row, col = [int(x) for x in input().split()]

start = 97

for i in range(row):
    for j in range(col):
        print(f'{chr(start)}{chr(start+j)}{chr(start)}', end=' ')
    start += 1
    print()

