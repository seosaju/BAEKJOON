import sys

s = []
answer = []
result = []


def stack():
    for _ in range(int(input())):
        answer.append(int(sys.stdin.readline()))

    n = 1
    m = 0
    while m != len(answer):
        if len(s) == 0 or s[-1] < answer[m]:
                s.append(n)
                result.append('+')
                n += 1
        else:
            if s[-1] != answer[m]:
                return ['NO']
            else:
                s.pop()
                result.append('-')
                m += 1

    return result


for i in stack():
    print(i)
