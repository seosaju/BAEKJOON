from math import gcd

i = int(input())
for _ in range(i):
    M, N, x, y = map(int, input().split())

    if M < N:
        M, N = N, M
        x, y = y, x
    lcm = M * N // gcd(M, N)

    while x != y and x <= lcm:
        if x < y:
            x += M
        else:
            y += N
    if x != y:
        print(-1)
    else:
        print(x)
