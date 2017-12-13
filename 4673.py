num = []
for i in range(1, 10001):
    num.append(i + sum(int(j) for j in str(i)))
for i in sorted(set(range(1, 10001)) - set(num)):
    print(i)
