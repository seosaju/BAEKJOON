n, k = map(int, input().split())
dp = [[j for j in range(k + 1)] for i in range(n + 1)]
for i in range(2, n + 1):
    for j in range(1, k + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
print(dp[n][k] % 1000000000)
