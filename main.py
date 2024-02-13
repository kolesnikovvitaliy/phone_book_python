import os
from classes.phonebook import Phonebook
from classes.phonebook_storage import PhonebookStorage
from services.crud import (
    add_contact,
    delete_entries,
    edit_entry,
    search_entries,
    view_entries,
)
from services.utils import header_interface


# Интерфейс командной строки для работы со справочником
def main():
    phonebook = Phonebook()
    storage = PhonebookStorage()

    filename = "./data/phonebook.pkl"

    # Загрузка существующего справочника из файла
    if os.path.exists(filename):
        storage.load_phonebook(phonebook=phonebook, filename=filename)

    while True:
        header_interface()
        choice = input("Введите номер операции: ")
        match choice:
            case "1":
                # Просмотр записей постранично
                view_entries(phonebook=phonebook)
            case "2":
                # Добавление записи
                add_contact(phonebook=phonebook)
                storage.save_phonebook(phonebook, filename)
            case "3":
                # Редактирование записи
                edit_entry(phonebook=phonebook)
                storage.save_phonebook(phonebook, filename)
            case "4":
                # Поиск записей по критериям
                search_entries(phonebook=phonebook)
            case "5":
                # Удаление записей
                delete_entries(phonebook=phonebook)
                storage.save_phonebook(phonebook, filename)
            case "6":
                # Сохранение изменений
                storage.save_phonebook(phonebook, filename)
                print("Изменения успешно сохранены")
            case "0":
                # Сохранение справочника и выход
                storage.save_phonebook(phonebook, filename)
                print("Справочник сохранен. До свидания!")
                break
            case _:
                print("Некорректный выбор, попробуйте еще раз.")


if __name__ == "__main__":
    main()
