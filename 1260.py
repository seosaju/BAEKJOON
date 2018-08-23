from sys import stdin
import copy
# 시간 초과


def dfs(v, first):
    graph = v
    x = first
    y = first
    answer = [x]
    while len(answer) != len(graph):
        if len(graph[x]) > 0:
            x = min(graph[x])
            graph[x].remove(y)
            graph[y].remove(x)
            if x in answer:
                x = y
            else:
                answer.append(x)
                y = x
        else:
            x = answer[-2]
            y = answer[-2]
    print(" ".join(str(i) for i in answer))


def bfs(v, first):
    graph = v
    x = first
    answer = [x]
    while len(answer) != len(graph):
        if len(graph[x]) > 0:
            k = min(graph[x])
            while len(graph[x]) != 0:
                y = graph[x].pop()
                graph[y].remove(x)
                if y not in answer:
                    answer.append(y)
                else:
                    pass
            x = k
        else:
            x = answer[-2]
    print(" ".join(str(i) for i in answer))


if __name__ == "__main__":
    n, edge, start = map(int, input().split())
    vertex = dict()
    for i in range(1, n + 1):
        vertex[i] = set()

    for _ in range(edge):
        x, y = map(int, stdin.readline().split())
        vertex[x].add(y)
        vertex[y].add(x)
    dfs(copy.deepcopy(vertex), start)
    bfs(copy.deepcopy(vertex), start)
