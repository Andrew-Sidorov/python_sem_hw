# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень
# B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

number_A = int(input('Введите число A: '))
number_B = int(input('Введите число B: '))


def summa(a, b):
    if a == number_A:
        return a
    elif b == number_B:
        return b
    else:
        return summa(a)**summa(b)


print(summa(a, b))


# без рекурсии
print(number_A ** number_B)
