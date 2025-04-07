MODULO = 301907


def count_valid_sequences(pattern: str) -> int:
    n = len(pattern)
    if n % 2 == 1:
        return 0

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(n):
        for balance in range(n):
            if dp[i][balance] == 0:
                continue

            if pattern[i] in "(?":
                dp[i + 1][balance + 1] = (dp[i + 1][balance + 1] + dp[i][balance]) % MODULO

            if pattern[i] in ")?" and balance > 0:
                dp[i + 1][balance - 1] = (dp[i + 1][balance - 1] + dp[i][balance]) % MODULO

    return dp[n][0]


pattern = input().strip()
print(count_valid_sequences(pattern))

