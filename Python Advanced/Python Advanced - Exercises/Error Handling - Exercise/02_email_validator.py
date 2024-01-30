class MustContainAtSymbolError(Exception):
    pass


class MoreThanOneAtSymbol(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class NameTooLongError(Exception):
    pass


VALID_DOMAINS = ("com", "bg", "org", "net")

email = input()
while email != "End":
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @ symbol")
    elif email.count('@') > 1:
        raise MoreThanOneAtSymbol("Email must contain only one @ symbol")
    elif email.split('.')[-1] not in VALID_DOMAINS:
        raise InvalidDomainError("Invalid Domain. Allowed Domains are: .com, .bg, .org, .net")
    elif len(email.split('@')[0]) < 5:
        raise NameTooShortError("Name must be at least 5 characters")
    elif len(email.split('@')[0]) > 10:
        raise NameTooLongError("Name cannot be more than 10 characters")

    print("Email is valid")

    email = input()
