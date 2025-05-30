import math

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.build(data, 1, 0, self.n - 1)

    def build(self, data, node, l, r):
        if l == r:
            self.tree[node] = data[l]
        else:
            mid = (l + r) // 2
            self.build(data, 2 * node, l, mid)
            self.build(data, 2 * node + 1, mid + 1, r)
            self.tree[node] = math.gcd(self.tree[2 * node], self.tree[2 * node + 1])

    def update(self, node, l, r, idx, value):
        if l == r:
            self.tree[node] = value
        else:
            mid = (l + r) // 2
            if idx <= mid:
                self.update(2 * node, l, mid, idx, value)
            else:
                self.update(2 * node + 1, mid + 1, r, idx, value)
            self.tree[node] = math.gcd(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        left_gcd = self.query(2 * node, l, mid, ql, qr)
        right_gcd = self.query(2 * node + 1, mid + 1, r, ql, qr)
        return math.gcd(left_gcd, right_gcd)

n = int(input())
a = list(map(int, input().split()))
m = int(input())

tree = SegmentTree(a)

for _ in range(m):
    q, l, r = map(int, input().split())
    if q == 1:
        print(tree.query(1, 0, n - 1, l - 1, r - 1))
    else:
        tree.update(1, 0, n - 1, l - 1, r)