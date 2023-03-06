# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

import random
X = random.randint(1, 10)
Y = random.randint(1, 10)
S = X + Y
P = X * Y
print(f'Петя загадал {S} и {P}')
print(f'Катя отгадала {X} и {Y}')

# Альтернатива
# x = int(input())
# y = int(input())
# for i in range(x):
# for j in range(y):
# if x == i + j and y == i * j:
# print(i, j)



# Альтернатива преподавателя
summa = int(input('Введите сумму чисел: '))
melti = int(input('Введите протъизведение'))

flag = False
for x in range(1000):
    if flag:
        break
    for y in range (1000):
        if x + y == summa and x * y == multi:
            print(x,y)
            flag = True
            break

# Альтернатива преподавателя 2 

# x + y = z
# x*y=c
# y = z - x
# x*(z-x)=c
# -x**2 + z*x - c = 0

x = y = 0
a,b,c = 1, -summa, multi

def roots (a, b, c):
    discr = b**2 - 4*a*c
    if dicr > 0:
        x1 = (b - discr**0.5)/2*a
        x2 = (b + discr**0.5)/2*a
        return int(x1), int(x2)
    elif discr ==0:
        x = b / 2 * a
        return int(x)
    else:
        return 'Петя обманул Катю'
    
print(roots(a,b,c))    



