from math import sqrt


def f(x):
    n = int(sqrt(x))
    n_pow = n ** 2
    if x == n_pow:
        return n * 2 - 1
    elif x <= n_pow + n:
        return n * 2
    else:
        return n * 2 + 1


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(f(b - a))
