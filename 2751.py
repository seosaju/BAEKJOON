import sys

a = int(sys.stdin.readline())
b = [int(sys.stdin.readline()) for _ in range(a)]
b.sort()
for i in range(a):
    print(b[i])
