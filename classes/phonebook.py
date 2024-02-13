from services.utils import search_utils, show_data


# Класс справочника, содержит все методы для работы со справочником
class Phonebook:
    def __init__(self):
        self.entries = []

    # Вывод записей постранично
    def show_entries(self, page_size=5, page_number=1):
        start_index = (page_number - 1) * page_size
        end_index = start_index + page_size
        for entry in self.entries[start_index:end_index]:
            show_data(entry)

    # Добавление записи
    def add_entry(self, contact):
        self.entries.append(contact)

    # Редактирование записи
    def edit_entry(self, index, contact):
        self.entries[index] = contact

    # Удаление записи
    def delete_entry(self, entry):
        self.entries.remove(entry)

    # Поиск записей по характеристикам
    def search_entries(self, search_criteria: list | None):
        search_results = search_utils(self, search_criteria)
        return list(sorted(search_results, key=lambda x: x.id))