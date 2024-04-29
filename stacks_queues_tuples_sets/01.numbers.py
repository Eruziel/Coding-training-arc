first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())
n = int(input())

for _ in range(n):
    action, action_type, *data = input().split()

    if action == 'Add':
        if action_type == 'First':
            for num in (int(x) for x in data):
                first_sequence.add(int(num))
        elif action_type == 'Second':
            for num in (int(x) for x in data):
                second_sequence.add(int(num))

    elif action == 'Remove':
        if action_type == 'First':
            for num in (int(x) for x in data):
                if num in first_sequence:
                    first_sequence.discard(num)
        elif action_type == 'Second':
            for num in (int(x) for x in data):
                if num in second_sequence:
                    second_sequence.discard(num)
    elif action == 'Check':
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print('True')
        else:
            print('False')

print(f'{", ".join(str(x) for x in sorted(first_sequence))}')
print(f'{", ".join(str(x) for x in sorted(second_sequence))}')