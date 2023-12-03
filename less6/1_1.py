number = input('').strip()
answer = ''
if number[0] == '8':
    answer = '+7'
    number = number[1:]

for i in number:
    if i.isdigit():
        answer += i
check = 0
sc = 0
try:
    if number[0] != '-' and number[-1] != '-':
        if number.count('(') == number.count(')'):
            for i in number:
                if i == '-':
                    check += 1
                else:
                    check = 0
                if check == 2:
                    break
            for i in number:
                if i == '(' and sc != -1:
                    sc += 1
                elif i == ')':
                    sc -= 1
                if sc == 2 or sc == -2 or sc < 0:
                    sc = 2
                    break
            if check == 2 or sc == 2 or sc == -2:
                raise AttributeError("неверный формат")
            if len(answer) == 12 and answer[0] == '+' and check != 2 and sc != 2 and sc != -2:
                print(answer)
            elif (len(answer) != 12 or answer[0] != '+') and check != 2 and sc != 2 and sc != -2:
                raise AttributeError("неверное количество цифр")
        else:
            raise AttributeError("неверный формат")
    else:
        AttributeError("неверный формат")
except Exception as ex:
    print(ex)
