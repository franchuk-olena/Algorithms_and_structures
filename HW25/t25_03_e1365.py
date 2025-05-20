def shortest_path(n, s, f, matrix):
    INF = 10**9
    dist = [INF] * n
    used = [False] * n
    dist[s] = 0

    for _ in range(n):
        v = -1
        for u in range(n):
            if not used[u] and (v == -1 or dist[u] < dist[v]):
                v = u
        if dist[v] == INF:
            break
        used[v] = True
        for u in range(n):
            if matrix[v][u] != -1 and dist[u] > dist[v] + matrix[v][u]:
                dist[u] = dist[v] + matrix[v][u]

    return dist[f] if dist[f] != INF else -1

n, s, f = map(int, input().split())
s -= 1
f -= 1

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print(shortest_path(n, s, f, matrix))
