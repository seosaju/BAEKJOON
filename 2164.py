from collections import deque

n = int(input())

q = deque(i for i in range(1, n + 1))
while len(q) > 1:
    q.popleft()
    if len(q) == 1:
        break
    q.append(q.popleft())

print(q.pop())