num = int(input())

stack = []

for _ in range(num):
    command = input()
    if command.startswith("2"):
        if stack:
            stack.pop()
    elif command.startswith("3"):
        if stack:
            print(max(stack))
    elif command.startswith("4"):
        if stack:
            print(min(stack))
    else:
        action = command.split()
        num_to_add = int(action[1])
        stack.append(num_to_add)

print(*reversed(stack), end='', sep=', ')
