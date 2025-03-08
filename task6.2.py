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

water = int(input('Температура: '))
meter = 0
while water > 15:
    meter += 20
    water -= 2
    if water <= 15:
        break
    meter +=10
print('Прошел дистанцию ', meter)
    
    
    