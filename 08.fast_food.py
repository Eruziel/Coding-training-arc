from collections import deque
available_food = int(input())


food_orders = deque(int(x) for x in input().split())

print(max(food_orders))

while food_orders:
    current_order = int(food_orders[0])
    if available_food - current_order >= 0:
        available_food -= current_order
        food_orders.popleft()

    else:
        print(f'Orders left: {" ".join(str(x) for x in food_orders)}')
        exit()

print('Orders complete')