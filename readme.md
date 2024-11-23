Использование

Основные классы и методы

Класс Book
Представляет книгу с атрибутами, такими как ID книги, название, автор, год издания и статус.

Атрибуты
book_id (int): Уникальный идентификатор книги.
title (str): Название книги.
author (str): Автор книги.
year (int): Год издания книги.
status (bool): Статус книги (True - "в наличии", False - "выдана"). По умолчанию True.

Класс Library
Управляет коллекцией экземпляров класса Book, включая загрузку и сохранение данных в JSON файл.

Методы
__init__(self, library_file='books.json'): Инициализирует новый экземпляр библиотеки с указанием файла JSON для хранения данных.
load_books(self): Загружает книги из файла JSON.
save_books(self): Сохраняет текущий список книг в файл JSON.
add_book(self, title, author, year): Добавляет новую книгу в библиотеку.
remove_book(self, book_id): Удаляет книгу из библиотеки по ее ID.
show_all_book(self): Возвращает все книги в библиотеке.
search_books(self, **kwargs): Находит книги, соответствующие заданным критериям.
update_status_book(self, book_id, new_status): Изменяет статус книги.

Запуск проекта

Для запуска основной программы выполните:

python main.py