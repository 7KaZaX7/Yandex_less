h = sorted(list(map(int, input().split(' '))))
m = sorted(list(map(int, input().split(' '))))
for x in h:
    for y in m:
        if not (int(x) % 10 + int(x) // 10) == (int(y) % 10 + int(y) // 10):
            if x // 10 == 0 and y // 10 == 0:
                print(f'0{x}:0{y}')
            elif x // 10 == 0:
                print(f'0{x}:{y}')
            elif y // 10 == 0:
                print(f'{x}:0{y}')
            else:
                print(f'{x}:{y}')
