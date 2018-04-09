import sys

n = int(sys.stdin.readline())
sum_list = []
for _ in range(n):
    sum_list.append(sum(map(int, sys.stdin.readline().split())))

for i in range(n):
    print(sum_list[i])
