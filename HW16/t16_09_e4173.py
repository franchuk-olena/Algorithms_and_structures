class Node:
    def __init__(self, idx):
        self.idx = idx
        self.parent = None
        self.children = []
        self.h = None

def f1(node):
    for child in node.children:
        f1(child)
    node.h = hash((len(node.children), tuple(child.h for child in node.children)))

def f2(node):
    if node is None:
        return
    new_h = hash((len(node.children), tuple(child.h for child in node.children)))
    if new_h != node.h:
        node.h = new_h
        f2(node.parent)

n, m = map(int, input().split())
nodes = [None] + [Node(i) for i in range(1, n + 1)]
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    k = data[0]
    if k:
        cnt = data[1]
        for child_idx in data[2:2+cnt]:
            child = nodes[child_idx]
            child.parent = nodes[i]
            nodes[i].children.append(child)
root = nodes[1]
f1(root)
seen = {root.h: 0}
result = (-1, -1)
for mod in range(1, m + 1):
    s, f = map(int, input().split())
    node_s = nodes[s]
    old_parent = node_s.parent
    old_parent.children.remove(node_s)
    f2(old_parent)
    node_f = nodes[f]
    node_s.parent = node_f
    node_f.children.append(node_s)
    f2(node_f)
    if root.h in seen:
        result = (seen[root.h], mod)
        break
    else:
        seen[root.h] = mod
if result[0] == -1:
    print(-1)
else:
    print(result[0], result[1])