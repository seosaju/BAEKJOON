def prime(n):
    if n < 2:
        return 0
    root = int(n ** 0.5) + 1
    for j in range(2, root):
        if n % j == 0:
            return 0
    return 1


x, y = map(int, input().split())
for i in range(x, y + 1):
    if prime(i) == 1:
        print(i)
