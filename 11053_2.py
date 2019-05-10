import bisect
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [arr[0]]

for i in range(1, n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        index = bisect.bisect_left(dp, arr[i], lo=0, hi=len(dp))
        dp[index] = arr[i]

print(len(dp))
