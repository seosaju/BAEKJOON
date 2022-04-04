n = int(input())

times = sorted(list(map(int, input().split())))

result = 0
for i in range(n):
    for j in range(i + 1):
        result += times[j]

print(result)
