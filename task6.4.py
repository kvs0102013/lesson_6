# count = 10 #первоначальный таймер
# while count <= 10:
#     if count == 0:
#         print('Время вышло!')
#         break
#     else:
#         print(count)
#         count -= 1

active = int(input('Продолжаем работать? 1/0'))
while True:
    active = int(input('Продолжаем работать? 1/0'))
    if active == 0:
        print('Приложение закрываеться')
        print('Работа завершена')
        break
    