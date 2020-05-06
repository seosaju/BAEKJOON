n, p = int(input()), list(map(int, input().split()))
dp = [p[0]]

for i in range(1, n):
    dp.append(max(dp[i - 1] + p[i], p[i]))
print(max(dp))
