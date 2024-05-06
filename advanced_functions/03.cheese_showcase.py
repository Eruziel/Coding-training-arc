def sorting_cheeses(**kwargs):
    result = ''
    sorted_result = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    for key, value in sorted_result:
        result += f"{key}\n"
        for nums in sorted(value, reverse=True):
            result += f"{nums}\n"

    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
