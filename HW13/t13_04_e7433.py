def convert_to_base(A: str, P: str) -> str:
    A = int(A)
    P = int(P)

    if A == 0:
        return "0"

    stack = ""

    while A > 0:
        remainder = A % P
        if remainder < 10:
            stack = str(remainder) + stack
        else:
            stack = f'[{remainder}]' + stack
        A //= P

    return stack

A = input().strip()
P = input().strip()

print(convert_to_base(A, P))
