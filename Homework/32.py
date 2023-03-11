# Задача 32: Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
# больше заданного максимума)
import random
min_number = int(input('min: '))
max_number = int(input('max: '))
random_mass1 = [random.randint(-10, 10) for _ in range(5)]
for i in range(len(random_mass1)):
    if min_number <= random_mass1[i] <= max_number:
        print(i)
print(random_mass1)
