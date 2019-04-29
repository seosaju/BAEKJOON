import sys

while True:
    x, y = map(int, sys.stdin.readline().split())
    if x or y:
        print(x + y)
    else:
        break
