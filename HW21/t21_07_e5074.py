n, m = map(int, input().split())
degree = [0] * n

for _ in range(m):
    u, v = map(int, input().split())
    degree[u - 1] += 1
    degree[v - 1] += 1

for d in degree:
    print(d)
