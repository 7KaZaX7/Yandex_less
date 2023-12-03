number = input("")
number = "".join(number.split())
digits = number[0]
if number[0] == '8':
    digits = '+7'
    number = number[1:]
for i in number:
    if i.isdigit():
        digits += i
check = 0
sc = 0
try:
    if digits[0] != "+":
        raise AttributeError("неверный формат")
    if number[0] != "-" and number[-1] != "-":
        if number.count("(") == number.count(")"):
            for i in number:
                if i == "-":
                    check += 1
                else:
                    check = 0
                if check == 2:
                    raise AttributeError("неверный формат")
            for i in number:
                if i == "(" and sc != -1:
                    sc += 1
                elif i == ")":
                    sc -= 1
                if sc == 2 or sc == -2 or sc < 0:
                    raise AttributeError("неверный формат")
            for i in number:
                if not i.isdigit() and (
                    i != "+" and i != "(" and i != ")" and i != "-"
                ):
                    raise AttributeError("неверный формат")
            if len(digits) != 12:
                raise AttributeError("неверное количество цифр")
            if '+7' not in digits and '+1' not in digits and '+359' not in digits and '+55' not in digits:
                raise AttributeError('не определяется код страны')
            if '+7' in digits:
                digits = digits[2:]
                if (
                    digits.startswith("910")
                    or digits.startswith("911")
                    or digits.startswith("912")
                    or digits.startswith("913")
                    or digits.startswith("914")
                    or digits.startswith("915")
                    or digits.startswith("916")
                    or digits.startswith("917")
                    or digits.startswith("918")
                    or digits.startswith("919")
                    or digits.startswith("980")
                    or digits.startswith("981")
                    or digits.startswith("982")
                    or digits.startswith("983")
                    or digits.startswith("984")
                    or digits.startswith("985")
                    or digits.startswith("986")
                    or digits.startswith("987")
                    or digits.startswith("988")
                    or digits.startswith("989")
                ):
                    pass
                elif (
                    digits.startswith("920")
                    or digits.startswith("921")
                    or digits.startswith("922")
                    or digits.startswith("923")
                    or digits.startswith("924")
                    or digits.startswith("925")
                    or digits.startswith("926")
                    or digits.startswith("927")
                    or digits.startswith("928")
                    or digits.startswith("929")
                    or digits.startswith("930")
                    or digits.startswith("931")
                    or digits.startswith("932")
                    or digits.startswith("933")
                    or digits.startswith("934")
                    or digits.startswith("935")
                    or digits.startswith("936")
                    or digits.startswith("937")
                    or digits.startswith("938")
                    or digits.startswith("939")
                ):
                    pass
                elif (
                    digits.startswith("902")
                    or digits.startswith("903")
                    or digits.startswith("904")
                    or digits.startswith("905")
                    or digits.startswith("906")
                    or digits.startswith("960")
                    or digits.startswith("961")
                    or digits.startswith("962")
                    or digits.startswith("963")
                    or digits.startswith("964")
                    or digits.startswith("965")
                    or digits.startswith("966")
                    or digits.startswith("967")
                    or digits.startswith("968")
                    or digits.startswith("969")
                ):
                    pass
                else:
                    raise AttributeError("не определяется оператор сотовой связи")
                digits = '+7' + digits
            print(digits)
        else:
            raise AttributeError("неверный формат")
    else:
        raise AttributeError("неверный формат")

except Exception as ex:
    print(ex)