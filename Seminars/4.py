# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Решение преподавателя
# import random

# my_list = [random.randint(1, 5) for _ in range(10)]
# print(my_list)
# my_dict = {}


# for i in my_list:
#     my_dict[i] = my_dict.get(i, 0)+1 # <- для подсчёта цифр
#     print(str(i) if my_dict.get(i) == 0 else f'{i}_{my_dict.get(i)-1}', end=', ')
# print('\n' + f'{my_dict}')
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
##
#
#
#
#
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных
# слов содержится в этом тексте.

# string = '''Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько
# различных слов содержится в этом тексте.'''

# listString = string.lower().split()
# print(string)
# print(listString)

# my_dict = {}

# for word in listString:
#     my_dict[word] = my_dict.get(word, 0) + 1
# count = 0
# for _ in my_dict:
#     count += 1
# print(count)

# key = my_dict.keys()
# print(len(key))

# print(len(set(listString)))


# # Аналогичное решение
# string = input("Enter some words: ")
# set = set(string.split())
# print(len(set))

# Ещё решение
# text = "тесто пекло тесто"
# print(len(set(text.split())))
#
#
#
#
##
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
##
#
#
#
#
#
##
##
#
##
##
#
#
#
# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]

import random

my_list = [random.randint(1000, 9999) for _ in range(5)]
print(my_list)
my_list2 = []
my_list3 = []
num = (input('Введите число: '))

for value in my_list:
    el = str(value)
    if num in el:
        el = el.replace(num, ' ')
    my_list2.append(el)
print(my_list2)

for value in my_list2:
    sum_num = sum([(int(el)) for el in value])
    while sum_num > 9:
        sum_num = sum([(int(el)) for el in str(sum_num)])
    my_list3.append(sum_num)
print(my_list3)
print(set(my_list3))
