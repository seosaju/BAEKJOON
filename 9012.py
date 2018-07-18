import sys


def f():
    ps = list(sys.stdin.readline().rstrip())
    n = 0
    while len(ps) != 0:
        if n < 0:
            return "NO"
        x = ps.pop()
        if x == ')':
            n += 1
        elif x == '(':
            n -= 1

    return "NO" if n else "YES"


for _ in range(int(input())):
    print(f())
