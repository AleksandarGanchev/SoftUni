class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, value: str):
        if 5 <= len(value) <= 15:
            self.__username = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value):
        min_length = 8
        contain_uppercase = len([letter for letter in value if letter.isupper()]) > 0
        contain_digit = len([x for x in value if x.isdigit()]) > 0

        if len(value) >= min_length and contain_uppercase and contain_digit:
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'
