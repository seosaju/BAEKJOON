import sys

s = []
for _ in range(int(input())):
    x = sys.stdin.readline()
    c = x[:2]
    if c == 'pu':
        s.append(x.split()[1])
    elif c == 'po':
        print(s.pop() if len(s) > 0 else -1)
    elif c == "si":
        print(len(s))
    elif c == "em":
        print((len(s) == 0) * 1)
    elif c == "to":
        print(s[-1] if len(s) > 0 else -1)
