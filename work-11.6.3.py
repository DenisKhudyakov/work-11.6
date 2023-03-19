
size = int(input('Укажите размер файла для скачивания: '))
speed = int(input('Какова скорость вашего соединения: '))
second = 0
download = 0
for _ in range(0, size, speed):
    second += 1
    download += speed
    percent = download / size * 100
    if percent > 100:
        print('Прошло', second, 'сек. Скачано', size, 'из', size, 'Мб (100%)')
    else:
        print('Прошло', second, 'сек. Скачано', download, 'из', size,
        'Мб', '('+str(round(percent))+'%)')
