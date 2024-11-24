from src.library import Library
from src.utils import add_new_book, delete_book, find_books, show_all_books, update_book_status


def main() -> None:
    library = Library("books.json")
    menu_options = {
        1: ("Добавить книгу", add_new_book),
        2: ("Удалить книгу", delete_book),
        3: ("Найти книгу", find_books),
        4: ("Показать все книги", show_all_books),
        5: ("Изменить статус книги", update_book_status),
        6: ("Выйти", None)
    }

    while True:
        print("Выберите команду по номеру: ")
        for key, (description, _) in menu_options.items():
            print(f"{key}: {description}")

        try:
            answer = int(input("Команда: "))
            if answer not in menu_options:
                raise ValueError("Не верный номер команды")

            if answer == 6:
                print("Хорошего дня!")
                break

            selected_function = menu_options[answer][1]
            selected_function(library)

        except ValueError:
            print(f"Ошибка: Пожалуйста введите команду числом\n")


if __name__ == '__main__':
    main()
