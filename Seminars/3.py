# #Общая задача
# Дан список чисел. Определите сколько в нём встречается различных чисел.

import random

my_list = [random.randint(0, 10) for _ in range(20)]
print(my_list)

new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)

print(new_list)
print(len(new_list))  # len -> длина списка


# # Аналагичное решение
# my_list = [random.randint(0, 10) for _ in range(20)]
# print(my_list)
# print(len(set(my_list)))


# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

# import random

# my_list = [random.randint(0, 10) for _ in range(10)]
# print(my_list)

# K = int(input('Введите на какое колличество элементов необходимо сдвинуть: '))

# for i in range(len(my_list)):

#     print(i)

# import random
# my_list = [random.randint(0, 10) for _ in range(10)]
# K = int(input('Введите K: '))
# print(my_list)

# list3 = my_list[K:] + my_list[:K]
# print(list3)

# решение преподавателя
# my_list = [i**2 for i in range(10) if i != 4]

# shift = int(input('Введите сдвиг: '))
# for i in range(shift):
#     my_list.insert(0, my_list.pop(-1))  # insert -> по ингдексу сдвигает вправо
# print(my_list)


# Задаем список из рандомных чисел (рандомной длины), нужно составить новый список только с
# уникальными значениями


import random
my_list = [random.randint(0, 10) for _ in range(10)]
# set_list = set(my_list)
# print(set_list)
my_dict = {}
for i in my_list:

    if my_dict.get[i]
    my_dict[i]

# решение преподавателя (через словари)

import random
my_list = [random.randint(0, 10) for _ in range(10)]
print(my_list)

my_dict = {}

for item in my_list:
    my_dict[item] = my_dict.get(item, 0) + 1
print(my_dict)

new_list = []
for key, value in my_dict.items():
    if value == 1:
        new_list.append(key)
print(new_list)

# Аналагичное решение через .COUNT
import random

my_list = [random.randint(0, 10) for _ in range(10)]
print(my_list)

new_list = []
for item in my_list:
    if my_list.count(item) == 1:
        new_list.append(item)
print(new_list)
