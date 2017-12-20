import sys
from collections import Counter


def median(x):
    x = sorted(x)
    return x[len(x) // 2]


def mode(x):
    x = sorted(x)
    counts = Counter(x)
    order = counts.most_common()
    modes = []
    for num in order:
        if num[1] == order[0][1]:
            modes.append(num[0])
    if len(modes) == 1:
        return modes[0]
    else:
        return modes[1]


n = int(sys.stdin.readline())
x = [int(sys.stdin.readline()) for _ in range(n)]
print(round(sum(x) / len(x)))
print(median(x))
print(mode(x))
print(max(x) - min(x))
