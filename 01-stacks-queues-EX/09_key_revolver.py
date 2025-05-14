from collections import deque

bullet_price = int(input())
size_of_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
prize = int(input())
shots = 0

while locks and bullets:
    shots += 1
    curr_bullet = bullets.pop()
    prize -= bullet_price

    if locks[0] >= curr_bullet:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    if shots == size_of_barrel and bullets:
        shots = 0
        print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${prize}")
