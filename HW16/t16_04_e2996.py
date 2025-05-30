class Node:
    def __init__(self, idx, d):
        self.idx = idx
        self.d = d
        self.children = []

def sd(node):
    s = node.d
    if node.children:
        s += min(sd(child) for child in node.children)
    return s

n = int(input())
nodes = [None] * (n + 1)
for i in range(1, n + 1):
    nodes[i] = Node(i, 0)
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    nodes[i].d = data[0]
    k = data[1]
    for j in range(k):
        nodes[i].children.append(nodes[data[2 + j]])
print(sd(nodes[1]))