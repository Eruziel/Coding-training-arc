from collections import deque

expression = input()
small_expression = deque()

for el in range(len(expression)):

    if expression[el] == "(":
        small_expression.append(el)
    elif expression[el] == ")":
        print(expression[small_expression.pop():el+1])



