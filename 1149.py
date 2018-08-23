import sys

value = []
dp = []

n = int(input())
for _ in range(n):
    value.append(list(map(int, sys.stdin.readline().split())))

dp.append(value[0])
for i in range(1, n):
    temp = []
    temp.append(min(dp[i - 1][1], dp[i - 1][2]) + value[i][0])
    temp.append(min(dp[i - 1][0], dp[i - 1][2]) + value[i][1])
    temp.append(min(dp[i - 1][0], dp[i - 1][1]) + value[i][2])
    dp.append(temp)

print(min(dp[-1]))
