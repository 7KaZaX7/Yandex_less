num = int(input(''))
cord = list(map(tuple, (input().split() for i in range(num))))
minx, miny, maxx, maxy, = ((int(cord[0][0]), int(cord[0][1])),
                           (int(cord[0][0]), int(cord[0][1])),
                           (int(cord[0][0]), int(cord[0][1])),
                           (int(cord[0][0]), int(cord[0][1])))
for i in cord:
    if int(i[0]) < int(minx[0]):
        minx = tuple(map(int, i))
    if int(i[0]) > int(maxx[0]):
        maxx = tuple(map(int, i))
    if int(i[1]) > int(maxy[1]):
        maxy = tuple(map(int, i))
    if int(i[1]) < int(miny[1]):
        miny = tuple(map(int, i))
for i in cord:
    if abs(int(i[0])) > abs(int(i[1])):
        print(f'({i[0]}, {i[1]})')
print(f'left: {minx}\n'
      f'right: {maxx}\n'
      f'top: {maxy}\n'
      f'bottom: {miny}')