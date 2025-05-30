import math

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.gcd_tree = [0] * (4 * self.n)
        self.lcm_tree = [1] * (4 * self.n)
        self.build(data, 1, 0, self.n - 1)

    def build(self, data, node, l, r):
        if l == r:
            self.gcd_tree[node] = data[l]
            self.lcm_tree[node] = data[l]
        else:
            mid = (l + r) // 2
            self.build(data, 2 * node, l, mid)
            self.build(data, 2 * node + 1, mid + 1, r)
            self.gcd_tree[node] = math.gcd(self.gcd_tree[2 * node], self.gcd_tree[2 * node + 1])
            self.lcm_tree[node] = self.lcm(self.lcm_tree[2 * node], self.lcm_tree[2 * node + 1])

    def update(self, node, l, r, idx, value):
        if l == r:
            self.gcd_tree[node] = value
            self.lcm_tree[node] = value
        else:
            mid = (l + r) // 2
            if idx <= mid:
                self.update(2 * node, l, mid, idx, value)
            else:
                self.update(2 * node + 1, mid + 1, r, idx, value)
            self.gcd_tree[node] = math.gcd(self.gcd_tree[2 * node], self.gcd_tree[2 * node + 1])
            self.lcm_tree[node] = self.lcm(self.lcm_tree[2 * node], self.lcm_tree[2 * node + 1])

    def gcd_query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return 0
        if ql <= l and r <= qr:
            return self.gcd_tree[node]
        mid = (l + r) // 2
        left = self.gcd_query(2 * node, l, mid, ql, qr)
        right = self.gcd_query(2 * node + 1, mid + 1, r, ql, qr)
        return math.gcd(left, right)

    def lcm_query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return 1
        if ql <= l and r <= qr:
            return self.lcm_tree[node]
        mid = (l + r) // 2
        left = self.lcm_query(2 * node, l, mid, ql, qr)
        right = self.lcm_query(2 * node + 1, mid + 1, r, ql, qr)
        return self.lcm(left, right)

    def lcm(self, a, b):
        return a * b // math.gcd(a, b)

n = int(input())
a = list(map(int, input().split()))
m = int(input())
tree = SegmentTree(a)
for _ in range(m):
    q, l, r = map(int, input().split())
    if q == 1:
        gcd_val = tree.gcd_query(1, 0, n - 1, l - 1, r - 1)
        lcm_val = tree.lcm_query(1, 0, n - 1, l - 1, r - 1)
        if gcd_val < lcm_val:
            print("wins")
        elif gcd_val > lcm_val:
            print("loser")
        else:
            print("draw")
    else:
        tree.update(1, 0, n - 1, l - 1, r)