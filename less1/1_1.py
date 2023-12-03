a = str(input())
b = str(input())
if a == b:
    print('ничья')
elif ((a == 'ножницы' and b == 'бумага') or
      (a == 'бумага' and b == 'камень') or
      (a == 'камень' and b == 'ножницы')):
    print('первый')
else:
    print('второй')
