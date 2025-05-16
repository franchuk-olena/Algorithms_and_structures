n = int(input())
grid = [list(input()) for _ in range(n)]

moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
         (1, -2), (1, 2), (2, -1), (2, 1)]

points = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == '@':
            points.append((i, j))

start, end = points[0], points[1]

visited = [[False]*n for _ in range(n)]
prev = [[None]*n for _ in range(n)]
queue = [start]
visited[start[0]][start[1]] = True
head = 0
found = False

while head < len(queue):
    x, y = queue[head]
    head += 1
    if (x, y) == end:
        found = True
        break
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and grid[nx][ny] != '#':
                visited[nx][ny] = True
                prev[nx][ny] = (x, y)
                queue.append((nx, ny))

if not found:
    print("Impossible")
else:
    path = []
    curr = end
    while curr != start:
        path.append(curr)
        curr = prev[curr[0]][curr[1]]
    path.reverse()
    for (x, y) in path[:-1]:
        if grid[x][y] == '.':
            grid[x][y] = '@'
    for row in grid:
        print("".join(row))
