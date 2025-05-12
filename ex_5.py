from collections import deque

queue = deque(input().split())
n = int(input())

while len(queue) != 1:
    queue.rotate(-(n-1))
    remove_kid = queue.popleft()
    print(f"Removed {remove_kid}")

print(f"Last is {queue[0]}")