# Учебный курс: алгоритм и структуры данных на Python
# Домашнее задание к уроку 3
# Александр Сысовский

# Задание 2.
# Во втором массиве сохранить индексы четных элементов первого массива.
from random import randrange

lst = []
lst_n = []

for i in range(randrange(20, 30)):
    lst.append(randrange(1, 100))

for i in range(len(lst)):
    if lst[i] % 2 == 0:
        lst_n.append(i)

print('Индексы четных элементов:', lst_n)            

# _______________________________________________________________________________
# Задание 3.
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import sample

lst = sample(range(-30, 30), 15)
print('Оригинальный список:\n' + str(lst))

num_max = max(lst)
num_min = min(lst)

i_max = lst.index(max(lst))
i_min = lst.index(min(lst))

lst[i_max] = num_min
lst[i_min] = num_max

print('Измененный список:\n' + str(lst))
# _______________________________________________________________________________
# Задание 4.
# Определить, какое число в массиве встречается чаще всего.

from random import randrange

lst = []
for i in range(randrange(20, 30)):
    lst.append(randrange(-30, 30))

counter = 0
for i in range(len(lst)):
    x = lst.count(lst[i])
    # print('number: {}, counter: {}.'.format(lst[i], x))
    if x > counter:
        counter = x
        number = lst[i]
if counter > 1:        
    print('Наиболее часто встречаемое число:', number)
else:
    print('Все числа встречаются по одному разу.')
    
# _______________________________________________________________________________
# Задание 5.
# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
from random import sample

lst = sample(range(-30, 30), 15)

# УПРОЩЕННАЯ РЕАЛИЗАЦИЯ:
print('Mаксимальный отрицательный элементm:', min(lst))
print('Положение данного элемента в списке:',lst.index(min(lst)))

# РЕАЛИЗАЦИЯ УСЛОЖНЕННЫМ ВАРИАНТОМ БЕЗ ИСПОЛЬЗОВАНИЯ ВСТРОЕННЫХ ФУНКЦИЙ:
i_min = 0
for i in range(len(lst)):
    if lst[i] <= lst[i_min]:
        i_min = i   
print('Значение элемента:', lst[i_min])
print('Позиция элемента вмассиве:', i_min)


# _______________________________________________________________________________
# Задание 6.
# В одномерном массиве найти сумму элементов, находящихся между минимальным
# и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
from random import sample

lst = sample(range(-30, 30), 15)
print('последовательность:', lst)

# РЕАЛИЗАЦИЯ УСЛОЖНЕННЫМ ВАРИАНТОМ БЕЗ ИСПОЛЬЗОВАНИЯ ВСТРОЕННЫХ ФУНКЦИЙ:
i_max = 0
i_min = 0
for i in range(len(lst)):
    if lst[i] >= lst[i_max]:
        i_max = i
    if lst[i] <= lst[i_min]:
        i_min = i    
    
num_sum = 0    
for i in range(i_min, i_max):
    num_sum += lst[i]
num_list -= lst[i_min]
    
print('индекс максимального элемента:', i_max)
print('индекс минимального элемента:', i_min)
print('Сумма элементов между минимальным и максимальным:', num_sum)

# _______________________________________________________________________________
# Задание 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее
# в последнюю ячейку строки. В конце следует вывести полученную матрицу.
matrix = []
# ВАРИАНТ РЕАЛИЗАЦИИ БЕЗ ИСПОЛЬЗОВАНИЯ ВСТРОЕННЫХ ФУНКЦИЙ:
for i in range(4):
    response = input('Введите четыре числа через пробел: ').split()
    row = []
    sum_row = 0
    for elem in response:
        row.append(int(elem))
        sum_row += int(elem)
    row.append(sum_row)
    matrix.append(row)

for line in matrix:
    print(line)

# ВАРИАНТ РЕАЛИЗАЦИИ СО ВСТРОЕННОЙ ФУНКЦИЕЙ sum():
for i in range(4):
    response = input('Введите четыре числа через пробел: ').split()
    row = []
    for elem in response:
        row.append(int(elem))
    row.append(sum(row))
    matrix.append(row)for line in matrix:
    print(line)

