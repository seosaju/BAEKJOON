import sys

quadrant = [0, 0, 0, 0, 0]
for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    if x == 0 or y == 0:
        quadrant[4] += 1
    elif x > 0:
        if y > 0:
            quadrant[0] += 1
        else:
            quadrant[3] += 1
    else:
        if y > 0:
            quadrant[1] += 1
        else:
            quadrant[2] += 1

print('Q1:', quadrant[0])
print('Q2:', quadrant[1])
print('Q3:', quadrant[2])
print('Q4:', quadrant[3])
print('AXIS:', quadrant[4])
