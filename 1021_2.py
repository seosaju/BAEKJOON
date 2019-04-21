import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
queue = [x + 1 for x in range(n)]
result = 0

while num:
    queue_len = len(queue)
    index = queue.index(num[0])
    if index > queue_len // 2:
        queue = queue[index:] + queue[:index]
        length = queue_len - index
        result += length
    else:
        queue = queue[index:] + queue[:index]
        result += index
    queue.pop(0)
    num.pop(0)
print(result)
