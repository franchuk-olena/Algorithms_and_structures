class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)
        print("ok")

    def pop(self):
        if self.stack:
            print(self.stack.pop())
        else:
            print("error")

    def back(self):
        if self.stack:
            print(self.stack[-1])
        else:
            print("error")

    def size(self):
        print(len(self.stack))

    def clear(self):
        self.stack.clear()
        print("ok")


def main():
    stack = Stack()
    while True:
        command = input().strip()
        if command.startswith("push"):
            _, n = command.split()
            stack.push(int(n))
        elif command == "pop":
            stack.pop()
        elif command == "back":
            stack.back()
        elif command == "size":
            stack.size()
        elif command == "clear":
            stack.clear()
        elif command == "exit":
            print("bye")
            break


if __name__ == "__main__":
    main()
