# Учебный курс: алгоритм и структуры данных на Python
# Домашнее задание к уроку 5
# Александр Сысовский

# Задание:
# Пользователь вводит данные о количестве предприятий, их наименования и
# прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
# определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно
# вывести наименования предприятий, чья прибыль ниже среднего.

import collections

comp_info = collections.defaultdict(list)
above_avg = collections.deque()
below_avg = collections.deque()
sum_ebit = 0

n = int(input('Введите количество предприятий: '))
for i in range(n):
    comp = (input('\nВведите наименование {}-й компании: '.format(i + 1)))
    ebit = 0
    for j in range(4):
        ebit += (int(input('|Введите прибыль за {}-й квартал: '.format(j + 1))))
    comp_info[comp] = ebit
    sum_ebit += ebit

avg_ebit = sum_ebit / n

print('\nПЕРЕЧЕНЬ АНАЛИЗИРУЕМЫХ ПРЕДПРИЯТИЙ:')
for key, val in comp_info.items():
    if val > avg_ebit:
        above_avg.appendleft(key)
    else:
        below_avg.appendleft(key)
    print('\t| Компания: {}, годовая прибыль: {}'.format(key, val))

print('\nСРЕДНЯЯ ГОДОВАЯ ПРИБЫЛЬ ПО ВСЕМ КОМПАНИЯМ:', int(avg_ebit)) 

print('\n\tПрибыль ниже среднего уровня у следующих предприятий:')
for elem in below_avg:
    print('\t|', elem)

print('\n\tПрибыль выше среднего уровня у следующих предприятий:')
for elem in above_avg:
    print('\t|', elem)

