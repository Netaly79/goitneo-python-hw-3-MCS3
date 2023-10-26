from datetime import datetime
from phone import Phone
from error import UnvalidPhoneNumber
from name import Name


class Record():
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = ''

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
            return True
        except UnvalidPhoneNumber:
            return False

    def edit_phone(self, old_phone, new_phone):
        try:
            self.remove_phone(old_phone)
            self.phones.append(Phone(new_phone))
            return self
        except TabError:
            print("Error deleting")
        except UnvalidPhoneNumber:
            return False

    def remove_phone(self, phone):
        phones = []
        for i in self.phones:
            if not i.value == phone:
                phones.append(i)
        self.phones = phones

    def find_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                return phone
        return "Not found"

    def add_birthday(self, date_string):
        try:
            date_format = '%d.%m.%Y'
            date_object = datetime.strptime(date_string, date_format)
            self.birthday = date_object
            print("Birthday added to contact")
            return self
        except ValueError:
            print("Birthday should be in format 'dd.MM.yyyy")
