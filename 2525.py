h, m = map(int, input().split())
time = int(input())

h += (m + time) // 60
if h >= 24:
    h = h - 24

m = (m + time) % 60
print(f'{h} {m}')
