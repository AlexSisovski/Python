# Задание 1. Проанализировать алгоритм.
#
# Возьмем задание 5 с прошлого ДЗ
#
# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
from random import sample

# Вопсользуемся четырмя вариантами алгоритма:
#   test1 - список с использованием встроенных функций
#   test2 - список без использования встроенных функций
#   test3 - кортеж с использованием встроенных функций
#   test4 - кортеж без использования встроенных функций

def test1():
    lst = sample(range(-1000, 1000), 10)
    print('Mаксимальный отрицательный элементm:', min(lst))
    print('Положение данного элемента в списке:',lst.index(min(lst)))

def test2():
    lst = sample(range(-1000, 1000), 10)
    i_min = 0
    for i in range(len(lst)):
        if lst[i] <= lst[i_min]:
            i_min = i
    print('Значение элемента:', lst[i_min])
    print('Позиция элемента вмассиве:', i_min)

def test3():
    lst = sample(range(-1000, 1000), 10)
    tuple(lst)
    print('Mаксимальный отрицательный элементm:', min(lst))
    print('Положение данного элемента в списке:',lst.index(min(lst)))
    
def test4():
    lst = sample(range(-1000, 1000), 10)
    tuple(lst)
    i_min = 0
    for i in range(len(lst)):
        if lst[i] <= lst[i_min]:
            i_min = i   
    print('Значение элемента:', lst[i_min])
    print('Позиция элемента вмассиве:', i_min)
    

# ОЦЕНКА РАБОТЫ АЛГОРИТМА
# Используем timeit:
import timeit

t1 = timeit.timeit('test1()', setup='from __main__ import test1', number=1000)
t2 = timeit.timeit('test2()', setup='from __main__ import test2', number=1000)
t3 = timeit.timeit('test3()', setup='from __main__ import test3', number=1000)
t4 = timeit.timeit('test4()', setup='from __main__ import test4', number=1000)

print('test1 = {} ms\ntest2 = {} ms\ntest3 = {} ms\ntest4 = {} ms'.format(t1, t2, t3, t4))

# РЕЗУЛЬТАТЫ ЗАМЕРОВ:
#------------------
# алгоритм|время, мс
#------------------
# test1    4.26930
# test2    4.02305
# test3    4.06002
# test4    3.99836
#------------------
# Анализ алгоримта показывает, что лучше всего
# работает функция с исполльзованием кортежа без встроенных функций.
