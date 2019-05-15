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
from random import shuffle

def array_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        for i in range(n):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

def array_sort_mod(arr):
    for n in range(len(arr) - 1, 0, -1):
        for i in range(n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

array = []
for i in range(randrange(40, 60)):
    array.append(randrange(-100, 100))

print('ПОПРОБУЕМ ЧЕРЕЗ СТАНДАРТНУЮ ФУНКЦИЮ СОРТИРОВКИ')
print('Оригинальный массив:\n', array)
array_sort(array)
print('Отсортированный массив:\n', array)

print()

print('\nПОПРОБУЕМ ЧЕРЕЗ МОДИФИЦИРОВАННУЮ ФУНКЦИЮ СОРТИРОВКИ')
shuffle(array)
print('Оригинальный массив:\n', array)
array_sort_mod(array)
print('Отсортированный массив:\n', array)
