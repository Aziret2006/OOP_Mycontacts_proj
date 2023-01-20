from MyContacs import MyContacts
from database import MY_CONTACTS


def name_validate(name: str) -> bool:
    if 20 >= len(name) >= 2 and name.isalpha():
        return True
    print("Incorrect name!")
    return False


def phone_number_validate(phone_number: str) -> bool:
    if 10 == len(phone_number) and phone_number.isdigit():
        return True
    print("Incorrect phone number!")
    return False


def client_exist(name: str) -> bool:
    return name in MY_CONTACTS.name
