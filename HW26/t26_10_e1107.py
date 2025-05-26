def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, c = map(int, input().split())
        edges.append((u - 1, v - 1, c))

    edges.sort(key=lambda x: x[2])

    parent = list(range(n))
    rank = [0] * n

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_j] = root_i
                rank[root_i] += 1
            return True
        return False

    s1_cost = 0
    mst_edges = []
    num_components = n

    parent = list(range(n))
    rank = [0] * n

    for u, v, c in edges:
        if union(u, v):
            s1_cost += c
            mst_edges.append((u, v, c))
            num_components -= 1
            if num_components == 1:
                break

    if num_components > 1:
        pass

    s2_cost = float('inf')

    for removed_edge_idx in range(len(mst_edges)):
        current_mst_cost = 0
        current_mst_edges_count = 0

        parent = list(range(n))
        rank = [0] * n
        current_num_components = n

        for i, (u, v, c) in enumerate(edges):
            if i == edges.index(mst_edges[removed_edge_idx]):  # Skip the removed edge
                continue

            if union(u, v):
                current_mst_cost += c
                current_mst_edges_count += 1
                current_num_components -= 1

                if current_num_components == 1:
                    break

        if current_num_components == 1:
            s2_cost = min(s2_cost, current_mst_cost)

    print(s1_cost, s2_cost)


solve()