from typing import List


class EmailValidator:
    def __init__(self, min_length: int, mails: List[str], domains: List[str]):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str) -> bool:
        if len(name) >= self.min_length:
            return True

        return False

    def __is_mail_valid(self, mail: str) -> bool:
        if mail in self.mails:
            return True

        return False

    def __is_domain_valid(self, domain) -> bool:
        if domain in self.domains:
            return True

        return False

    def validate(self, email) -> bool:
        data = email.split("@")
        mail, domain = data[1].split(".")

        if len(data[0]) >= self.min_length and mail in self.mails and domain in self.domains:
            return True

        return False
