def bracket(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return "no"
            stack.pop()

    return "yes" if not stack else "no"


sequence = input().strip()

print(bracket(sequence))