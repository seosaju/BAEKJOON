import sys
input = sys.stdin.readline

n, value = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

result = 0
for coin in coins:
    if coin > value:
        continue

    result += value // coin
    value -= coin * (value // coin)

    if value == 0:
        break

print(result)
