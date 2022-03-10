n, m = map(int, input().split())
nums = list(map(int, input().split()))

result = 0
index = 0
for i in nums:
    for j in nums[nums.index(i) + 1:]:
        for k in nums[nums.index(j) + 1:]:
            add = i + j + k
            if result <= add <= m:
                result = add
    index += 1
print(result)
