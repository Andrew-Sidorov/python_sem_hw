#
# def function(x):
#     if x%2==0:
#         return x
# arg_1 = function
# arg_2 = [1,2,3,4]
# func = map(arg_1, arg_2)
# print(list(func))
#
#
#
#
# Задача №47. Решение в группах У вас есть код, который вы не можете менять (так часто бывает, когда код в
# глубине программы используется множество раз и вы не хотите ничего сломать):
# transformation = values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений,
# а нужно получить его как есть. Напишите такое лямбда-выражение transformation, чтобы transformed_values
# получился копией values.
#
# values = [1, 23, 42, 'asdfg']
# trasformation = lambda x : x
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')
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
# Задача №49. Решение в группах Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой
# далекой планетой ту, орбита которой имеет самую большую площадь.
# Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту,
# по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды
# таких планет нет, зато искусственные спутники были были запущены на круговые орбиты.
# Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты.
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса.
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса.
# При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага:
# сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь.
# Гарантируется, что самая далекая планета ровно одна
# def find_farthest_orbit(orb):
#     new_orb = list(filter(lambda x: x[0] != x[1], orb))
#     # for cort in orb:
#     #     if cort[0] != cort[1]:
#     #         new_orb.append(cort)
#     return max(new_orb, key=lambda x: x[0]*x[1])


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
#
#
#
# Делаем список из строки и переводим в int
#
# my_string = '423213323'
# my_string = list(my_string)
# print(my_string)

# my_string = list(map(int, my_string))

# print(my_string)
# print(sum(my_string))
#
#
# my_string = list(filter(lambda x: x%2 == 0, my_string))  <- фильтр
# print(my_string)
#
# вместо лямбды поставим функцию:
# def is_odd(num: int) -> buul:
#     if num % 2 == 1:
#         return True
#     else:
#         return False
# my_string = list(filter(is_odd, my_string))
# print(my_string)
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
# my_string = '423213323'
# my_string = list(my_string)
# my_string = [int(x) for x in my_string if int(x) % 2 == 0]
# print(my_string)


# def is_odd(lst: list) -> list:
#     new_list = [int(x) for x in lst if int(x) % 2 == 0]
#     new_list = list(filter(lambda x: x % 2 != 0, lst))
#     return new_list


# my_string = '423213323'  # <- телефонный справочник!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# my_string = list(my_string)
# print(my_string)

# for i, item in enumerate(my_string, 5):
#     print(f'{i}. {item}')


# def func(num: int) -> tuple:
#     num1 = num**2
#     num2 = num - 2
#     return num1, num2
# power = func(5)
# print(power)
# list(power)[0] = 6
# print(power)
#
#
#
#
#
#
# /////////////////ZIP////////////////////создаёт кортедж
# my_string = '423213323'
# my_list = [1, 2, 3, 4, 5]
# my_string = list(my_string)
# print(my_string)
# print(my_list)
# new_list = list(zip(my_string, my_list))
# print(new_list)
#
#
#
#
#
#
#
#
#
# /////////////////ЛЯМБДА\\\\\\\\\\\\\\\\\\\\
# operation = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
# string = '3+2'
# string = list(string)
# print(string)

# for i, item in enumerate(string):
#     if string[i] in ['+', '-']:
#         print(operation.get(string[i])(int(string[i-1]), int(string[i+1])))
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
# ///////////////ФАЙЛ\\\\\\\\\\\\\\\\\\\\\
# path = 'C:\Users\sidor\OneDrive\Рабочий стол\Pyhton\Seminars\7.py'

# file = open(path, 'r', encoding='UTF-8')
# data = file.read()
# data = file.readline()
# data = file.readlines()

# print(data)
# #
#
#
#
#
#
#
path_to_r = 'C:\Users\sidor\OneDrive\Рабочий стол\Pyhton\Seminars\7.py'
path_to_w = 'C:\Users\sidor\OneDrive\Рабочий стол\Pyhton\Seminars\7.py'
path_to_a = 'C:\Users\sidor\OneDrive\Рабочий стол\Pyhton\Seminars\7.py'

with open(path_to_r, 'r', encoding='UTF-8') as file:
    <- чтение(ошибка)
    data = file.readline()
print(data)

with open(path_to_w, 'w', encoding='UTF-8') as file:
    <- создаёт и записывает
    file.write('text new')

with open(path_to_a, 'a', encoding='UTF-8') as file:
    <- дополнение(ошибка)
    file.write('text new')
