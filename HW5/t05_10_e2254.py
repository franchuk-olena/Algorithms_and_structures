import sys


def min_transport_cost(X, R, k):
    """Знаходить мінімальну вартість транспортування для k полів"""
    prefix = [0] * (R + 1)
    for i in range(R):
        prefix[i + 1] = prefix[i] + X[i]

    min_cost = float('inf')

    # Проходимо по всіх можливих підмножинах довжиною k
    for i in range(R - k + 1):
        median_idx = i + k // 2  # Оптимальне місце для сховища
        median_x = X[median_idx]

        left_cost = median_x * (median_idx - i) - (prefix[median_idx] - prefix[i])
        right_cost = (prefix[i + k] - prefix[median_idx + 1]) - median_x * ((i + k - 1) - median_idx)

        min_cost = min(min_cost, left_cost + right_cost)

    return min_cost


def max_trucks(X, R, L, B):
    """Бінарний пошук максимальної кількості полів, які можна обслужити"""
    left, right = 0, R
    while left < right:
        mid = (left + right + 1) // 2
        if min_transport_cost(X, R, mid) <= B:
            left = mid
        else:
            right = mid - 1
    return left


# Зчитування вхідних даних
R, L, B = map(int, sys.stdin.readline().split())
X = [int(sys.stdin.readline()) for _ in range(R)]

# Вивід відповіді
print(max_trucks(X, R, L, B))

