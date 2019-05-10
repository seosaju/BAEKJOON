import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1]
high = 1

for i in range(1, n):
    dp.append(1)
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
    high = max(high, dp[i])
print(high)
