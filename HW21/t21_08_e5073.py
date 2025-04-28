n, m = map(int, input().split())
edges = set()

has_multiple_edges = False

for _ in range(m):
    u, v = map(int, input().split())
    if (u, v) in edges:
        has_multiple_edges = True
    edges.add((u, v))

print("YES" if has_multiple_edges else "NO")
