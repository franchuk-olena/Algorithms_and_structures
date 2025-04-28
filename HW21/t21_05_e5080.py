n = int(input())
adjacency_matrix = [list(map(int, input().split())) for _ in range(n)]

count = 0
for i in range(n):
    degree = sum(adjacency_matrix[i])
    if degree == 1:
        count += 1

print(count)
