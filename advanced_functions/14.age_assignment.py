def age_assignment(*args, **kwargs):
    result = ''
    new_dict = {}
    for name in args:
        for key, value in kwargs.items():
            if name.startswith(key):
                new_dict[name] = value

    for n, a in sorted(new_dict.items(), key=lambda kvp: kvp[0]):
        result += f"{n} is {a} years old.\n"

    return result


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))