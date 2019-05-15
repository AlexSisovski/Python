# Учебный курс: алгоритм и структуры данных на Python
# Домашнее задание к уроку 7
# Александр Сысовский
#
# ЗАДАНИЕ:
# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный
# массив, заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.

from random import randrange
import timeit

def array_sort():
    arr = []
    for i in range(randrange(40, 60)):
        arr.append(randrange(-100, 100))

    for n in range(len(arr) - 1, 0, -1):
        for i in range(n):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

def array_sort_mod():
    arr = []
    for i in range(randrange(40, 60)):
        arr.append(randrange(-100, 100))

    for n in range(len(arr) - 1, 0, -1):
        for i in range(n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

print('СРАВНИМ ПРОИЗВОДИТЕЛЬНОСТЬ ФУНКЦИЙ')
t1 = timeit.timeit('array_sort()', setup='from __main__ import array_sort', number=10000)
t2 = timeit.timeit('array_sort_mod()', setup='from __main__ import array_sort_mod', number=10000)
print('Test array_sort:\n{} ms\n\nTest array_sort_mod:\n{} ms'.format(t1, t2))

# Модифицированная функция хоть и немного, но все-таки выигрывает по производительности
# РЕЗУЛЬТАТЫ ЗАМЕРОВ:
#----------------------------
# алгоритм         |время, мс
#----------------------------
# array_sort        2.48112
# array_sort_mod    2.43640
# array_sort        2.51120
# array_sort_mod    2.45945
# array_sort        2.51498
# array_sort_mod    2.45546
#------------------

