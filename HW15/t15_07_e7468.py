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
        if not self.head:
            self.head = self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node

    def ReorderList(self) -> None:
        if not self.head or not self.head.next:
            return

        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        first = self.head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

    def Print(self) -> None:
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
        print()


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    lst = List()
    for x in arr:
        lst.addToTail(x)

    lst.ReorderList()
    lst.Print()
