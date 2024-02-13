import pickle
import os


class PhonebookStorage:
    """
    Class for loading 
    and saving data to a file
    """

    # Сохранение справочника в файл
    @staticmethod
    def save_phonebook(phonebook, filename):
        with open(filename, "wb") as file:
            pickle.dump(phonebook.entries, file)

    # Загрузка справочника из файла
    @staticmethod
    def load_phonebook(phonebook, filename):
        if os.path.exists(filename):
            with open(filename, "rb") as file:
                phonebook.entries = pickle.load(file)
        else:
            raise FileNotFoundError
