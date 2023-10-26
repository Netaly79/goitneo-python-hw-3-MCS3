from datetime import datetime

from error import UnknownUserName, input_error
from record import Record
from address_book import AddressBook


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def change_contact(args, contacts):
    if len(args) < 3:
        raise IndexError
    name, old_phone, new_phone = args
    contact = contacts.find(name)
    res = contact.edit_phone(old_phone, new_phone)
    if res:
        contacts.change_record(contact)
    else:
        contact.phones = old_phone
        contacts.change_record(contact)


@input_error
def show_phone(args, contacts):
    name = args[0]
    phones = contacts.find(name).phones
    arr = []
    for phone in phones:
        arr.append(phone.value)
    print(name, ': ', arr)


@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise IndexError
    name, phone = args
    contact_names = contacts.data.keys()
    if name in contact_names:
        answer = input(
            "This contact already exists. Do you want to rewrite this contact? Press 1 if yes, 0 if no\n")
        if answer == '0':
            return "Contact hasn't been modified"
    new_record = Record(name)
    res = new_record.add_phone(phone)
    if res:
        contacts.add_record(new_record)
        return "Contact " + name + "added."


def show_all(contacts):
    for name, record in contacts.data.items():
        for phone in record.phones:
            print(name, phone)


def add_birthday(args, contacts):
    if len(args) < 2:
        raise IndexError
    name, bd_string = args
    contact = contacts.find(name)
    contact = contact.add_birthday(bd_string)
    contacts.change_record(contact)


def show_birthday(args, contacts):
    if len(args) < 1:
        raise IndexError
    name = args[0]
    contact = contacts.find(name)
    if contact is not None:
        print("Contact " + name + " has bithday " +
              contact.birthday.strftime('%d.%m.%Y'))
    else:
        print("Contact " + name + " not found")


def closest_birthdays(contacts):
    week_days = ["Monday", "Tuesday", "Wednesday",
                 "Thursday", "Friday", "Saturday", "Sunday"]
    current_date = datetime.today().date()
    day_today = datetime.today().weekday()
    birthdays = {'Monday': [], 'Tuesday': [], 'Wednesday': [],
                 'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}
    day_today = datetime.today().weekday()
    for user in contacts.data.items():
        name = user[0]
        birthday = user[1].birthday.date()
        birthday_this_year = birthday.replace(year=datetime.today().year)

        if birthday_this_year < current_date:
            birthday_this_year = birthday.replace(
                year=datetime.today().year + 1)

        delta_days = (birthday_this_year - datetime.today().date()).days
        if delta_days < 7:
            day_number = (day_today + delta_days) % 7
            if day_number > 0 and day_number < 5:
                birthdays[week_days[day_number]].append(name)
            else:
                birthdays[week_days[0]].append(name)

    i = day_today
    while i < 5:
        arr = birthdays[week_days[i]]
        if arr:
            print(f"{week_days[i]}: {', '.join(arr)}")
        i += 1

    i = 0
    while i < day_today:
        arr = birthdays[week_days[i]]
        if arr:
            print(f"{week_days[i]}: {', '.join(arr)}")
        i += 1


@input_error
def main():
    contacts = AddressBook()
    print("\nWelcome to the assistant bot!\n")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            print("{:*^10}".format(''))
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            add_contact(args, contacts)
            print("{:*^10}".format(''))
        elif command == "add_bday":
            add_birthday(args, contacts)
            print("{:*^10}".format(''))
        elif command == "show_bday":
            show_birthday(args, contacts)
            print("{:*^10}".format(''))
        elif command == "change":
            try:
                change_contact(args, contacts)
                print("{:*^10}".format(''))
            except UnknownUserName:
                print("This user is not present in the Address Book")
                print("{:*^10}".format(''))
        elif command == "phone":
            show_phone(args, contacts)
            print("{:*^10}".format(''))
        elif command == "all":
            show_all(contacts)
            print("{:*^10}".format(''))
        elif command == "birthdays":
            closest_birthdays(contacts)
            print("{:*^10}".format(''))
        else:
            print("Invalid command.")
            print("{:*^10}".format(''))


if __name__ == "__main__":
    main()
