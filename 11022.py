import sys

for i in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    print('Case #{}: {} + {} ='.format(i + 1, x, y), x + y)
