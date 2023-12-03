data = []
with open("input.txt", "r", encoding="utf8") as file:
    for i in file:
        data.append(i)
file.close()
answer = 0
word_list = ['далек', 'далеков',
             'далека', 'далеки',
             'далеку', 'далекам',
             'далеком', 'далеками',
             'далеке', 'далеках']

for i in data:
    yo = ''
    for j in i.split():
        for y in word_list:
            if y == j.lower():
                answer += 1
                yo = y
                break
        if yo == j.lower():
            break
print(answer)