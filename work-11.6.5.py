import math

radius = float(input('Введите радиус теоретически возможной планеты: '))
earth = 10.8321 * 10**11
volume = (4/3) * math.pi * radius ** 3

print(earth / volume)
if volume < earth:
    print('Объём планеты Земля больше в', round(earth / volume, 3), 'раз')
else:
    print('Объём планеты Земля меньше в', str(volume/volume) + '/' + str(round(earth / volume, 3))+' =', round(volume / earth, 3), 'раз')