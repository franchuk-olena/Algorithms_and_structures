class RecursiveNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None
        self.depth = -1

class RecursiveTree:
    def __init__(self, n, parents):
        self.n = n
        self.nodes = [RecursiveNode(i) for i in range(n)]
        self.root = self.nodes[0]
        if n > 1:
            for i, p_val in enumerate(parents):
                child = self.nodes[i + 1]
                parent = self.nodes[p_val]
                child.parent = parent
                parent.children.append(child)
        self._calculate_depths()

    def _calculate_depths(self):
        def dfs(node, d):
            node.depth = d
            for child in node.children:
                dfs(child, d + 1)
        dfs(self.root, 0)

    def get_node(self, value):
        return self.nodes[value]

    def _get_ancestors(self, node):
        ancestors = []
        while node:
            ancestors.append(node)
            node = node.parent
        return ancestors

    def lca(self, node1_val, node2_val):
        node1 = self.get_node(node1_val)
        node2 = self.get_node(node2_val)

        ancestors1 = self._get_ancestors(node1)
        ancestors2 = self._get_ancestors(node2)

        lca_node = None
        i = len(ancestors1) - 1
        j = len(ancestors2) - 1

        while i >= 0 and j >= 0 and ancestors1[i] == ancestors2[j]:
            lca_node = ancestors1[i]
            i -= 1
            j -= 1

        return lca_node.value if lca_node else self.root.value

def solve():
    line1 = input().split()
    n = int(line1[0])
    m = int(line1[1])

    if n > 1:
        parents_input = list(map(int, input().split()))
    else:
        parents_input = []

    line3 = input().split()
    a1 = int(line3[0])
    a2 = int(line3[1])

    line4 = input().split()
    x = int(line4[0])
    y = int(line4[1])
    z = int(line4[2])

    tree = RecursiveTree(n, parents_input)

    a = [0] * (2 * m + 1)
    a[1] = a1
    a[2] = a2
    for i in range(3, 2 * m + 1):
        a[i] = (x * a[i - 2] + y * a[i - 1] + z) % n

    total_sum = 0
    prev_lca = -1

    for i in range(1, m + 1):
        u = a[2 * i - 1]
        v = a[2 * i]
        if i > 1:
            u = (u + prev_lca) % n

        current_lca = tree.lca(u, v)
        total_sum += current_lca
        prev_lca = current_lca

    print(total_sum)

if __name__ == "__main__":
    solve()