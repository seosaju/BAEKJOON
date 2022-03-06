i = 1
result = 0
index = 1
for _ in range(9):
    n = int(input())
    if n > result:
        result = n
        index = i
    i += 1
print(result)
print(index)
