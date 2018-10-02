for _ in range(int(input())):
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))
    check = 1
    while True:
        top_num = max(num_list)
        top = num_list[0]
        num_list.pop(0)
        if top == top_num:
            if m == 0:
                break
            else:
                check += 1
                m -= 1
        else:
            num_list.append(top)
            if m == 0:
                m = len(num_list) - 1
            else:
                m -= 1
    print(check)
