first = str(input(''))
last = str(input(''))
if first == last:
    print('ничья')
elif ((first == 'ножницы' and last == 'бумага') or
      (first == 'ножницы' and last == 'ром') or
      (first == 'бумага' and last == 'камень') or
      (first == 'бумага' and last == 'пират') or
      (first == 'камень' and last == 'ножницы') or
      (first == 'камень' and last == 'ром') or
      (first == 'ром' and last == 'бумага') or
      (first == 'ром' and last == 'пират') or
      (first == 'пират' and last == 'ножницы') or
      (first == 'пират' and last == 'камень')):
    print('первый')
else:
    print('второй')