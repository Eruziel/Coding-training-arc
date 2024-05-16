from collections import deque

money = [int(x) for x in input().split()]
prices = deque(int(x) for x in input().split())
bought = 0
while money and prices:
    current_money = money.pop()
    current_price = prices.popleft()

    if current_money > current_price:
        bought += 1
        current_money -= current_price
        if money:
            money[-1] += current_money

    elif current_price == current_money:
        bought += 1

if bought >= 4:
    print(f"Gluttony of the day! Henry ate {bought} foods.")
elif 0 < bought < 4:
    if bought == 1:
        print('Henry ate: 1 food.')
    else:
        print(f'Henry ate: {bought} foods.')
elif bought == 0:
    print('Henry remained hungry. He will try next weekend again.')