n = int(input())
dp = [[], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

for i in range(2, n + 1):
    tmp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for digit in range(10):
        tmp[digit] += sum(dp[i - 1][digit:])
    dp.append(tmp)
print(sum(dp[n]) % 10007)
