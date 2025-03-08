# number = int(input('Введите число: '))
# total = 0
# while number != 0:
#     total += number
#     number = int(input('Введите число: '))
# print(total)

# step = int(input('Введите шаг прогрессии  '))
# total = 0
# while total < 93:
#     total +=step
#     print(total)

# water = int(input('Температура: '))
# meter = 0
# while water > 15:
#     meter += 20
#     water -= 2
#     if water <= 15:
#         break
#     meter +=10
# print('Прошел дистанцию ', meter)

# number = int(input('Введите число  '))
# summ = 0 # Считаем сумму всех чисел до появления  5
# while number != 0:
#     last_num = number % 10
#     print(last_num)
#     if last_num == 5:
#         print('Обнаружен разрыв ')
#         break
#     summ += last_num
#     number = number // 10
# print('Сумма чисел равна  ', summ)    

# book_lib =int(input('Сколько книг выдал библиотекарь? '))
# book_watch = int(input('Сколько книг просмотрено? '))
# book_res = int(input('Сколько требует реставрации? '))
# summ_res = 0
# summ_res += book_res
# while summ_res < 5:
#     book_watch = int(input('Сколько книг просмотрено? '))
#     book_res = int(input('Сколько требует реставрации? '))
#     summ_res += book_res
#     print('Требует реставрации ', summ_res)
#     print('На сегодня все благодарю за помощь')
# print('Ура практика завершена')
    
st_summ = int(input('Введите стартовую сумму '))
num = int(input('Какая цифра выпала? '))
while num != 3:
    print('Вы выиграли 500 рублей ')
    num = int(input('Какая цифра выпала? '))
else:        
    print('Вы проиграли все')
    print('Игра закончена')
    print('На счету осталось 0 рублей')
    
    
    # comment: 
# end while    
    
    