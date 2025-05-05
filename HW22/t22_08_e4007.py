from collections import deque


def bfs(start, end):
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()
        if current == end:
            return path
        for next_num in generate_neighbors(current):
            if next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, path + [next_num]))

    return []


def generate_neighbors(number):
    num_str = str(number)
    neighbors = set()

    # 1. Збільшити першу цифру на 1, якщо вона не 9
    if num_str[0] != '9':
        new_num = str(int(num_str[0]) + 1) + num_str[1:]
        neighbors.add(int(new_num))

    # 2. Зменшити останню цифру на 1, якщо вона не 1
    if num_str[3] != '1':
        new_num = num_str[:3] + str(int(num_str[3]) - 1)
        neighbors.add(int(new_num))

    # 3. Циклічно зсунути усі цифри на одну праворуч
    new_num = num_str[-1] + num_str[:-1]
    neighbors.add(int(new_num))

    # 4. Циклічно зсунути усі цифри на одну ліворуч
    new_num = num_str[1:] + num_str[0]
    neighbors.add(int(new_num))

    return neighbors

start = int(input())
end = int(input())

path = bfs(start, end)

for number in path:
    print(number)
