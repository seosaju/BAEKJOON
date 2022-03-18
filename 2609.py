def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


x, y = map(int, input().split())
gcd = gcd(x, y)
print(gcd)
print(x * y // gcd)
