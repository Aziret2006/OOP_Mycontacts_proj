from view import create_contact
from MyContacs import MyContacts


def main():
    while True:
        client_action = input("""
                       Press 1 to create contact
                       Press 2 to get contact
                       Press 3 to edit contact
                       Press 4 to delete contact
                       Press 5 to show all my contacts
                       Press 6 to exit
                               """)
        if client_action == '1':
            pass
        elif client_action == '2':
            pass
        elif client_action == '3':
            pass
        elif client_action == '4':
            pass
        elif client_action == '5':
            MyContacts.show_all_contact()
        elif client_action == '6':
            print("I miss you already")
            break


if __name__ == '__main__':
    main()
