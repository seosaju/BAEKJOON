dp = [[], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
for i in range(2, int(input()) + 1):
    tmp = []
    for j in range(10):
        tmp.append(sum(dp[i-1][j:]))
    dp.append(tmp)
print(sum(dp[-1]) % 10007)
