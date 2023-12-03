data = []
with open("input.txt", "r", encoding="utf8") as file:
    for i in file:
        data.append(i.split(' '))
file.close()
answer = 0
for i in data:
    for y in i:
        if y[:5].lower() == 'далек':
            answer += 1
            break
print(answer)