num = int(input(''))
cord = []
while num != 0:
    cord.append(tuple(input().split(' ')))
    num -= 1
for i in cord:
    if '0' in i:
        print(f'({i[0]}, {i[1]})')
s_1, s_2, s_3, s_4 = 0, 0, 0, 0
for i in cord:
    if not ('0' in i):
        if int(i[0]) > 0 and int(i[1]) > 0:
            s_1 += 1
        elif int(i[0]) < 0 < int(i[1]):
            s_2 += 1
        elif int(i[0]) > 0 > int(i[1]):
            s_4 += 1
        else:
            s_3 += 1
print(f'I: {s_1}, II: {s_2}, III: {s_3}, IV: {s_4}.')
