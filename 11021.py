import sys

for i in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    print('Case #{0}:'.format(i + 1), x + y)
