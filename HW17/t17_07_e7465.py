class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None

    def Insert(self, val):
        if not self.head:
            self.head = TreeNode(val)
        else:
            self._insert(self.head, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert(node.right, val)

    def IsSameTree(self, other_tree):
        return 1 if self._is_same(self.head, other_tree.head) else 0

    def _is_same(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return (node1.val == node2.val) and self._is_same(node1.left, node2.left) and self._is_same(node1.right, node2.right)

if __name__ == "__main__":
    n = int(input())
    arr1 = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))

    tree1 = Tree()
    tree2 = Tree()

    for val in arr1:
        tree1.Insert(val)

    for val in arr2:
        tree2.Insert(val)

    print(tree1.IsSameTree(tree2))
