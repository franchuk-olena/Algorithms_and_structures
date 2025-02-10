def find_min_x():
    left, right = 0.0, 10.0
    eps = 1e-7

    while right - left > eps:
        mid = (left + right) / 2
        if mid ** 3 + mid + 1 > 5:
            right = mid
        else:
            left = mid

    return left

print(find_min_x())