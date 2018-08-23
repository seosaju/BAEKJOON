import copy
from sys import stdin


def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            temp = []
            temp.extend(graph[vertex] - set(visited))
            temp.sort(reverse=True)
            stack.extend(temp)
    return " ".join(str(i) for i in visited)


def bfs(graph, start):
    visited, queue = [], [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            temp = []
            temp.extend(graph[vertex] - set(visited))
            temp.sort()
            queue.extend(temp)
    return " ".join(str(i) for i in visited)


if __name__ == "__main__":
    N, M, V = map(int, input().split())
    graph = {}
    for i in range(N):
        graph[i + 1] = set()
    for _ in range(M):
        x, y = map(int, stdin.readline().split())
        graph[x].add(y)
        graph[y].add(x)

    print(dfs(copy.deepcopy(graph), V))
    print(bfs(copy.deepcopy(graph), V))
