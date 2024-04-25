clothes = [int(x) for x in input().split()]

rack_space = int(input())
racks = 0
space_remaining = rack_space
while clothes:
    current_clothing = clothes[-1]
    if space_remaining - current_clothing == 0:
        racks += 1
        space_remaining = rack_space
        clothes.pop()
    elif space_remaining - current_clothing < 0:
        racks += 1
        space_remaining = rack_space
    elif len(clothes) == 1:
        racks += 1
        clothes.pop()
    else:
        space_remaining -= current_clothing
        clothes.pop()

print(racks)