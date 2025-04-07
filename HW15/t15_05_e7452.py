class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: 'Node | None' = None

class List:
    def __init__(self):
        self.head: 'Node | None' = None
        self.tail: 'Node | None' = None

    def addToTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node

    def Print(self) -> None:
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def PrintReverse(self) -> None:
        def _collect_reverse(node):
            if node is None:
                return []
            return _collect_reverse(node.next) + [node.data]
        result = _collect_reverse(self.head)
        print(' '.join(map(str, result)))

n = int(input())
numbers = list(map(int, input().split()))

lst = List()
for number in numbers:
    lst.addToTail(number)

# res у прямому порядку
lst.Print()

# res у зворотному порядку
lst.PrintReverse()


#ВИКОРИСТАЛА ОДНОЗВЯЗНИЙ СПИСОК