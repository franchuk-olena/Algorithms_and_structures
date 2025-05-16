m, n = map(int, input().split())

grid = [list(input()) for _ in range(m)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[False for _ in range(n)] for _ in range(m)]

def dfs(x, y):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny] and grid[nx][ny] == '#':
                    visited[nx][ny] = True
                    stack.append((nx, ny))

count = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == '#' and not visited[i][j]:
            visited[i][j] = True
            dfs(i, j)
            count += 1

print(count)
