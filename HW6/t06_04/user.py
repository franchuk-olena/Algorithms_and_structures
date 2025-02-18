"""
Каталог бібліотеки художніх книг.
Бібліотека може містити кілька книг одного автора.
"""

LIBRARY_CAPACITY = 10007  # Оптимальний розмір хеш-таблиці для зменшення колізій


class HashTable:
    """ Реалізація хеш-таблиці з методом ланцюжків для розв'язання колізій. """

    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]  # Масив списків (ланцюжків)

    def _hash(self, key):
        """ Хеш-функція для отримання індексу комірки. """
        return hash(key) % self.capacity

    def insert(self, key, value):
        """ Додає книгу в хеш-таблицю. """
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Оновлення значення
                return
        bucket.append((key, value))  # Додаємо новий елемент

    def search(self, key):
        """ Повертає значення книги або None, якщо книга не знайдена. """
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        """ Видаляє книгу з бібліотеки. """
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return


library_db = None  # Основна хеш-таблиця для книг
author_catalog = None  # Словник для зберігання списків книг за авторами


def init():
    """ Ініціалізує бібліотечну базу даних. """
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


