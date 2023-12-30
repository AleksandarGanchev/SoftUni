from collections import deque


bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence_price = int(input())

bullets_shot = 0
bullets_total_cost = 0
while bullets:
    if bullets[-1] <= locks[0]:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    bullets.pop()
    bullets_shot += 1
    bullets_total_cost += bullet_price

    if bullets_shot == gun_barrel_size and len(bullets):
        print("Reloading!")
        bullets_shot = 0

    if len(locks) == 0:
        break

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    earned_money = intelligence_price - bullets_total_cost
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")
