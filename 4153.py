while True:
    x, y, z = map(int, input().split())
    result = sorted([x, y, z])
    x, y, z = result[0], result[1], result[2]
    if x == 0 and y == 0 and z == 0:
        break
    if (x ** 2) + (y ** 2) == (z ** 2):
        print("right")
    else:
        print("wrong")
