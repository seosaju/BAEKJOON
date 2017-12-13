for _ in range(int(input())):
    key, value = input().split()
    for x in value:
        print(int(key) * x, end='')
    print()
