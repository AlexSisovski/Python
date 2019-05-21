# Учебный курс: алгоритм и структуры данных на Python
# Домашнее задание к уроку 8
# Александр Сысовский
#
# ЗАДАНИЕ:
# Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

import hashlib

def get_substring(s):
    lst = []
    lenght = len(s)
    for i in range(lenght-1):
        lst.append(s[0:lenght-i])
        lst.append(s[i+1:lenght])
    return lst

def get_hash(s):
    lst = []
    for n in s:
        hash = hashlib.sha1(n.encode('utf-8')).hexdigest()
        lst.append(hash)
    return lst

string = 'python'
substrings = get_substring(string)
hash_lst = get_hash(substrings)

print('СТРОКА: {}'.format(string))
print('ПОДСТРОКИ:\n{}'.format(substrings))

for i in range(len(substrings)):
    print('\nПодстрока: {}\nхэш: {}'.format(substrings[i], hash_lst[i]))
