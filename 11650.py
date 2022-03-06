n = int(input())

coordinates = []
for i in range(n):
    coordinates.append(list(map(int, input().split())))
coordinates.sort()

for i in range(n):
    print(coordinates[i][0], coordinates[i][1])
