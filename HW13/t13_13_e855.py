def generate(n, expr='', stack=[]):
    if len(expr) == n:
        if not stack:
            print(expr)
        return


    generate(n, expr + '(', stack + ['('])
    generate(n, expr + '[', stack + ['['])


    if stack:
        if stack[-1] == '(':
            generate(n, expr + ')', stack[:-1])
        elif stack[-1] == '[':
            generate(n, expr + ']', stack[:-1])


n = int(input())
if n % 2 == 0:
    generate(n)
