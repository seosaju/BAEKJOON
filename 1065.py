n = int(input())
han = 0
for i in range(1, n + 1):
    if i < 100:
        han += 1
    else:
        a = i // 100
        b = i % 100 // 10
        c = i % 10
        if (a - b) == (b - c):
            han += 1
        else:
            pass
print(han)