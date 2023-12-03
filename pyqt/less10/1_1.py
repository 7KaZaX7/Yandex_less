with open('foreigner.txt', 'r') as file:
    data = file.read()

lines = data.split('; ')

answer = set()
for i in lines:
    words = i.split()
    word = ' '.join(words[:2])
    answer.add(word.lower())

with open('signs.txt', 'w') as file:
    for sign in answer:
        file.write(sign + '\n')



