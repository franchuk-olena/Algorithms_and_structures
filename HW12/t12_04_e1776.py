import sys


def can_rearrange(n, target_order):
    stack = []  # Станція (стек)
    current = 1  # Очікуваний вагон для виходу

    for wagon in target_order:
        while current <= n and (not stack or stack[-1] != wagon):
            stack.append(current)
            current += 1

        if stack and stack[-1] == wagon:
            stack.pop()
        else:
            return "No"

    return "Yes"


def main():
    input_data = sys.stdin.read().strip().split("\n")
    index = 0

    while index < len(input_data):
        n = int(input_data[index])
        if n == 0:
            break
        index += 1

        results = []
        while index < len(input_data) and input_data[index] != "0":
            target_order = list(map(int, input_data[index].split()))
            results.append(can_rearrange(n, target_order))
            index += 1

        print("\n".join(results))
        print()  # Порожній рядок між тестами
        index += 1  # Пропускаємо нульовий рядок


if __name__ == "__main__":
    main()
