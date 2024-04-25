from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = deque(int(x) for x in input().split())
locks = deque(int(x) for x in input().split())
intelligence = int(input())
barrel = deque()
cost = 0
while True:

    if barrel:
        current_bullet = barrel.popleft()
        cost += bullet_price
        if current_bullet > locks[0]:
            print('Ping!')
            continue
        else:
            current_lock = locks.popleft()
            print('Bang!')
            if len(barrel) == 0 and bullets:
                print('Reloading!')
            if not locks:
                print(f'{len(bullets)} bullets left. Earned ${intelligence-cost}')
                break

    else:
        if not bullets:
            print(f"Couldn't get through. Locks left: {len(locks)}")
            break
        for bullet in range(barrel_size):
            barrel.append(bullets.pop())




