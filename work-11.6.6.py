print('Введите местоположение коня ')
X = float(input('По горизонтали '))
Y = float(input('По вертикали '))
print('Введите местоположение точки на доске:')
XX = float(input('По горизонтали '))
YY = float(input('По вертикали '))
if 0 < X < 0.8 and 0 < Y < 0.8 and 0 < XX < 0.8 and 0 < YY < 0.8:
    x_number = int(X * 10)
    y_number = int(Y * 10)
    x_path = int(XX * 10)
    y_path = int(YY * 10)
    print('Конь в клетке', (x_number, y_number), 'Точка в клетке', str((x_path, y_path))+'.')
    if abs((x_number - x_path)*(y_number - y_path)) == 2:
        print('Да, конь может ходить в эту точку.')
    else:
        print('Конь так не ходит')