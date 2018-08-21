from sys import stdin
val = []
dp = []

n = int(input())
for _ in range(n):
    val.append(list(map(int, stdin.readline().split())))

dp.append(val[-1])
for i in range(1, n):
    temp = []
    for j in range(n - i):
        temp.append(val[n - i - 1][j] + max(dp[i - 1][j:j + 2]))
    dp.append(temp)
print(dp[-1][0])
