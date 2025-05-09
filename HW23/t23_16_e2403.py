def dfs(graph, vertex, visited, stack=None):
    visited[vertex] = True
    for v in graph[vertex]:
        if not visited[v]:
            dfs(graph, v, visited, stack)
    if stack is not None:
        stack.append(vertex)


def kosaraju(n, graph):
    visited = [False] * n
    stack = []

    for v in range(n):
        if not visited[v]:
            dfs(graph, v, visited, stack)

    transposed_graph = [[] for _ in range(n)]
    for u in range(n):
        for v in graph[u]:
            transposed_graph[v].append(u)

    visited = [False] * n
    scc_count = 0

    while stack:
        v = stack.pop()
        if not visited[v]:
            dfs(transposed_graph, v, visited)
            scc_count += 1

    return scc_count

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)

result = kosaraju(n, graph)

print(result)
