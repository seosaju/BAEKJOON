import sys
input = sys.stdin.readline

n = int(input())

magic_list = [[2, 4, 8, 6],
              [3, 9, 7, 1],
              [4, 6],
              [5],
              [6],
              [7, 9, 3, 1],
              [8, 4, 2, 6],
              [9, 1]]

for _ in range(n):
    i, j = map(int, input().split())
    j = j % 4 + 4
    num = 1
    for _ in range(j):
        num *= i
        num = int(str(num)[-1])
    result = num
    if result == 0:
        print(10)
    else:
        print(result)
