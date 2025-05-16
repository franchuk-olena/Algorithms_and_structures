n = int(input())
grid = [list(input()) for _ in range(n)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

start = end = None
for i in range(n):
    for j in range(n):
        if grid[i][j] == '@':
            start = (i, j)
        elif grid[i][j] == 'X':
            end = (i, j)

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n and (grid[x][y] == '.' or grid[x][y] == 'X')

def bfs(start, end):
    queue = [start]
    visited = [[False for _ in range(n)] for _ in range(n)]
    prev = [[None for _ in range(n)] for _ in range(n)]
    visited[start[0]][start[1]] = True

    front = 0
    while front < len(queue):
        x, y = queue[front]
        front += 1

        if (x, y) == end:
            return prev

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                prev[nx][ny] = (x, y)
                queue.append((nx, ny))
    return None

prev = bfs(start, end)

if prev is None:
    print("N")
else:
    print("Y")

    path = []
    cur = end
    while cur != start:
        path.append(cur)
        cur = prev[cur[0]][cur[1]]
    path.append(start)

    for i in range(n):
        row = ""
        for j in range(n):
            if (i, j) == start:
                row += "@"
            elif (i, j) == end:
                row += "+"
            elif (i, j) in path:
                row += "+"
            else:
                row += grid[i][j]
        print(row)