# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
# 4

a = int(input('Vvedite A: '))
b = int(input('Vvedite B: '))


def summa(a, b):
    if a == a:
        print(f'число целое {1}')
        return summa(a+b)
    elif b == b:
        print(f'число отрицательное {-1}')
        return summa(a) + summa(-b)
    # else:
    #     return summa(a + b)


print(summa(a, b))
