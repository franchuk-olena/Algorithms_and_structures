class HashTable:
    def __init__(self, capacity=10007):
        self.capacity = capacity
        self.table = [None] * capacity

    def _hash(self, key):
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 37 + ord(char)) % self.capacity
        return hash_value

    def add(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index] == key:
                return
            index = (index + 1) % self.capacity
        self.table[index] = key

    def contains(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index] == key:
                return True
            index = (index + 1) % self.capacity
        return False

    def get_all(self):
        return {word for word in self.table if word is not None}


def main():
    # Зчитуємо вхідні дані
    n, m = map(int, input().split())

    # Створюємо хеш-таблиці для словника та тексту
    dictionary = HashTable()
    for _ in range(n):
        dictionary.add(input().strip().lower())

    text_words = HashTable()
    for _ in range(m):
        line = input().strip().lower()
        word = ""
        for char in line:
            if char.isalpha():
                word += char
            elif word:
                text_words.add(word)
                word = ""
        if word:
            text_words.add(word)

    # Перевірка умов
    dict_words = dictionary.get_all()
    text_word_set = text_words.get_all()

    if not text_word_set.issubset(dict_words):
        print("Some words from the text are unknown.")
    elif not dict_words.issubset(text_word_set):
        print("The usage of the vocabulary is not perfect.")
    else:
        print("Everything is going to be OK.")


if __name__ == "__main__":
    main()