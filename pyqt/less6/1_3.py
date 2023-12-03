number = input('')
number = ''.join(number.split())
answer = number[0]
if number[0] == '8':
    answer = '+7'
    number = number[1:]

for i in number:
    if i.isdigit():
        answer += i
check = 0
sc = 0
try:
    if answer[0] != '+':
        raise AttributeError("неверный формат")
    if number[0] != '-' and number[-1] != '-':
        if number.count('(') == number.count(')'):
            for i in number:
                if i == '-':
                    check += 1
                else:
                    check = 0
                if check == 2:
                    raise AttributeError("неверный формат")
            for i in number:
                if i == '(' and sc != -1:
                    sc += 1
                elif i == ')':
                    sc -= 1
                if sc == 2 or sc == -2 or sc < 0:
                    raise AttributeError("неверный формат")
            for i in number:
                if not i.isdigit() and (i != '+' and i != '(' and i != ')' and i != '-'):
                    raise AttributeError('неверный формат')
            if len(answer) != 12:
                raise AttributeError('неверное количество цифр')
            print(answer)
        else:
            raise AttributeError("неверный формат")
    else:
        raise AttributeError("неверный формат")

except Exception as ex:
    print(ex)