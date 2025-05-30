def qsort(array, left, right):
    if left >= right:
        return
    pivot = array[(left + right) // 2]
    i, j = left, right
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    qsort(array, left, j)
    qsort(array, i, right)

n = int(input())
array = list(map(int, input().split()))

qsort(array, 0, n - 1)
print(*array)