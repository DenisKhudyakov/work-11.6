
# Рассмотрите разность суммы и разности чисел, сумму разности и суммы чисел.
# При необходимости можете использовать функцию abs(), позволяющую взять модуль числа.

number1 = int(input('Введите первое число '))
number2 = int(input('Введите второе число '))

max = abs(((number1 + number2) - (number1 - number2)) - ((number1 - number2) + (number1 + number2)))
print('Максимальное число', max) # работает при условии, если первое число в два раза больше второго

# (a*(a//b) + b*(b//a))/(b//a+a//b)
max = (number1*(number1//number2) + number2*(number2 // number1))/(number2//number1+number1//number2)
print('Максимальное число', round(max))