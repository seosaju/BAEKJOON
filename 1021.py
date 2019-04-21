import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
queue = deque(x + 1 for x in range(n))
result = 0

while num:
    half = len(queue) // 2
    if queue[0] is num[0]:
        queue.popleft()
        num.pop(0)
        continue
    else:
        if half < queue.index(num[0]):
            queue.appendleft(queue.pop())
        else:
            queue.append(queue.popleft())
    result += 1
print(result)
