from collections import UserDict
from error import UnknownUserName
from record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        name = record.name.value
        is_valid_phone = self[name] = record
        if is_valid_phone:
            print("Contact " + name + " added")

    def find(self, name):
        try:
            data = self[name]
            record = Record(name)
            record.phones = data.phones
            record.birthday = data.birthday
            return record
        except KeyError:
            raise UnknownUserName(name)

    def delete(self, name):
        records = []
        for i in self.data.keys():
            if not i == name:
                records.append({i: self.data[i]})
        self.data = records
        return self

    def change_record(self, record: Record):
        self.data[record.name.value] = record
        print("contact for " + record.name.value + " changed")
