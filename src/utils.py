from src.library import Library


def add_new_book(library: Library) -> None:
    """
    Добавление книги в библиотеку
    """
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    try:
        year = int(input("Введите год издания книги: "))
        library.add_book(title=title, author=author, year=year)
    except ValueError:
        print("Неправильный год. Введите год в числом\n")


def delete_book(library: Library) -> None:
    """
    Удаление книги из библиотеки
    """
    try:
        book_id = int(input("Введите номер книги которую нужно удалить: "))
        library.remove_book(book_id=book_id)
    except ValueError:
        print("Не верный номер книги!\n")


def find_books(library: Library) -> None:
    """
    Поиск книги
    """
    valid_fields = {"title", "author", "year"}  # Допустимые поля для поиска
    field = input("Поиск по (title/author/year): ").lower()

    if field not in valid_fields:
        print(f"Недопустимое поле {field}. Пожалуйста, выберите из {', '.join(valid_fields)}.\n")
        return

    value = input(f"Введите {field}: ")
    if field == "year":
        try:
            value = int(value)
        except ValueError:
            print("Год должен быть числом. Пожалуйста, попробуйте еще раз.\n")
            return

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
            print(f"Номер книги: {book.book_id}\nНазвание: {book.title}\n"
                  f"Автор: {book.author}\nГод издания: {book.year}\nНаличие книги: {book.status}\n")
    else:
        print("Нет книг в библиотеке\n")


def update_book_status(library: Library) -> None:
    """
    Изменение статуса книги
    """
    try:
        book_id = int(input("Введите номер книги, статус которой хотите изменить: "))
        print('1: Книга в наличии\n'
              '2: Книга выдана')
        user_status = int(input("Выберите статус (1/2): "))
        if user_status == 1:
            book_status = True
        elif user_status == 2:
            book_status = False
        else:
            print("Неверный выбор. Пожалуйста, введите 1 или 2.\n")
            return
        library.update_status_book(book_id=book_id, new_status=book_status)
    except ValueError:
        print("Неверный ввод. Введите числовые значения идентификатора и статуса.\n")
