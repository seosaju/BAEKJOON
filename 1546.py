n = int(input())
x = list(map(int, input().split()))
print("{:.2f}".format(sum(x) / max(x) * 100 / len(x)))
