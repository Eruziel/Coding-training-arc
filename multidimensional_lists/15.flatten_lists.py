nums = input().split('|')

matrix = [el for el in nums]


for i in matrix[::-1]:
    nums = [int(x) for x in i.split()]
    if nums:
        print(*nums, end=' ')
