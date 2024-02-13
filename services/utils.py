from services.validates import _is_valid
from classes.contact import Contact
from typing import Any, List, Literal
from colorama import Fore, Style
from services import constants


def header_interface() -> None:
    """
    Main interface display
    """
    print("=== ТЕЛЕФОННЫЙ СПРАВОЧНИК ===")
    print("1. Просмотр записей")
    print("2. Добавить запись")
    print("3. Редактировать запись")
    print("4. Поиск записей")
    print("5. Удалить запись")
    print("6. Сохранить изменения")
    print("0. Сохранение и Выход")


def input_validate_data() -> dict[str, Any]:
    """
    Entering and checking data for validity

    first_name: ValidStringItem,
    last_name: ValidStringItem,
    middle_name: ValidStringItem,
    organization: ValidOrgItem,
    work_phone: ValidPhoneItem,
    personal_phone: ValidPhoneItem,

    """
    first_name: str = _is_valid(item="Введите имя: ")
    last_name: str = _is_valid(item="Введите фамилию: ")
    middle_name: str = _is_valid(item="Введите отчество: ")
    organization: str = _is_valid(
        item="Введите название организации: ", org=True
    )
    work_phone: str = _is_valid(item="Введите рабочий телефон: ", phone=True)
    personal_phone: str = _is_valid(
        item="Введите личный телефон: ", phone=True
    )
    return locals()


def show_data(entry: Contact) -> None:
    """
    Displaying the table
    """
    print(
        "     ",
        "|",
        Fore.GREEN + str(entry.id).center(constants.len_id),
        Style.RESET_ALL,
        "|",
        str(entry.first_name).center(constants.len_first_name),
        "|",
        str(entry.last_name).center(constants.len_last_name),
        "|",
        str(entry.middle_name).center(constants.len_middle_name),
        "|",
        str(entry.organization).center(constants.len_organization),
        "|",
        str(entry.work_phone).center(constants.len_work_phone),
        "|",
        str(entry.personal_phone).center(constants.len_personal_phone),
        "|",
        sep="",
    )
    decor_line()


def format_table() -> None:
    """
    Displaying the table header
    """
    decor_line(head=True)
    print(
        "     ",
        "|",
        Fore.RED + "ID".center(constants.len_id),
        Style.RESET_ALL,
        "|",
        Fore.RED + "FIRST NAME".center(constants.len_first_name),
        Style.RESET_ALL,
        "|",
        Fore.RED + "LAST NAME".center(constants.len_last_name),
        Style.RESET_ALL,
        "|",
        Fore.RED + "MIDDLE NAME".center(constants.len_middle_name),
        Style.RESET_ALL,
        "|",
        Fore.RED + "ORGANIZATION".center(constants.len_organization),
        Style.RESET_ALL,
        "|",
        Fore.RED + "WORK PHONE".center(constants.len_work_phone),
        Style.RESET_ALL,
        "|",
        Fore.RED + "PERSONAL PHONE".center(constants.len_personal_phone),
        Style.RESET_ALL,
        "|",
        sep="",
    )
    decor_line(head=True)


def decor_line(head=False) -> None:
    """
    Displaying the table header
    """
    delimiter: Literal["-"] = "-"

    if head:
        delimiter: Literal["="] = "="

    print(
        "     ",
        "+",
        delimiter * constants.len_id,
        "+",
        delimiter * constants.len_first_name,
        "+",
        delimiter * constants.len_last_name,
        "+",
        delimiter * constants.len_middle_name,
        "+",
        delimiter * constants.len_organization,
        "+",
        delimiter * constants.len_work_phone,
        "+",
        delimiter * constants.len_personal_phone,
        "+",
        sep="",
    )


def search_interface() -> List[str]:
    """
    Search records interface
    """
    search_criteria = input(
        """Вводите значения любых критериев для поиска через пробел :
id(ID)
first_name(Имя)
last_name(Фамилия)
middle_name(Отчество)
work_phone(Рабочий телефон)
personal_phone(Личный мобильный телефон)
: """
    )
    return search_criteria.split(" ")


def search_utils(self, search_criteria) -> List[Contact]:
    """
    Search records
    """
    search_results = []
    while search_criteria:
        item = search_criteria.pop()
        print(item)
        if item.isdigit():
            item = int(item)
        for entry in self.entries:
            if any(v == item for v in entry.__dict__.values()):
                search_results.append(entry)

    return search_results
