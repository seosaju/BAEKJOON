import sys

deque = []


def push_front(n):
    deque.insert(0, n)


def push_back(n):
    deque.append(n)


def pop_front():
    try:
        print(deque.pop(0))
    except IndexError:
        print(-1)


def pop_back():
    try:
        print(deque.pop())
    except IndexError:
        print(-1)


def size():
    print(len(deque))


def empty():
    if deque:
        print(0)
    else:
        print(1)


def front():
    try:
        print(deque[0])
    except IndexError:
        print(-1)


def back():
    try:
        print(deque[-1])
    except IndexError:
        print(-1)


for _ in range(int(sys.stdin.readline())):
    x = sys.stdin.readline().split()
    try:
        x[1]
    except IndexError:
        exec(x[0] + '()')
    else:
        exec(x[0]+'(' + x[1] + ')')
