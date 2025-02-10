import math

def find_x():
    left, right = 1.6, 3.0
    eps = 1e-7

    while right - left > eps:
        mid = (left + right) / 2
        if math.sin(mid) < mid / 3:
            right = mid
        else:
            left = mid

    return left

print(find_x())