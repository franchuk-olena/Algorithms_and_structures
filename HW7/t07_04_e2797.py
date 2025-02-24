EMPTY = None

class HashTable:
    def __init__(self, size=100003):
        self.size = size
        self.table = [None] * self.size
        self.count = 0

    def hash(self, key: int):
        return key % self.size

    def add(self, key: int):
        index = self.hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index] == key:
                return
            index = (index + 1) % self.size
            if index == original_index:
                break
        else:
            self.table[index] = key
            self.count += 1

    def get_count(self):
        return self.count


if __name__ == "__main__":
    N = int(input())  # Читаємо кількість з'єднань
    numbers = input().split()  # Читаємо номери телефонів як рядки

    hash_table = HashTable()  # Створюємо хеш-таблицю

    for number in numbers:
        number_int = int(number)  # Перетворюємо номер телефону на ціле число
        hash_table.add(number_int)  # Додаємо номер телефону в таблицю

    print(hash_table.get_count())  # Виводимо кількість унікальних номерів
