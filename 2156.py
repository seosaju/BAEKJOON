import sys

n = int(sys.stdin.readline())
x, dp = [], [0]
for _ in range(n):
    x.append(int(sys.stdin.readline()))
dp.append(x[0])
if n > 1:
    dp.append(x[0] + x[1])
for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 2] + x[i - 1], dp[i - 3] + x[i - 2] + x[i - 1]))
print(dp[n])
