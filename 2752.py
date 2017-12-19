import sys

MAX_NUM = 10000
x = int(input())
a = [int(sys.stdin.readline()) for _ in range(x)]
n = len(a)

count = [0] * (MAX_NUM + 1)
countSum = [0] * (MAX_NUM + 1)

for i in range(n):
    count[a[i]] += 1

countSum[0] = count[0]
for i in range(1, MAX_NUM + 1):
    countSum[i] = countSum[i - 1] + count[i]

B = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    B[countSum[a[i]]] = a[i]
    countSum[a[i]] -= 1

for i in range(1, n + 1):
    print(str(B[i]))
