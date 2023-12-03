data = []
with open("input.txt", "r", encoding="utf8") as file:
    for i in file:
        i = i.strip()
        data.append(i)
file.close()
word = data[0]
data.remove(word)
num_answer = 0
answer = ''
for i in data:
    word1 = word
    len_word = 0
    for y in i:
        if y in word1:
            word1 = word1.replace(y, '', 1)
            len_word += 1
        if len_word == len(i):
            num_answer += 1
            answer += i + '\n'
print(f'{num_answer}\n{answer}')