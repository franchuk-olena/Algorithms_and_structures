class Node:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.left = None
        self.right = None
        self.first = 0
        self.last = 0
        self.prefix = 1
        self.suffix = 1
        self.maxlen = 1

def build(a, l, r):
    node = Node(l, r)
    if l == r:
        node.first = node.last = a[l]
        return node
    m = (l + r) // 2
    node.left = build(a, l, m)
    node.right = build(a, m + 1, r)
    return merge(node)

def merge(node):
    l, r = node.left, node.right
    node.first = l.first
    node.last = r.last
    node.prefix = l.prefix
    if l.prefix == l.r - l.l + 1 and l.last <= r.first:
        node.prefix += r.prefix
    node.suffix = r.suffix
    if r.suffix == r.r - r.l + 1 and l.last <= r.first:
        node.suffix += l.suffix
    node.maxlen = max(l.maxlen, r.maxlen)
    if l.last <= r.first:
        node.maxlen = max(node.maxlen, l.suffix + r.prefix)
    return node

def update(node, idx, val):
    if node.l == node.r:
        node.first = node.last = val
        node.prefix = node.suffix = node.maxlen = 1
        return
    if idx <= node.left.r:
        update(node.left, idx, val)
    else:
        update(node.right, idx, val)
    merge(node)

def query(node, l, r):
    if node.r < l or node.l > r:
        dummy = Node(0, 0)
        dummy.first = dummy.last = -1
        dummy.prefix = dummy.suffix = dummy.maxlen = 0
        return dummy
    if l <= node.l and node.r <= r:
        return node
    left = query(node.left, l, r)
    right = query(node.right, l, r)
    temp = Node(0, 0)
    temp.left = left
    temp.right = right
    return merge(temp)

n = int(input())
a = list(map(int, input().split()))
tree = build(a, 0, n - 1)

m = int(input())
for _ in range(m):
    q, l, r = map(int, input().split())
    l -= 1
    if q == 1:
        print(query(tree, l, r - 1).maxlen)
    else:
        update(tree, l, r)
