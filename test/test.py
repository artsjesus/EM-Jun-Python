import json
import unittest
import os

from src.library import Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        """
        Создает тестовую библиотеку и добавляет несколько книг для тестирования
        """
        initial_books = [
            {"book_id": 1, "title": "Book 1", "author": "Author 1", "year": 2021, "status": True},
            {"book_id": 2, "title": "Book 2", "author": "Author 2", "year": 2022, "status": True},
            {"book_id": 3, "title": "Book 3", "author": "Author 3", "year": 2023, "status": True}
        ]
        with open("data/test_books.json", "w") as f:
            json.dump(initial_books, f)
        self.library = Library("test_books.json")

    def tearDown(self):
        """
        Удаляет файл библиотеки тестов после каждого теста
        """
        if os.path.exists("test_books.json"):
            os.remove("test_books.json")

    def test_add_book(self):
        """
        Тест добавления новой книги в библиотеку
        """
        self.library.add_book("Book 4", "Author 4", 2024)
        books = self.library.search_books(title="Book 4")
        self.assertEqual(len(books), 1)
        book = books[0]
        self.assertEqual(book.title, "Book 4")
        self.assertEqual(book.author, "Author 4")
        self.assertEqual(book.year, 2024)
        self.assertEqual(book.status, True)

    def test_delete_book(self):
        """
        Тест удаление книги из библиотеки
        """
        books = self.library.search_books(title="Book 1")
        self.assertEqual(len(books), 1)
        book = books[0]
        self.library.remove_book(book.book_id)
        books = self.library.search_books(title="Book 1")
        self.assertEqual(len(books), 0)

    def test_find_books(self):
        """
        Тест поиска книг в библиотеке по заданному атрибуту
        """
        books = self.library.search_books(author="Author 2")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "Book 2")

    def test_get_all_books(self):
        """
        Тест получение всех книг из библиотеки
        """
        books = self.library.show_all_book()
        self.assertEqual(len(books), 3)

    def test_change_status(self):
        """
        Тест изменения статуса книги
        """
        books = self.library.search_books(title="Book 3")
        self.assertEqual(len(books), 1)
        book = books[0]
        self.library.update_status_book(book.book_id, False)
        update_books = self.library.search_books(title="Book 3")
        self.assertEqual(len(update_books), 1)
        update_book = update_books[0]
        self.assertEqual(update_book.status, False)


if __name__ == "__main__":
    unittest.main()
