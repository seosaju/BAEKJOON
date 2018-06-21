import math


def prime(n):
    if n < 2:
        return 0
    for j in range(2, int(math.sqrt(n)) + 1):
        if not n % j:
            return 0
    return 1


for _ in range(int(input())):
    k = int(input()) // 2
    if prime(k):
        print(k, k)
        continue
    for i in range(1, k):
        if prime(k - i) and prime(k + i):
            print(k - i, k + i)
            break
