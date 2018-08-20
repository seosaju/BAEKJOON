a_money = {0: 0, 1: 5000000, 2: 3000000, 3: 2000000, 4: 500000, 5: 300000, 6: 100000}
b_money = {0: 0, 1: 5120000, 2: 2560000, 3: 1280000, 4: 640000, 5: 320000}

for _ in range(int(input())):
    a, b = map(int, input().split())
    k = 0
    m = 0
    while a > 0:
        a -= (k + 1)
        k += 1
        if k > 6:
            k = 0
            break
    while b >= 1:
        b = b // 2
        m += 1
        if m > 5:
            m = 0
            break
    print(a_money[k] + b_money[m])
