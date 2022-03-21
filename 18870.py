import sys
input = sys.stdin.readline

n = int(input())
points = list(map(int, input().split()))
sorted_points = sorted(set(points))
point_dict = {sorted_points[i]: i for i in range(len(sorted_points))}

for i in points:
    print(point_dict[i], end=' ')
