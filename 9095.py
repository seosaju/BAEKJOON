for _ in range(int(input())):
    dp = [0, 1, 2, 4]
    n = int(input())
    for i in range(3, n + 1):
        dp.append(dp[i - 2] + dp[i - 1] + dp[i])
    print(dp[n])
