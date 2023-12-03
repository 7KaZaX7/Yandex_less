def check_float(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


data = []
with open('lines.txt') as file:
    for i in file.read().split():
        if i.isdigit() or check_float(i):
            data.append(i.strip())
file.close()
answer = ''
for i in data:
    if data.index(i) % 2 != 0:
        answer += '{} + '.format(i)
    else:
        answer += '{} * '.format(i)
print("%.2f" % eval(answer + '0'))
