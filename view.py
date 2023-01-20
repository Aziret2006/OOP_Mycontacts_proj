from MyContacs import MyContacts
from validation import name_validate, phone_number_validate, client_exist
from database import MY_CONTACTS


def create_contact():
    name = input("Enter contact name: ").strip()
    phone_number = input("Enter phone number(0558705070): ").strip()
    validate = (name_validate(name=name) and phone_number_validate(phone_number=phone_number))
    if all(validate):
        is_client_exist = client_exist(name=name)
        if is_client_exist:
            MyContacts(
                name=name
            )
            MY_CONTACTS.append(MyContacts)
            print("")
            return



def get_contact():
    for name in MY_CONTACTS:
        pass


def update_contact():
    pass


def delete_contact():
    pass


def show_all_contcats():
    print(MyContacts)
