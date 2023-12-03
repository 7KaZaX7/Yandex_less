class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def check_password(password):
    stop_list = ["qwertyuiop", "asdfghjkl", "zxcvbnm",
                 "йцукенгшщзхъ", "фывапролджэё", "ячсмитьбю"]
    if len(password) < 9:
        raise LengthError('LengthError')
    if not any(i.isdigit() for i in password):
        raise DigitError('DigitError')
    elif not any(i.islower() for i in password) or not any(i.isupper() for i in password):
        raise LetterError('LetterError')
    for i in range(len(password) - 2):
        for j in stop_list:
            if password[i:i + 3].lower() in j:
                raise SequenceError('SequenceError')
    return "ok"
