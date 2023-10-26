from field import Field
from error import UnvalidPhoneNumber


class Phone(Field):
    def __init__(self, phone):
        if phone.isdigit() and len(phone) == 10:
            self.value = phone
        else:
            raise UnvalidPhoneNumber(phone)

    def __str__(self):
        return self.value
