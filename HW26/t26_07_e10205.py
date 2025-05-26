def my_sqrt(x, eps=1e-10):
    if x == 0:
        return 0.0
    low, high = 0.0, max(1.0, x)
    while high - low > eps:
        mid = (low + high) / 2
        if mid * mid > x:
            high = mid
        else:
            low = mid
    return (low + high) / 2


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            self.parent[a] = b
        else:
            self.parent[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1
        return True


def distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return my_sqrt(dx * dx + dy * dy)


def solve():
    t = int(input())
    input()  # порожній рядок після кількості тестів

    for _ in range(t):
        line = input()
        while line.strip() == '':
            line = input()

        n = int(line)
        coords = []
        for _ in range(n):
            x, y = map(int, input().split())
            coords.append((x, y))

        m = int(input())
        dsu = DSU(n)
        for _ in range(m):
            u, v = map(int, input().split())
            dsu.union(u - 1, v - 1)

        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = distance(coords[i], coords[j])
                edges.append((dist, i, j))

        edges.sort(key=lambda x: x[0])

        new_highways = []
        for dist, u, v in edges:
            if dsu.union(u, v):
                new_highways.append((u + 1, v + 1))

        if len(new_highways) == 0:
            print("No new highways need")
        else:
            for u, v in new_highways:
                print(u, v)

        print()


if __name__ == "__main__":
    solve()
