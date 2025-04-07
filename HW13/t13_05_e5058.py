def is_valid_bracket_sequence(sequence: str) -> str:
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for char in sequence:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets:
            if not stack or stack.pop() != brackets[char]:
                return "no"

    return "yes" if not stack else "no"

sequence = input().strip()

print(is_valid_bracket_sequence(sequence))
