import sys
x = int(input())
n = [int(sys.stdin.readline()) for _ in range(x)]
n.sort()
for i in n:
    print(i)
