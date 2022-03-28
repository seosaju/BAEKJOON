nums = list(map(int, input().split()))
m = [1, 1, 2, 2, 2, 8]

for i, num in enumerate(nums):
    print(m[i] - num, end=' ')
