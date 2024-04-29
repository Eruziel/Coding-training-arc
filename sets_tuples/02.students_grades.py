names = int(input())
students = {}

for _ in range(names):
    name, grade = input().split()

    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for key, value in students.items():
    grades = ' '.join(str(f"{x:.2f}") for x in value)
    avg = sum(value) / len(value)
    print(f'{key} -> {grades} (avg: {avg:.2f})')

