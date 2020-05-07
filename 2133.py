n = int(input())
dp = [1, 0, 3]

for i in range(3, n + 1):
    if i % 2 != 0:
        dp.append(0)
        continue
    else:
        dp.append(3 * dp[i - 2])
        for j in range(4, i + 1, 2):
            dp[i] += dp[i - j] * 2
print(dp[n])
