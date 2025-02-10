# Функція для підрахунку кількості елементів, рівних x
def count_occurrences(array, x):
    left, right = 0, len(array) - 1
    # Пошук першого входження
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] < x:
            left = mid + 1
        elif array[mid] > x:
            right = mid - 1
        else:
            first = mid
            while first > 0 and array[first - 1] == x:
                first -= 1
            # Пошук останнього входження
            last = mid
            while last < len(array) - 1 and array[last + 1] == x:
                last += 1
            return last - first + 1
    return 0

# Вхідні дані
n = int(input())  # кількість тварин
animals = list(map(int, input().split()))  # види тварин
m = int(input())  # кількість запитів
queries = list(map(int, input().split()))  # запити

# Відповідаємо на кожен запит
for query in queries:
    print(count_occurrences(animals, query))
