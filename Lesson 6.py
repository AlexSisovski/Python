# Учебный курс: алгоритм и структуры данных на Python
# Домашнее задание к уроку 6
# Александр Сысовский
#
# ЗАДАНИЕ:
# Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы
# с наиболее эффективным использованием памяти.
#
# Версия Python - 3.7
# Операционная система - Windows 7
# Разряднсть - 64 bit

from pympler import asizeof
import sys

# Задание с предыдущих уроков:
# Во втором массиве сохранить индексы четных элементов первого массива.
from random import randrange

lst = []
lst_n = []

print('Адрес переменной i:')
for i in range(randrange(20, 50)):
    print(id(i))
    lst.append(randrange(1, 100))

for i in range(len(lst)):
    if lst[i] % 2 == 0:
        lst_n.append(i)

print('Индексы четных элементов:', lst_n)

# Попробуем проверить списки
print('Адрес переменной lst:', id(lst))
print('Объем памяти lst:', asizeof.asizeof(lst))
print('Адрес переменной lst_n:', id(lst_n))
print('Объем памяти lst_n:', asizeof.asizeof(lst_n))
print()

# Попробуем преобразовать списки, например во множетсво и проверим
lst_set = set(lst)
lst_n_set = set(lst_n)
print('Адрес переменной lst_set:', id(lst_set))
print('Объем памяти lst_set:', asizeof.asizeof(lst_set))
print('Адрес переменной lst_n_set:', id(lst_n_set))
print('Объем памяти lst_n_set:', asizeof.asizeof(lst_n_set))
print()

# Проверим размер пустых объектов
lst = []
tup = ()
set = set()
print('Объем памяти lst:', asizeof.asizeof(lst))
print('Объем памяти tup:', asizeof.asizeof(tup))
print('Объем памяти set:', asizeof.asizeof(set))
print()
# Явно видно, что кортеж потребляет меньше всего памяти
# Если нет необходимости добавлять элементы в массив,
# то эффективнее тогда пользоваться кортежем.

# Здесь просто поэкспериментируем.
# Проверим размер различных переменных
a = 1346579854
b = 'Test Text Text'
c = '01345 6789'
d = 0
e = 'Тестовый текст'
lst_txt = ['apple', 'orange', 'tea', 'water']
lst_num = [1, 2, 645, 71, 345]
lst_mix = lst_txt + lst_num
print('Объем памяти a:', asizeof.asizeof(a))
print('Объем памяти b:', asizeof.asizeof(b))
print('Объем памяти c:', asizeof.asizeof(c))
print('Объем памяти d:', asizeof.asizeof(d))
print('Объем памяти e:', asizeof.asizeof(e))
print('Объем памяти списка с текстом:', asizeof.asizeof(lst_txt))
print('Объем памяти списка с числами:', asizeof.asizeof(lst_num))
print('Объем памяти смешанного списка:', asizeof.asizeof(lst_mix))
print()
# Наиболее памяти потребляет переменная с текстом на русском языке


# Еще одно задание с прошлых уроков.
# Пользователь вводит две буквы, определить,
# на каких местах они стоят и сколько между ними находится букв.

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lst = []
for i in range(0, 2):
    lst.append(str(input('Введите букву: ')))
    position = letter.index(lst[i]) + 1
    print('Позиция буквы {} в списке - {}'.format(lst[i], position))

print('Количество букв между введенными буквами:',
    abs(letter.index(lst[0]) - letter.index(lst[1])))

# Объем используемой памяти проверим на списке и на кортеже
letter_tup = tuple(letter)
print('Объем памяти letter:', asizeof.asizeof(letter))
print('Объем памяти letter_tup:', asizeof.asizeof(letter_tup))
# Видим, что при конструкции с кортежем память используется более эффективно.
