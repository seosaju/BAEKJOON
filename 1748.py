x = 0
n = int(input())
length = len(str(n))
for i in range(1, length + 1):
    if i < length:
        x += ((10 ** i) - (10 ** (i - 1))) * i
    else:
        tmp_n = n - (10 ** (i - 1))
        x += (tmp_n * i) + i
print(x)
