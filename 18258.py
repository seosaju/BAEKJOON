from collections import deque
import sys

input = sys.stdin.readline
queue = deque()
n = int(input())
for _ in range(n):
    operate = list(input().split())
    if len(operate) == 2:
        queue.append(int(operate[1]))
    else:
        if operate[0] == "pop":
            print(queue.popleft() if len(queue) else -1)
        elif operate[0] == "size":
            print(len(queue))
        elif operate[0] == "empty":
            print(int(len(queue) == 0))
        elif operate[0] == "front":
            print(queue[0] if len(queue) else -1)
        elif operate[0] == "back":
            print(queue[-1] if len(queue) else -1)
