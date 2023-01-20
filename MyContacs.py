
class MyContacts:
    def __init__(self, name: str):
        self.__contact_name = name
        self.__phone_number = []


    @property
    def contact_name(self):
        return self.__contact_name


    def show_all_contact(self):
        print(f"""
        Contact name: {self.__contact_name}
        Phone: {self.__phone_number}   
        """)

    def get_contact(self):
        print(f"Your contact name -> {self.__contact_name}"
              f"Your phone number -> {self.__phone_number}")


