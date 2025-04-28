n, m = map(int, input().split())
edges = set()

for _ in range(m):
    u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    edges.add((u, v))

expected_edges = n * (n - 1) // 2

if len(edges) == expected_edges:
    print("YES")
else:
    print("NO")
