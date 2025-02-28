def insertion_sort_with_steps(lst):
    n = len(lst)
    sorted_flag = True

    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

        if i != j + 1:
            sorted_flag = False
            print(*lst)

    if sorted_flag:
        return
n = int(input())
lst = list(map(int, input().split()))
insertion_sort_with_steps(lst)
