import sys

for _ in range(int(sys.stdin.readline())):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = abs(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
    sum_r = r1 + r2
    sub_r = abs(r1 - r2)
    if distance == 0 and r1 == r2:
        print(-1)
    elif sum_r < distance or distance < sub_r:
        print(0)
    elif distance == sum_r or distance == sub_r:
        print(1)
    else:
        print(2)
