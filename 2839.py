num = int(input())
bag = 0

while True:
    if num % 5 == 0:
        print(num // 5 + bag)
        break

    elif num <= 0:
        print(-1)
        break

    num -= 3
    bag += 1
