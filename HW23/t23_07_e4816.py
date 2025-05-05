def dfs(v, adj, visited, component):
    visited[v] = True
    component.append(v + 1)
    for u in adj[v]:
        if not visited[u]:
            dfs(u, adj, visited, component)

n, m = map(int, input().split())
adj = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * n
components = []

for i in range(n):
    if not visited[i]:
        component = []
        dfs(i, adj, visited, component)
        components.append(component)

print(len(components))
for comp in components:
    print(len(comp))
    print(' '.join(map(str, comp)))
