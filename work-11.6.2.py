import math

count = int(input('Введите количество чисел '))

for _ in range(count):
    number = float(input('Введите число '))
    if number > 0:
        print('Логарифм числа', number, 'равен', math.log(math.ceil(number)))
    else:
        print('Экспонента числа', number, 'равна', math.exp(math.floor(number)))
