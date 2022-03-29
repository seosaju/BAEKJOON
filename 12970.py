n, k = map(int, input().split())

if k == 0:
    print("B" * 1 + "A" * (n - 1))
    exit()
if k == 1:
    print("B" * (n - 2) + "A" + "B")
    exit()
else:
    a = 0
    b = n - a
    while True:
        if k <= (a * b):
            break
        a += 1
        b -= 1
        if b < 0:
            print(-1)
            exit()

    ab_list = ['A' for _ in range(a - 1)]
    ab_list.extend(['B' for _ in range(n - (a - 1))])
    ab_list[-1] = 'A'
    index = n - 1
    while index >= 0:
        score = 0
        for i in range(n):
            if ab_list[i] == 'B':
                continue
            for j in range(i + 1, n):
                if ab_list[j] == 'B':
                    score += 1
        if score == k:
            print(''.join(ab_list))
            exit()
        else:
            ab_list[index] = 'B'
            ab_list[index - 1] = 'A'
            index -= 1
