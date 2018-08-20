import sys

q = []
for _ in range(int(input())):
    x = sys.stdin.readline()
    c = x[:2]

    if c == "pu":
        q.append(x.split()[1])
    elif c == "po":
        print(-1) if not q else print(q.pop(0))
    elif c == "si":
        print(len(q))
    elif c == "em":
        print(0) if q else print(1)
    elif c == "fr":
        print(q[0]) if q else print(-1)
    elif c == "ba":
        print(q[-1]) if q else print(-1)
