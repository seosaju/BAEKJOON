from collections import deque


def josephus(n, m):
    deq = deque([i + 1 for i in range(n)])
    print("<", end='')
    while len(deq) != 1:
        deq.rotate(-m + 1)
        num = deq.popleft()
        print(str(num) + ", ", end='')
    print(deq.popleft(), end='')
    print(">")


n, m = map(int, input().split())
josephus(n, m)
