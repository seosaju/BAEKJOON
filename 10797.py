n = int(input())
nums = list(map(int, input().split()))

result = 0
for num in nums:
    if num == n:
        result += 1

print(result)
