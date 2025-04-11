def solve():
    n = int(input())
    parents = [0] * (n + 1)
    colors = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        p, c = map(int, input().split())
        parents[i] = p
        colors[i] = c
        if p != 0:
            adj[p].append(i)

    subtree_color_counts = [0] * (n + 1)

    def get_subtree_colors(u):
        subtree_colors = {colors[u]}
        for v in adj[u]:
            subtree_colors.update(get_subtree_colors(v))
        return subtree_colors

    for i in range(1, n + 1):
        subtree_colors = get_subtree_colors(i)
        subtree_color_counts[i] = len(subtree_colors)

    print(*subtree_color_counts[1:])

if __name__ == "__main__":
    solve()