n = int(input())

nums = list(map(int, input().split()))
b = []
results = []

for i in range(n):
    min_index = nums.index(min(nums))
    b.append(min_index)

    nums[min_index] = 1001

for i in range(n):
    result_index = b.index(min(b))
    results.append(result_index)

    b[result_index] = 51

for i in range(n):
    print(results[i], end=' ')