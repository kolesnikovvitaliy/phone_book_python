import re
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    validator,
)
from typing import Annotated
from annotated_types import MaxLen, MinLen


STRONG_PHONE_PATTERN = re.compile(
    r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$"
)
LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")
LETTER_ORG_MATCH_PATTERN = re.compile(r"^[\W а-яА-Яa-zA-Z\-0-9]+$")


class CustomModel(BaseModel):
    """
    Main class of model settings
    for data validation
    """
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
    )


class ValidStringItem(CustomModel):
    """
    Name validation model
    """
    item: Annotated[str, MinLen(1), MaxLen(25)]

    @validator("item")
    @classmethod
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise ValueError("Строка должна содержать только буквы")
        return value

    def __str__(self):
        return self.item

    def __repr__(self):
        return str(self.item)


class ValidPhoneItem(CustomModel):
    """
    Phone validation model
    """
    phone: str = Field(min_length=9, max_length=25)

    @field_validator("phone", mode="after")
    @classmethod
    def valid_phone(cls, phone: str) -> str:
        if not re.match(STRONG_PHONE_PATTERN, phone):
            raise ValueError("Phone Number Invalid." "EXAMPLE: +74950000000")

        return phone

    def __str__(self):
        return self.phone

    def __repr__(self):
        return str(self.phone)


class ValidOrgItem(CustomModel):
    """
    Organization validation model
    """
    item: Annotated[str, MinLen(1), MaxLen(255)]

    @validator("item")
    @classmethod
    def validate_name(cls, value):
        if not LETTER_ORG_MATCH_PATTERN.match(value):
            raise ValueError("Стока должна содержать только буквы")
        return value

    def __str__(self):
        return self.item

    def __repr__(self):
        return str(self.item)


def _is_valid(item, phone=False, org=False):
    """
    Checking the validity of all data types
    """
    while True:
        try:
            if phone:
                model = ValidPhoneItem(phone=input(item))
            elif org:
                model = ValidOrgItem(item=input(item))
            else:
                model = ValidStringItem(item=input(item))

            if model:
                return str(model)
        except ValueError as e:
            print(e)
