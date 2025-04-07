class Node:
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.prev = prev_node
        self.next = next_node


class Deque:
    def __init__(self):
        self.front_node = None
        self.rear_node = None

    def push_front(self, n):
        new_node = Node(n, None, self.front_node)
        if self.front_node is None:
            self.front_node = self.rear_node = new_node
        else:
            self.front_node.prev = new_node
            self.front_node = new_node
        print("ok")

    def push_back(self, n):
        new_node = Node(n, self.rear_node, None)
        if self.rear_node is None:
            self.front_node = self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node
        print("ok")

    def pop_front(self):
        if self.front_node is None:
            print("error")
        else:
            print(self.front_node.value)
            self.front_node = self.front_node.next
            if self.front_node is None:
                self.rear_node = None
            else:
                self.front_node.prev = None

    def pop_back(self):
        if self.rear_node is None:
            print("error")
        else:
            print(self.rear_node.value)
            self.rear_node = self.rear_node.prev
            if self.rear_node is None:
                self.front_node = None
            else:
                self.rear_node.next = None

    def front(self):
        if self.front_node is None:
            print("error")
        else:
            print(self.front_node.value)

    def back(self):
        if self.rear_node is None:
            print("error")
        else:
            print(self.rear_node.value)

    def size(self):
        count = 0
        current = self.front_node
        while current is not None:
            count += 1
            current = current.next
        print(count)

    def clear(self):
        self.front_node = self.rear_node = None
        print("ok")

    def exit(self):
        print("bye")
        return False  # повертається False для завершення циклу


if __name__ == "__main__":
    deque = Deque()
    while True:
        command = input().strip().split()
        if command[0] == "push_front":
            deque.push_front(int(command[1]))
        elif command[0] == "push_back":
            deque.push_back(int(command[1]))
        elif command[0] == "pop_front":
            deque.pop_front()
        elif command[0] == "pop_back":
            deque.pop_back()
        elif command[0] == "front":
            deque.front()
        elif command[0] == "back":
            deque.back()
        elif command[0] == "size":
            deque.size()
        elif command[0] == "clear":
            deque.clear()
        elif command[0] == "exit":
            if deque.exit() == False:
                break
