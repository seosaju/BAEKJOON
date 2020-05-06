import sys

n = int(input())
stair = list(int(sys.stdin.readline()) for _ in range(n))

if n < 3:
    if n == 0: print(0)
    if n == 1: print(stair[0])
    if n == 2: print(stair[0] + stair[1])
else:
    dp = [stair[0], stair[0] + stair[1], max(stair[0] + stair[2], stair[1] + stair[2])]
    for i in range(3, n):
        dp.append(max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i]))
    print(dp[-1])
