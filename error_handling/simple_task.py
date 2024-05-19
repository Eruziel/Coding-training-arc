class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


VALID_DOMAINS = ('com', 'bg', 'net', 'org')
while True:
    command = input()
    if command == 'End':
        break

    if '@' not in command:
        raise MustContainAtSymbolError('Email must contain @')

    email = command.split('@')

    if len(email[0]) < 4:
        raise NameTooShortError('Name must be more than 4 characters')

    domain = email[1].split('.')

    if domain[1] not in VALID_DOMAINS:
        raise InvalidDomainError(f'Domain must be one of the following: {", ".join("." + x for x in VALID_DOMAINS)}')

    print('Email is valid')






