n = int(input())
x = [input() for _ in range(n)]
result = 0
for i in range(len(x)):
    tmp = []
    for j in range(len(x[i])):
        if x[i][j] not in tmp:
            tmp.append(x[i][j])
        else:
            if x[i][j - 1] != x[i][j]:
                break
        if j == len(x[i]) - 1:
            result += 1
        else:
            continue
print(result)
