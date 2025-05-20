n = int(input())
INF = 10**9
a = []

for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)

dist = [0] * n
pred = [-1] * n

x = -1

for i in range(n):
    x = -1
    for u in range(n):
        for v in range(n):
            if a[u][v] != 100000 and dist[v] > dist[u] + a[u][v]:
                dist[v] = dist[u] + a[u][v]
                pred[v] = u
                x = v

if x == -1:
    print("NO")
else:
    print("YES")
    
    for _ in range(n):
        x = pred[x]

    cycle = []
    cur = x
    while True:
        cycle.append(cur)
        if len(cycle) > 1 and cur == x:
            break
        cur = pred[cur]

    cycle = list(reversed(cycle))
    print(len(cycle))
    print(' '.join(str(v + 1) for v in cycle))
