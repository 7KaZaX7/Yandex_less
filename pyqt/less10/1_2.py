import sys
num = 0
for i in sys.stdin:
    data2 = ''
    with open(i.strip()) as file:
        for j in file.readlines():
            data = data2
            data2 = j
    data = data.split()
    data2 = data2.split()
    for y in range(len(data2)):
        if int(data2[y]) >= int(data[y]):
            num += 1
    with open('fate.txt', 'a') as file:
        file.writelines(f'{i[:-5]}: value {round((num/len(data)), 2)}\n')
    num = 0

