a, b, c = map(int, input().split())

if b == c or a / (c - b) < 0:
    print(-1)
else:
    print((a // (c - b)) + 1)
