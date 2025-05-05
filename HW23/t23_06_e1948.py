n, m = map(int, input().split())
adj = [[] for _ in range(n)]
in_deg = [0] * n

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    in_deg[v] += 1

queue = []
for i in range(n):
    if in_deg[i] == 0:
        queue.append(i)

order = []
while queue:
    u = queue.pop()
    order.append(u + 1)
    for v in adj[u]:
        in_deg[v] -= 1
        if in_deg[v] == 0:
            queue.append(v)

if len(order) == n:
    print(*order)
else:
    print(-1)
