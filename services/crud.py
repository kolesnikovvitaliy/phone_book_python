from classes.contact import Contact
from classes.phonebook import Phonebook
from services.utils import (
    format_table,
    input_validate_data,
    search_interface,
    show_data,
)


def add_contact(phonebook: Phonebook) -> None:
    """
    Создание записи
    """
    data = input_validate_data()
    if phonebook.entries:
        id = phonebook.entries[-1].id + 1
        contact = Contact(id=id, **data)
    else:
        contact = Contact(**data)
    phonebook.add_entry(contact)
    print("Запись успешно добавлена в справочник")


def edit_entry(phonebook: Phonebook) -> None:
    """
    Редактирование записи
    """
    item = int(input("Введите ID записи для редактирования: "))
    if phonebook.entries:
        for index, entry in enumerate(phonebook.entries):
            if entry.id == item:
                data = input_validate_data()
                contact = Contact(id=entry.id, **data)
                phonebook.edit_entry(index=index, contact=contact)
                print("Запись успешно обновлена")
                break
        else:
            print("Некорректный ID записи")
    else:
        print("Список Пуст")


def view_entries(phonebook: Phonebook) -> None:
    """
    Постраничное отображение данных
    """
    page_size = 5
    page_number = 1
    while True:
        format_table()
        phonebook.show_entries(page_size, page_number)
        print("1. Следующая страница")
        print("2. Предыдущая страница")
        print("0. Возврат в главное меню")
        sub_choice = input("Введите номер операции: ")
        if sub_choice == "1":
            page_number += 1
        elif sub_choice == "2":
            if page_number > 1:
                page_number -= 1
        elif sub_choice == "0":
            break


def search_entries(phonebook: Phonebook) -> None:
    """
    Поиск записей
    """
    search_criteria = search_interface()
    search_results = phonebook.search_entries(search_criteria)
    if len(search_results) > 0:
        print("Результаты поиска:")
        format_table()
        for entry in search_results:
            show_data(entry=entry)
    else:
        print("Записи не найдены")


def delete_entries(phonebook: Phonebook) -> None:
    """
    Удаление записей
    """
    index = int(input("Введите ID записи для удаления: "))
    if phonebook.entries:
        for entry in phonebook.entries:
            if entry.id == index:
                phonebook.delete_entry(entry)
                print("Запись успешно удаленна")
                break
        else:
            print("Нет записи с таим ID")
    else:
        print("Список Пуст")
