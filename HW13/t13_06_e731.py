def convert_prefix_to_infix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    operands = []

    for symbol in reversed(expression):
        if symbol.isalpha():
            operands.append((symbol, 3))
        else:
            op1, prec1 = operands.pop()
            op2, prec2 = operands.pop()
            current_prec = precedence[symbol]

            if prec1 < current_prec:
                op1 = f'({op1})'
            if prec2 < current_prec or (symbol in "-/" and prec2 == current_prec):
                op2 = f'({op2})'

            new_expr = f'{op1}{symbol}{op2}'
            operands.append((new_expr, current_prec))

    return operands[0][0]

expr = input().strip()
print(convert_prefix_to_infix(expr))
