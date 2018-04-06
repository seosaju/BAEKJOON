n = int(input())
x = list(list(map(int, input().split())) for _ in range(n))

for i in range(n):
    avg = sum(x[i][1:]) / x[i][0]
    over_avg = [n for n in x[i][1:] if n > avg]
    print("{:.3f}".format(len(over_avg) / (len(x[i]) - 1) * 100) + "%")
