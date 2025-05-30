def prefix_to_infix(expr):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []

    for char in reversed(expr):
        if char.isalpha():
            stack.append((char, 3))
        else:
            left, left_prec = stack.pop()
            right, right_prec = stack.pop()
            curr_prec = precedence[char]

            if left_prec < curr_prec:
                left = f'({left})'
            if right_prec < curr_prec or (char in "-/" and right_prec == curr_prec):
                right = f'({right})'

            new_expr = f'{left}{char}{right}'
            stack.append((new_expr, curr_prec))

    return stack[0][0]

expr = input().strip()

print(prefix_to_infix(expr))