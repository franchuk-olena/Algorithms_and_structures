def can_place_cows(stalls, k, dist):
    cows = 1  # Ставимо першу корову в перше стійло
    last = stalls[0]

    for stall in stalls[1:]:
        if stall - last >= dist:  # Якщо відстань достатня
            cows += 1
            last = stall  # Ставимо корову
            if cows == k:
                return True
    return False


def max_min_distance(stalls, k):
    left, right = 1, stalls[-1] - stalls[0]

    while left <= right:
        mid = (left + right) // 2
        if can_place_cows(stalls, k, mid):
            left = mid + 1  # Пробуємо збільшити відстань
        else:
            right = mid - 1  # Зменшуємо відстань

    return right  # Правий кордон буде відповіддю


n, k = map(int, input().split())
stalls = list(map(int, input().split()))

print(max_min_distance(stalls, k))