n = [int(x) for x in input()]

if len(n) == 1:
    n.append(0)
    n.sort()

queue = []
queue += n
cnt = 1

while True:
    new = str(int(queue[0]) + int(queue[1]))
    queue.append(int(new[len(new) - 1]))
    queue.pop(0)
    if queue == n:
        break
    cnt += 1

print(cnt)
