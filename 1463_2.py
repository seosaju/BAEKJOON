n = 0
s = {int(input())}
while 1 not in s:
    n += 1
    copy_s = s.copy()
    for i in copy_s:
        if i % 3 == 0:
            s.add(i // 3)
        if i % 2 == 0:
            s.add(i // 2)
        s.add(i - 1)
    s = s - copy_s
print(n)
