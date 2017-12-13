n = int(input())
x = y = 1
while True:
    x += y
    if n < x:
        break
    y += 1
a = x - n
b = (y + 1) - (x - n)
if y % 2 == 1:
    print("{}/{}".format(a, b))
else:
    print("{}/{}".format(b, a))
