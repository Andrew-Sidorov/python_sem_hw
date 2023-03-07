# Рекурсия

# def hello(a):
#     if a == 100:
#         return
#     print('Hello')
#     a += 1
#     hello(a)


# hello(0)
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
# Задача фибоначи
# fib1 = int(input("Введите номер числа Фибоначи:"))


def fibbonachi(fib1):
    if fib1 == 1:
#         return 1
#     elif fib1 == 0:
#         return 0
#     else:
#         return fibbonachi(fib1 - 1)+fibbonachi(fib1-2)


# print(fibbonachi(fib1))
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
##
#
#
#
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# import random
# leng_mass = int(input())
# random_mass = [random.randint(1, 5) for _ in range(leng_mass)]

# print(random_mass)
# i = 0
# while i < len(random_mass):
#     if random_mass[i] == 4 or random_mass[i] == 5:
#         random_mass[i] = 1
#     i += 1
# print(random_mass)
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
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# number = int(input('Введите число: '))


# def is_simpl(num: int):
#     if not num % 2 and num != 2:
#         for dev in range(3, num//2, 2):
#             if not num % dev:
#                 return False
#         return True


# print(is_simpl(number))
#
#
#
# TRY EXCEPT
#
# def input_int():
#     while True:
#         number = input('Введите число: ')
#         try:
#             if 0 < int(number) <= 100:
#                 return int(number)
#             else:
#                 print('Число должно быть от 1 до 100')
#         except:
#             print('Это не число. Повторите ввод')


# num = input_int()
# print(f'Урааа!!! Наконец-то правильн!!! {num} =)')
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
# Как написать слово задом наперёд
# string = 'Привет'
# print(string[::-1])
#
#
#
# GET
my_dict = {1: 'one', 2: 'two', 3: 'three'}

print(my_dict)

my_dict.get(5, my_dict.setdefault(5, 'five'))

print(my_dict)


# my_dict.setdefault(5, 'five')
# my_dict.setdefault(6, 'six')
# print(my_dict)


# my_dict[5] = 'five'


# def hello():
#     print('Takogo HET')


# print(my_dict.get(2, 'Takogo HET'))
