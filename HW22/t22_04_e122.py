def count_routes(n, k, a, b, d, edges):
    from collections import defaultdict

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    count = 0

    def dfs(current, depth, visited):
        nonlocal count
        if depth > d:
            return
        if current == b and depth <= d:
            count += 1
            return
        for neighbor in graph[current]:
            if neighbor not in visited:
                dfs(neighbor, depth + 1, visited | {neighbor})

    dfs(a, 0, {a})
    return count

n, k, a, b, d = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(k)]

print(count_routes(n, k, a, b, d, edges))
