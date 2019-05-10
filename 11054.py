def lis(arr, dp):
    for i in range(1, n):
        dp.append(1)
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return dp


n = int(input())
a = list(map(int, input().split()))
rev_a = a[::-1]
lis_dp = lis(a, [1])
lds_dp = lis(rev_a, [1])[::-1]

high = 0
for k in range(n):
    high = max(high, lis_dp[k] + lds_dp[k])
print(high - 1)
