n = int(input())

li = []
for _ in range(n):
    xy = list(map(int, input().split()))
    li.append([xy[1], xy[0]])

li.sort()

for i in li:
    print(i[1], i[0])
