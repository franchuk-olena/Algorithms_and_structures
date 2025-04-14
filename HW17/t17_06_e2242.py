class Node:
    def __init__(self, x):
        self.x = x
        self.l = None
        self.r = None

def add(t, x):
    if t is None:
        return Node(x)
    if x < t.x:
        t.l = add(t.l, x)
    else:
        t.r = add(t.r, x)
    return t

def build(stacks):
    t = None
    for s in reversed(stacks):
        for ch in s:
            t = add(t, ch)
    return t

def preorder(t):
    if t is None:
        return ''
    return t.x + preorder(t.l) + preorder(t.r)

if __name__ == "__main__":
    stacks = []
    while True:
        try:
            line = input().strip()
            if line == '*':
                break
            stacks.append(line)
        except EOFError:
            break

    tree = build(stacks)
    print(preorder(tree))
