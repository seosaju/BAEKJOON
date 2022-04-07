from collections import deque

results = deque([1, 1, 2, 4, 7])
for i in range(5, 1000001):
    results.append(results[-1] % 1000000009 + results[-2] % 1000000009 + results[-3] % 1000000009)

n = int(input())
for _ in range(n):
    i = int(input())
    print(results[i] % 1000000009)
