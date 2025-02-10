import math

def find_x():
    left, right = 0.0, 2.0
    eps = 1e-7

    while right - left > eps:
        mid = (left + right) / 2
        if mid ** 3 + 4 * mid ** 2 + mid - 6 > 0:
            right = mid
        else:
            left = mid

    return left

print(find_x())