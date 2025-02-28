def selection_sort_times(times):
    n = len(times)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if times[j] < times[min_index]:
                min_index = j
        times[i], times[min_index] = times[min_index], times[i]

n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

selection_sort_times(times)
for time in times:
    print(*time)
