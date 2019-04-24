import sys

n = int(sys.stdin.readline())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = abs(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
    sqrt_sum = r1 + r2
    sqrt_sub = abs(r1 - r2)
    if distance == 0 and r1 == r2:
        print(-1)
        continue
    if sqrt_sum < distance or distance < sqrt_sub:
        print(0)
        continue
    if distance == sqrt_sum or distance == sqrt_sub:
        print(1)
        continue
    else:
        print(2)

