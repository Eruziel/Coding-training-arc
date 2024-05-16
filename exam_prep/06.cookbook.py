def cookbook(*args: tuple):
    recipe_data = {}
    result = ''
    for recipe, cuisine, ingredients in args:
        if cuisine not in recipe_data:
            recipe_data[cuisine] = []

        recipe_data[cuisine].append((recipe, ingredients))

    sorted_cookbook = sorted(recipe_data.items(), key=lambda x: (-len(x[1]), x[0]))

    for key, value in sorted_cookbook:
        sorted_value = sorted(value, key=lambda x: x[0])
        result += f"{key} cuisine contains {len(sorted_value)} recipes:\n"
        for recipe, ingredients in sorted_value:
            result += f"  * {recipe} -> Ingredients: {', '.join(x for x in ingredients)}\n"

    return result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
