n = int(input())
dp = [[], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

for i in range(1, n + 1):
    tmp = []
    for digit in range(10):
        if digit == 0:
            tmp.append(dp[i][digit + 1])
        elif 0 < digit < 9:
            tmp.append(dp[i][digit - 1] + dp[i][digit + 1])
        if digit == 9:
            tmp.append(dp[i][digit - 1])
    dp.append(tmp)
print(sum(dp[n]) % 1000000000)
