n = int(input())
for i in range(n):
    print(' ' * i + '*' * (n * 2 - 1 - (i * 2)))
for i in range(2, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

