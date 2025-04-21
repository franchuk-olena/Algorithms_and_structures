def is_min_heap(arr):
    n = len(arr)
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] > arr[left]:
            return False

        if right < n and arr[i] > arr[right]:
            return False

    return True


def is_max_heap(arr):
    n = len(arr)
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            return False

        if right < n and arr[i] < arr[right]:
            return False

    return True


def check_heap(arr):
    if is_min_heap(arr):
        return "YES"
    elif is_max_heap(arr):
        return "YES"  #
    else:
        return "NO"

n = int(input())
arr = list(map(int, input().split()))
print(check_heap(arr))
