class Node:
    def __init__(self, idx, color):
        self.idx = idx
        self.color = color
        self.children = []

def dfs(node):
    s = {node.color}
    for child in node.children:
        t = dfs(child)
        if len(t) > len(s):
            s, t = t, s
        s |= t
    ans[node.idx] = len(s)
    return s

n = int(input())
nodes = [None] * (n + 1)
root = None
for i in range(1, n + 1):
    nodes[i] = Node(i, 0)
for i in range(1, n + 1):
    p, c = map(int, input().split())
    nodes[i].color = c
    if p == 0:
        root = nodes[i]
    else:
        nodes[p].children.append(nodes[i])
ans = [0] * (n + 1)
dfs(root)
print(" ".join(str(ans[i]) for i in range(1, n + 1)))