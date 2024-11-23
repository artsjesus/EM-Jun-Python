from src.library import Library
from src.utils import add_new_book, delete_book, find_books, show_all_books, update_book_status


def main() -> None:
    library = Library("books.json")
    while True:
        answer = int(input("Выберите команду по номеру:\n"
                           "1: Добавить книгу\n"
                           "2: Удалить книгу\n"
                           "3: Найти книгу\n"
                           "4: Показать все книги\n"
                           "5: Изменить статус книги\n"
                           "6: Выйти\n"
                           "Команда: "))
        if answer == 1:
            add_new_book(library)
        if answer == 2:
            delete_book(library)
        if answer == 3:
            find_books(library)
        if answer == 4:
            show_all_books(library)
        if answer == 5:
            update_book_status(library)
        if answer == 6:
            print("Хорошего дня")
            exit()


if __name__ == '__main__':
    main()
