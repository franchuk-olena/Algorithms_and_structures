from collections import deque


def fire_spread(n, m, edges, k, fire_sources):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque()
    time_to_burn = [-1] * (n + 1)

    for source in fire_sources:
        queue.append(source)
        time_to_burn[source] = 0

    while queue:
        current = queue.popleft()
        current_time = time_to_burn[current]

        for neighbor in graph[current]:
            if time_to_burn[neighbor] == -1:
                time_to_burn[neighbor] = current_time + 1
                queue.append(neighbor)

    max_time = -1
    last_vertex = -1
    for i in range(1, n + 1):
        if time_to_burn[i] > max_time:
            max_time = time_to_burn[i]
            last_vertex = i
        elif time_to_burn[i] == max_time and i < last_vertex:
            last_vertex = i

    return max_time, last_vertex


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
k = int(input())
fire_sources = list(map(int, input().split()))
time, vertex = fire_spread(n, m, edges, k, fire_sources)
print(time)
print(vertex)
