# Задача 30:  Заполните массив элементами арифметической прогрессии. Её
# первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input('Vvedite A: '))
d = int(input('Vvedite D: '))
n = int(input('Vvedite N: '))
list = []
for i in range(n):
    list = a+i*d
print(list)