def bubble_sort_count_swaps(lst):
    n = len(lst)
    swap_count = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swap_count += 1
    return swap_count
n = int(input())
lst = list(map(int, input().split()))
print(bubble_sort_count_swaps(lst))