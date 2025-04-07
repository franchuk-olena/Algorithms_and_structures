class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0) if self.items else None

    def __bool__(self):
        return bool(self.items)


n = int(input().strip())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

first_queue = Queue()
second_queue = Queue()

for card in first:
    first_queue.push(card)
for card in second:
    second_queue.push(card)

max_rounds = 200000
rounds = 0

while first_queue and second_queue:
    if rounds >= max_rounds:
        print("draw")
        exit()

    card1 = first_queue.pop()
    card2 = second_queue.pop()

    if (card1 > card2 and not (card1 == n - 1 and card2 == 0)) or (card1 == 0 and card2 == n - 1):
        first_queue.push(card1)
        first_queue.push(card2)
    else:
        second_queue.push(card1)
        second_queue.push(card2)

    rounds += 1

print(f"first {rounds}" if first_queue else f"second {rounds}")
