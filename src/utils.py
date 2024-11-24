from src.library import Library


def add_new_book(library: Library) -> None:
    """
    Добавление книги в библиотеку
    """
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    while True:
        try:
            year = int(input("Введите год издания книги: "))
            library.add_book(title=title, author=author, year=year)
            print(f"Книга добавлена\n")
            break
        except ValueError:
            print("Неправильный год. Введите год числом\n")


def delete_book(library: Library) -> None:
    """
    Удаление книги из библиотеки
    """
    book_id = int(input("Введите номер книги которую нужно удалить: "))
    try:
        library.remove_book(book_id=book_id)
        print(f"Книга с номером {book_id} удалена \n")
    except AttributeError:
        print(f"Книга с номером {book_id} не найдена\n")


def find_books(library: Library) -> None:
    """
    Поиск книги
    """
    valid_fields = {"title", "author", "year"}  # Допустимые поля для поиска
    field = input("Поиск по (title/author/year): ").lower()

    if field not in valid_fields:
        print(f"Недопустимое поле {field}. Пожалуйста, выберите из {', '.join(valid_fields)}.\n")
    while True:
        value = input(f"Введите {field}: ")
        if field == "year":
            try:
                value = int(value)
                break
            except ValueError:
                print("Год должен быть числом. Пожалуйста, попробуйте еще раз.\n")

    found_books = library.search_books(**{field: value})
    if found_books:
        for book in found_books:
            print(book)
    else:
        print("Нет книги с такими параметрами\n")


def show_all_books(library: Library) -> None:
    """
    Показать всё книги в наличии
    """
    books = library.show_all_book()
    if books:
        for book in books:
            print(book)
    else:
        print("Нет книг в библиотеке\n")


def update_book_status(library: Library) -> None:
    """
    Изменение статуса книги
    """
    book_id = int(input("Введите номер книги, статус которой хотите изменить: "))
    print('1: Книга в наличии\n'
          '2: Книга выдана')
    user_status = int(input("Выберите статус (1/2): "))
    try:
        if user_status == 1:
            library.update_status_book(book_id=book_id, new_status=True)
            print(f"У книги с номером {book_id} изменился статус на {user_status}\n")
        elif user_status == 2:
            library.update_status_book(book_id=book_id, new_status=False)
            print(f"У книги с номером {book_id} изменился статус на {user_status}\n")
        else:
            print("Неверный выбор. Пожалуйста, введите 1 или 2.\n")
    except AttributeError:
        print(f"Книга с номером {book_id} не найдена\n")
