import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

deque = deque()
for _ in range(n):
    i = int(input())
    if i != 0:
        deque.append(i)
    else:
        deque.pop()

print(sum(deque))
