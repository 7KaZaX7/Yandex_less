def check_password(password):
    stop_list = [
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm",
        "йцукенгшщзхъ",
        "фывапролджэё",
        "ячсмитьбю",
    ]
    try:
        assert len(password) > 8, "error"
        assert any(i.isdigit() for i in password), "error"
        assert any(i.islower() for i in password) and any(
            i.isupper() for i in password
        ), "error"
        for i in range(len(password) - 2):
            for j in stop_list:
                assert password[i:i + 3].lower() not in j, "error"
        return "ok"
    except Exception as err:
        return err


print(check_password(input()))