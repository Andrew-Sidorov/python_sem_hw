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
for item in list:
    if item == num:
        count = count + 1


print(f'Колличество искомых чисел: {count}')

i = 0
while i < len(list):
    if list[i] == num:
        list[i] = num or list[i] - 1
    i += 1
    print(f'максимально близкое ему по значению {list}')
