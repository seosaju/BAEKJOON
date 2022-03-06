nums = list(map(int, input().split()))
sets = set()

for num in nums:
    sets.add(num)

count = 0
big_num = 0
for s in sets:
    if count < nums.count(s):
        count = nums.count(s)
        big_num = s

if count == 3:
    print(10000 + big_num * 1000)
elif count == 2:
    print(1000 + big_num * 100)
else:
    print(max(sets) * 100)
