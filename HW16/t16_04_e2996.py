def solve():
    n = int(input())
    costs = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        line = input().split()
        costs[i] = int(line[0])
        k = int(line[1])
        if k > 0:
            adj[i].extend(map(int, line[2:]))

    def min_bribe(u):
        if not adj[u]:
            return costs[u]

        min_cost_with_one_subordinate = float('inf')

        for v in adj[u]:
            cost_with_one_subordinate = min_bribe(v) + costs[u]
            min_cost_with_one_subordinate = min(min_cost_with_one_subordinate, cost_with_one_subordinate)

        return min_cost_with_one_subordinate

    result = min_bribe(1)
    print(result)

if __name__ == "__main__":
    solve()