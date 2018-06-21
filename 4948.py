MAX = 246913
num = [x for x in range(1, MAX)]
num.insert(0, 1)

for i in range(2, MAX):
    for j in range(i * 2, MAX, i):
        if num[j] == 1:
            continue
        num[j] = 1

while True:
    n = int(input())
    if n == 0:
        break
    else:
        cnt = 0
        for i in range(n, 2 * n):
            if num[i + 1] != 1:
                cnt += 1
        print(cnt)
