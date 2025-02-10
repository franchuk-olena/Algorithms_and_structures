def find_x(C):
    left, right = 1.0, C
    eps = 1e-7

    while right - left > eps:
        mid = (left + right) / 2
        if mid ** 2 + mid ** 0.5 < C:
            left = mid
        else:
            right = mid

    return left


C = float(input().strip())
result = find_x(C)
print(f"{result:.6f}")