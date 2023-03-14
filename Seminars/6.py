# # # библиотека
# # from decimal import Decimal

# # number = 0.56
# # number_d = Decimal('0.56')

# # print(number*10)
# # print(number_d*10)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# 39/Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в
# первом массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом
# массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве.
# Затем элементы второго массива

# import random
# leng_mass1 = int(input('Vvedite dlinu  list 1: '))
# random_mass1 = [random.randint(1, 30) for _ in range(leng_mass1)]
# leng_mass2 = int(input('Vvedite dlinu  list 2: '))
# random_mass2 = [random.randint(1, 30) for _ in range(leng_mass2)]
# temp_list = []
# print(random_mass1)
# print(random_mass2)
# for i in random_mass1:
#     if i not in random_mass2:
#         temp_list.append(i)
# print(temp_list)

# Решение преподавателя
# res_list = [i for i in list_1 if i not in list_2]
# print(res_list)
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N —
# количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# import random
# leng_mass1 = int(input('Vvedite dlinu  list 1: '))
# random_mass1 = [random.randint(1, 30) for _ in range(leng_mass1)]
# count = 0
# for i in range(-1, leng_mass1 - 1):
#     if random_mass1[i - 1] < random_mass1[i] > random_mass1[i+1]:
#         count += 1
# print(random_mass1)
# print(count)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.
# import random
# leng_mass1 = int(input('Vvedite dlinu  list 1: '))
# random_mass1 = [random.randint(1, 30) for _ in range(leng_mass1)]
# count = 0
# for i in random_mass1:
#     if random_mass1.count(i) > 1:
#         count += 1
# print(count // 2)
# print(random_mass1)

# Решение преподлавателя
# import random
# list_1 = [random.randint(0, 20)
#           for _ in range(int(input('Vvedite razmer list: ')))]
# count = 0
# pairs_list = []
# for item in set(list_1):
#     pairs = list_1.count(item) // 2
#     count += pairs
#     if pairs:
#         [pairs_list.append(item) for _ in range(pairs*2)]
#     [list_1.remove(item) for _ in range(pairs*2)]

# print(pairs_list)
# print(list_1)
# print(count)
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но
# исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести
# все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке,
# разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

# len_arr = int(input('Vvedite K: '))
# my_dict = {}
# for i in range(1, len_arr):
#     my_dict[i] = my_dict.get(i, 0)
#     for j in range(1, i//2+1):
#         if i % j == 0:
#             my_dict[i] = my_dict.get(i, 0) + j
# print(my_dict)
# for key1, value1 in my_dict.items():
#     for key2, value2 in my_dict.items():
#         if key2 > key1:
#             if key1 != key2 and value1 == key2 and value2 == key1:
#                 print(f'{key1} {key2}')
##
#
#
#
#
#
#
#
#
s = [1, 2, 3, 8, 4]
a = s // 2
print(a)
