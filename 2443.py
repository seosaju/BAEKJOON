n = int(input())

j = 0
for i in range(n, 0, -1):
    print(" " * j + "*" * (2 * i - 1))
    j += 1
