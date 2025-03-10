def generate_permutations(n, k, current=[], used=set()):
    if len(current) == k:
        print(*current)
        return

    for i in range(1, n + 1):
        if i not in used:
            used.add(i)
            generate_permutations(n, k, current + [i], used)
            used.remove(i)


if __name__ == "__main__":
    n, k = map(int, input().split())
    generate_permutations(n, k)