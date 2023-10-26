def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me a name and phone, please."
        except KeyError:
            return "Unknown name"
        except IndexError:
            return "Incorrect number of arguments"
    return inner


class UnknownUserName(Exception):
    def __init__(self, username):
        self.message = f"Unknown username: {username}"
        super().__init__(self.message)
        print(self.message)


class UnvalidPhoneNumber(Exception):
    def __init__(self, phone):
        self.message = f"Incorrect phone number: {phone}. Please add number in format 'ten digits'"
        super().__init__(self.message)
        print(self.message)
