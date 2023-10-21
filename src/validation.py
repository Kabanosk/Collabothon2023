import re


def valid_email(email: str):
    pattern = "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    if re.match(pattern, email):
        return True
    return False


def valid_password(password: str):
    pattern = "(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$"
    if re.match(pattern, password):
        return True
    return False
