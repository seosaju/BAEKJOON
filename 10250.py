for _ in range(int(input())):
    H, W, N = map(int, input().split())
    print("{}{:02d}".format((N - 1) % H + 1, (N - 1) // H + 1))
