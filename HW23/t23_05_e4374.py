def dfs(v, used, adj):
    used[v] = True
    for u in adj[v]:
        if not used[u]:
            dfs(u, used, adj)

n, m = map(int, input().split())
edges = []
adj = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b))
    adj[a].append(b)
    adj[b].append(a)

k = int(input())
for _ in range(k):
    parts = list(map(int, input().split()))
    c = parts[0]
    query = parts[1:]

    temp_adj = [list(neigh) for neigh in adj]

    for idx in query:
        idx -= 1
        u, v = edges[idx]
        if v in temp_adj[u]:
            temp_adj[u].remove(v)
        if u in temp_adj[v]:
            temp_adj[v].remove(u)

    used = [False] * n
    dfs(0, used, temp_adj)

    if all(used):
        print("Connected")
    else:
        print("Disconnected")
