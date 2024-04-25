from collections import deque

parentheses = deque(input())

parents = {
    ')': '(',
    ']': '[',
    '}': '{'
}
temp = ''
for el in parentheses:
    if el in parents.values():
        temp += el
        continue
    if el in parents.keys():  # el = ')'
        opening = parents[el]  # parents[el] = '('
        if not temp:
            print('NO')
            exit()
        if temp[-1] != opening:
            print('NO')
            exit()
        temp = temp[:-1]

print('YES')







