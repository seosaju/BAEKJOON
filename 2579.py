import sys

n = int(input())
stair = []
dp = []

for _ in range(n):
    stair.append(int(sys.stdin.readline()))

dp.append(stair[0])
dp.append(stair[1] + dp[0])
dp.append(max(stair[2] + stair[0], stair[2] + stair[1]))

for i in range(3, n):
    dp.append(max(stair[i] + dp[i - 2], stair[i] + stair[i - 1] + dp[i - 3]))

print(dp[-1])
