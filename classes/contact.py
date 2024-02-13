# Класс записи в справочнике
class Contact:
    """
    first_name: ValidStringItem,
    last_name: ValidStringItem,
    middle_name: ValidStringItem,
    organization: ValidOrgItem,
    work_phone: ValidPhoneItem,
    personal_phone: ValidPhoneItem,

    """
    count = 0

    def __init__(
        self,
        id: int | None = None,
        **kwargs,
    ):
        """
        Автоматическое присвоение аргументов переданных
        в функцию input_validate_data from module utils

        ###############################

        first_name: ValidStringItem,
        last_name: ValidStringItem,
        middle_name: ValidStringItem,
        organization: ValidOrgItem,
        work_phone: ValidPhoneItem,
        personal_phone: ValidPhoneItem,
        ...

        ################################

        """
        if not id:
            __class__.count += 1
            self.id = __class__.count
        else:
            self.id = id
        [
            setattr(self, key, value)
            for key, value in kwargs.items()
        ]
