import sys

m = 10000
p = [0] * (m + 1)
n = int(sys.stdin.readline())

for i in range(n):
    p[int(sys.stdin.readline())] += 1

for i in range(m + 1):
    print('%s\n' % i * p[i], end='')
