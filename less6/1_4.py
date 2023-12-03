def check_password(password):
    stop_list = ["qwertyuiop", "asdfghjkl", "zxcvbnm",
                 "йцукенгшщзхъ", "фывапролджэё", "ячсмитьбю"]
    try:
        if len(password) < 9:
            raise AttributeError
        if (not any(i.isdigit() for i in password) or
                not any(i.islower() for i in password) or
                not any(i.isupper() for i in password)):
            raise AttributeError
        for i in range(len(password) - 2):
            for j in stop_list:
                if password[i:i + 3].lower() in j:
                    raise AttributeError
        return f"ok"
    except AttributeError:
        return f"error"


passw = input()
print(check_password(passw))