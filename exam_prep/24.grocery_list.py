def shop_from_grocery_list(budget, grocery_list, *args):
    bought = []
    for name, price in args:
        if name in grocery_list:
            if name not in bought:
                if budget - price >= 0:
                    budget -= price
                    bought.append(name)
                    grocery_list.remove(name)
                    if not grocery_list:
                        break
                else:
                    break

    if not grocery_list:
        return f'Shopping is successful. Remaining budget: {budget:.2f}.'
    else:
        return f"You did not buy all the products. Missing products: {', '.join(str(x) for x in grocery_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))

