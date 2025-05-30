def conver(A, P ):

    if A == 0:
        return "0"

    stack = []

    while A > 0:
        remainder = A % P
        stack.append(remainder)
        A //= P

    res = ''
    while stack:
        digit = stack.pop()
        if digit <= 9:
            res += str(digit)
        else:
            res += f"[{digit}]"

    return res



A = int(input())
P = int(input())

print(conver(A, P))