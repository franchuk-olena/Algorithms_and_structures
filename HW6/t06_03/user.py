"""
Каталог бібліотеки художніх книг.
Бібліотека може містити кілька книг одного автора.
"""

LIBRARY_CAPACITY = 10007  # Оптимальний розмір хеш-таблиці для унікальних ключів


class HashTable:
    """ Реалізація хеш-таблиці з відкритою адресацією для зберігання книг. """

    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        self.deleted_marker = object()

    def _hash(self, key, probe):
        h1 = hash(key) % self.capacity
        h2 = 1 + (hash(key) % (self.capacity - 1))
        return (h1 + probe * h2) % self.capacity

    def insert(self, key, value):
        probe = 0
        while probe < self.capacity:
            index = self._hash(key, probe)
            if self.table[index] in (None, self.deleted_marker) or self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            probe += 1
        raise RuntimeError("Хеш-таблиця переповнена!")

    def search(self, key):
        probe = 0
        while probe < self.capacity:
            index = self._hash(key, probe)
            if self.table[index] is None:
                return None
            if self.table[index] is not self.deleted_marker and self.table[index][0] == key:
                return self.table[index][1]
            probe += 1
        return None

    def delete(self, key):
        probe = 0
        while probe < self.capacity:
            index = self._hash(key, probe)
            if self.table[index] is None:
                return
            if self.table[index] is not self.deleted_marker and self.table[index][0] == key:
                self.table[index] = self.deleted_marker
                return
            probe += 1


library_db = None  # Основна хеш-таблиця для книг
author_catalog = None  # Словник для зберігання списків книг за авторами


def init():
    global library_db, author_catalog
    library_db = HashTable(LIBRARY_CAPACITY)
    author_catalog = {}


def addBook(author, title):
    """ Додає книгу до каталогу.
    :param author: Ім'я автора книги
    :param title: Назва книги
    """
    global library_db, author_catalog
    book_key = (author, title)
    library_db.insert(book_key, True)

    if author not in author_catalog:
        author_catalog[author] = set()
    author_catalog[author].add(title)


def find(author, title):
    """ Перевіряє, чи є книга у бібліотеці.
    :param author: Ім'я автора
    :param title: Назва книги
    :return: True, якщо книга є в бібліотеці, інакше False.
    """
    global library_db
    return library_db.search((author, title)) is not None


def delete(author, title):
    """ Видаляє книгу з каталогу.
    :param author: Ім'я автора
    :param title: Назва книги
    """
    global library_db, author_catalog
    book_key = (author, title)
    library_db.delete(book_key)

    if author in author_catalog:
        author_catalog[author].discard(title)
        if not author_catalog[author]:
            del author_catalog[author]


def findByAuthor(author):
    """ Повертає список книг певного автора у відсортованому порядку.
    :param author: Ім'я автора
    :return: Відсортований список назв книг автора.
    """
    global author_catalog
    return sorted(author_catalog.get(author, []))
