def math_operations(*args, **kwargs):
    index = 0
    result = ''
    for nums in args:

        for key, value in kwargs.items():
            if index == 0:
                kwargs['a'] += nums

            elif index == 1:
                kwargs['s'] -= nums

            elif index == 2:
                if nums != 0:
                    kwargs['d'] /= nums

            elif index == 3:
                kwargs['m'] *= nums

            if index == 3:
                index = 0
            else:
                index += 1
            break

    for key, value in sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0])):
        result += f"{key}: {value:.1f}\n"

    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))

print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))

print(math_operations(6.0, a=0, s=0, d=5, m=0))

