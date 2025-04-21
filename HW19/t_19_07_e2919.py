class Node:
    def __init__(self):
        self.left = -1
        self.right = -1
        self.potential = -1


def calc_potential(node, tree):
    if tree[node].left == -1 and tree[node].right == -1:
        return 0
    if tree[node].left == -1 or tree[node].right == -1:
        return 1
    return 2


def solve(N, edges):
    tree = [Node() for _ in range(N)]
    parent = [-1] * N

    for i in range(N):
        l, r = edges[i]
        tree[i].left = l - 1 if l != -1 else -1
        tree[i].right = r - 1 if r != -1 else -1
        if tree[i].left != -1:
            parent[tree[i].left] = i
        if tree[i].right != -1:
            parent[tree[i].right] = i

    for i in range(N):
        tree[i].potential = calc_potential(i, tree)

        if tree[i].right != -1 and tree[i].left == -1:
            return i + 1

        if tree[i].left != -1 and tree[i].right != -1:
            if tree[tree[i].left].potential < tree[tree[i].right].potential:
                return i + 1

    return -1

N = int(input())
edges = [tuple(map(int, input().split())) for _ in range(N)]
print(solve(N, edges))
