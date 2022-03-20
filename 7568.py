import sys
input = sys.stdin.readline

n = int(input())

weights = []
heights = []
for _ in range(n):
    x, y = map(int, input().split())
    weights.append(x)
    heights.append(y)

for i in range(len(weights)):
    result = 1
    for j in range(len(weights)):
        if weights[i] < weights[j] and heights[i] < heights[j]:
            result += 1
    print(result, end=' ')
