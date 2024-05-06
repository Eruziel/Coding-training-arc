def neg_pos(num: list):
    positives = []
    negatives = []
    for n in num:
        if n > 0:
            positives.append(n)
        else:
            negatives.append(n)

    print(sum(negatives))
    print(sum(positives))
    if abs(sum(negatives)) > sum(positives):
        print('The negatives are stronger than the positives')
    else:
        print('The positives are stronger than the negatives')


nums = [int(x) for x in input().split()]

neg_pos(nums)
