import math

n = int(input())
num = list(input().split())


def prime(i):
    if i < 2:
        return 0
    for j in range(2, int(math.sqrt(i) + 1)):
        if i % j == 0:
            return 0
    return 1


print(sum(prime(int(num[i])) for i in range(n)))
