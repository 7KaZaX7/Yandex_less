data = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
        "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
        "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
        "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
        "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
        "б": "b", "ю": "ju", "ё": "jo"}
data_file = []
with open("*.txt") as file:
    for i in file:
        data_file.append(i)
    file.close()
file = open("*.txt", 'w')
k = ''
for i in data_file:
    for y in i:
        if y in data.keys():
            k += data[y]
        elif y.lower() in data.keys():
            k += data[y.lower()].capitalize()
        else:
            k += y
    print(k, end='', file=file)
    k = ''
file.close()
