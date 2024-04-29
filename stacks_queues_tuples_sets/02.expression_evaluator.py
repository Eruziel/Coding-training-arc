from collections import deque

expression = deque(input().split())

calculator = deque()

while expression:

    symbol = expression.popleft()

    if symbol not in "-*/+":
        calculator.append(int(symbol))

    elif symbol in "-*/+":

        while len(calculator) > 1:
            result = calculator.popleft()
            if symbol == '+':
                result += calculator.popleft()
                calculator.append(result)
            elif symbol == '-':
                result += -(calculator.popleft())
                calculator.appendleft(result)
            elif symbol == '/':
                result //= calculator.popleft()
                calculator.appendleft(result)
            elif symbol == '*':
                result *= calculator.popleft()
                calculator.append(result)


print(*calculator)

