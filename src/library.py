import json
from typing import List


class Book:
    def __init__(self, book_id: int, title: str, author: str, year: int, status: bool):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return (f"Номер книги: {self.book_id}\nНазвание: {self.title}\n"
                f"Автор: {self.author}\nГод издания: {self.year}\nНаличие книги: {self.status}\n")


class Library:
    def __init__(self, file_name):
        self.file_name = file_name
        self.book: List[Book] = self.load_book()

    def load_book(self) -> List[Book]:
        with open(f"data/{self.file_name}", 'r', encoding='utf-8') as file:
            return [Book(**book) for book in json.load(file)]

    def save_book(self):
        with open(f"data/{self.file_name}", "w", encoding="utf-8") as f:
            json.dump([book.__dict__ for book in self.book], f, ensure_ascii=False, indent=4)

    def add_book(self, title, author, year):
        book_id = max((book.book_id for book in self.book), default=0) + 1
        self.book.append(Book(book_id=book_id, title=title, author=author, year=year, status=True))
        self.save_book()
        print(f"Книга добавлена присвоен номер {book_id}")

    def remove_book(self, book_id: int):
        book_to_delete = next((book for book in self.book if book.book_id == book_id), None)
        if book_to_delete:
            self.book.remove(book_to_delete)
            self.save_book()
            print(f"Книга с номером {book_id} удалена \n")
        else:
            print(f"Книга с номером {book_id} не найдена\n")

    def show_all_book(self) -> List[Book]:
        return self.book

    def search_books(self, **kwargs):
        found_books = self.book
        for key, value in kwargs.items():
            if isinstance(value, str):
                found_books = [book for book in found_books if value.lower() in getattr(book, key, "").lower()]
            else:
                found_books = [book for book in found_books if getattr(book, key) == value]

        return found_books

    def update_status_book(self, book_id: int, new_status: bool):
        current_book = next((book for book in self.book if book.book_id == book_id), None)
        try:
            current_book.status = new_status
            self.save_book()
            if new_status is True:
                status_text = "В наличии"
            else:
                status_text = "Выдана"

            print(f"У книги с номером {book_id} изменился статус на {status_text}\n")
        except ValueError:
            print(f"Книга с номером {book_id} не найдена\n")
