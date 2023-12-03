data = []
with open("input.txt", "r", encoding="utf8") as file:
    for i in file:
        data.append(i)
file.close()
answer = 0
for i in data:
    if 'далек' in i.lower():
        answer += 1
print(answer)
