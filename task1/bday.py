from .field import Field

class Birthday(Field):
    def __init__(self, date):
        self.value = date

    def __str__(self):
        return str(self.value)