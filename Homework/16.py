# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random

num = int(input('Введите искомое число: '))
list = [random.randint(0, 10) for _ in range(5)]
print(list)

count = 0
for i in list:
    if i == num:
        count = count + 1

print(f'Колличество искомых чисел: {count}')
