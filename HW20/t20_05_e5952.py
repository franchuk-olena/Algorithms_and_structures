class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (4 * size)
        self.lazy = [0] * (4 * size)

    def push(self, node, l, r):
        if self.lazy[node] != 0:
            self.tree[node] += (r - l + 1) * self.lazy[node]
            if l != r:
                self.lazy[2 * node] += self.lazy[node]
                self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0

    def update(self, node, l, r, ql, qr, value):
        self.push(node, l, r)
        if qr < l or r < ql:
            return
        if ql <= l and r <= qr:
            self.lazy[node] += value
            self.push(node, l, r)
            return
        mid = (l + r) // 2
        self.update(2 * node, l, mid, ql, qr, value)
        self.update(2 * node + 1, mid + 1, r, ql, qr, value)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, l, r, ql, qr):
        self.push(node, l, r)
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        return self.query(2 * node, l, mid, ql, qr) + self.query(2 * node + 1, mid + 1, r, ql, qr)


q, L, R, p = map(int, input().split())
st = SegmentTree(256)

for _ in range(q):
    l = min(L, R)
    r = max(L, R)
    st.update(1, 0, 255, l, r, 1)
    s = st.query(1, 0, 255, l, r)
    L = s % p
    R = 255 - s % p

print(st.query(1, 0, 255, 0, 255))