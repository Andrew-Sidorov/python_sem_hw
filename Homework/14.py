# Задача 14: Требуется вывести все целые степени двойки(т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

N = int(input('Введите число: '))
i = 1
while i < N:
    i = i * 2
    print(i)


# Альтернатива
# n = int(input())
# i = 0
# while 2 ** i <= n:
# print(2 ** i)
# i += 1

# Альтернатива преподавателя 
number = int(input('Введите придел: '))
i=1
while i < number:
    print(i, end=' ')
    i*=2
