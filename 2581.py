import sys
import math

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
p_min = []


def prime(i):
    if i < 2:
        return 0
    for j in range(2, int(math.sqrt(i) + 1)):
        if i % j == 0:
            return 0
    if len(p_min) == 0:
        p_min.append(i)
    return i


p_sum = sum(prime(i) for i in range(n, m + 1))
if len(p_min) != 0:
    print(p_sum)
    print(p_min[0])
else:
    print(-1)
