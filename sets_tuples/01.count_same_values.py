nums = [float(x) for x in input().split()]
nums_set = {}
for n in nums:
    if n not in nums_set:
        nums_set[n] = 0

    nums_set[n] += 1

for key, value in nums_set.items():
    print(f"{key} - {value} times")

