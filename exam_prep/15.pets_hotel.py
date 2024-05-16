def accommodate_new_pets(capacity, max_weight, *args):
    pets = {}
    result = ''
    current_capacity = capacity
    for pet, weight in args:
        if current_capacity == 0:
            result += 'You did not manage to accommodate all pets!\n'
            break

        if weight <= max_weight:
            if pet not in pets:
                pets[pet] = 0
            pets[pet] += 1
            current_capacity -= 1

    else:
        result += f"All pets are accommodated! Available capacity: {current_capacity}.\n"

    result += 'Accommodated pets:\n'

    for key, value in sorted(pets.items(), key=lambda kvp: kvp[0]):
        result += f"{key}: {value}\n"

    return result


print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))





