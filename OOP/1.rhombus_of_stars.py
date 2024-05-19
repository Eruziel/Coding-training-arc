n = int(input())


def upper_part(num):
    result = ''
    for i in range(1, num + 1):
        result += " " * (n - i) + "* " * i + "\n"

    m = 0
    for i in range(n, -1, -1):
        result += " " * (n - i + 1) + "* " * (n - m - 1) + "\n"
        m += 1

    return result


print(upper_part(n))
