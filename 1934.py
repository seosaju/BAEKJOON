from math import lcm

n = int(input())
for _ in range(n):
    i, j = map(int, input().split())
    print(lcm(i, j))
