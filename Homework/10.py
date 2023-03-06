# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть

import random

money = int(input('Введите количество монет: '))

zero = 0
one = 0


for i in range(money):
    num = random.randint(0, 1)
    money1 = num
    print(money1)
    if num == 0:
        zero += 1
    elif num == 1:
        one += 1
print(f'Орёл {one}, Решка {zero}')
if one > zero:
    print(f'нужно перевернуть {zero}')
elif zero > one:
    print(f'нужно перевернуть {one}')


# Аналогичное решение
import random

coins = [random.randint(0,1) for _ in range(9)]
print(coins)

print('Перевернуть 1' if coins.count(1) < coins.count(0) else 'Перевернуть 0')