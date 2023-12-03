persons = str(input('')).split(' -> ')
num = int(input(''))
help_per = []
for i in range(num):
    help_per.append(input(''))
for i in help_per:
    if i in persons:
        if persons.index(i) == 0:
            print(f'{i} -> {persons[persons.index(i) + 1]}')
        elif persons.index(i) == (len(persons) - 1):
            print(f'{persons[persons.index(i) - 1]} -> {i}')
        else:
            print(f'{persons[persons.index(i) - 1]} -> {i} '
                  f'-> {persons[persons.index(i) + 1]}')
