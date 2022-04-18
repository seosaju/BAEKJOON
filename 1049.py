import math

n, m = map(int, input().split())

ij_list = []
for _ in range(m):
    ij_list.append((map(int, input().split())))

min_i = 1001
min_j = 1001
for i, j in ij_list:
    if i <= min_i:
        min_i = i
    if j <= min_j:
        min_j = j

print(min(min(min_i * (n // 6) + min_j * (n % 6), min_i * math.ceil(n / 6)), min_j * n))
