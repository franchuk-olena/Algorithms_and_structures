def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    sorted_arr = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


n = int(input())
array = [tuple(map(int, input().split())) for _ in range(n)]

sort = merge_sort(array)

for robot in sort:
    print(robot[0], robot[1])