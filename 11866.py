from collections import deque

n, m = map(int, input().split())
x = deque([i + 1 for i in range(n)])

print("<", end='')
for i in range(n):
    x.rotate(-m + 1)
    print(x.popleft(), end='')
    if i != n - 1:
        print(', ', end='')
print(">")
