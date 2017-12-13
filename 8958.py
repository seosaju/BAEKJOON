n = int(input())
x = []
exec(n * "x.append(input());")
for i in range(len(x)):
    p = 0
    result = 0
    for j in range(len(x[i])):
        if x[i][j] == 'O':
            p += 1
            result += p
        else:
            p = 0
    print(result)
