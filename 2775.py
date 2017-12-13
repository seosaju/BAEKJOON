for _ in range(int(input())):
    x = int(input())
    y = int(input())
    n = [[0 for _ in range(y + 1)] for _ in range(x + 1)]
    for i in range(len(n[0])):
        n[0][i] = i
    for a in range(1, x + 1):
        for b in range(1, y + 1):
            n[a][b] = n[a - 1][b] + n[a][b - 1]
    print(n[x][y])
