# Учебный курс: алгоритм и структуры данных на Python
# Домашнее задание к уроку 8
# Александр Сысовский
#
# ЗАДАНИЕ:
# Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

import hashlib
import timeit

def sha1():
    s = 'python'
    subs_lst = []
    hash_lst = []
    lenght = len(s)

    for i in range(lenght-1):
        subs_lst.append(s[0:lenght-i])
        subs_lst.append(s[i+1:lenght])

    for n in subs_lst:
        hash = hashlib.sha1(n.encode('utf-8')).hexdigest()
        hash_lst.append(hash)
    print('SHA1:', hash_lst)

def sha224():
    s = 'python'
    subs_lst = []
    hash_lst = []
    lenght = len(s)

    for i in range(lenght-1):
        subs_lst.append(s[0:lenght-i])
        subs_lst.append(s[i+1:lenght])

    for n in subs_lst:
        hash = hashlib.sha224(n.encode('utf-8')).hexdigest()
        hash_lst.append(hash)
    print('SHA224:', hash_lst)

def sha512():
    s = 'python'
    subs_lst = []
    hash_lst = []
    lenght = len(s)

    for i in range(lenght-1):
        subs_lst.append(s[0:lenght-i])
        subs_lst.append(s[i+1:lenght])

    for n in subs_lst:
        hash = hashlib.sha512(n.encode('utf-8')).hexdigest()
        hash_lst.append(hash)
    print('SHA224:', hash_lst)

print('СРАВНИМ ПРОИЗВОДИТЕЛЬНОСТЬ ФУНКЦИЙ')
t1 = timeit.timeit('sha1()', setup='from __main__ import sha1', number=10000)
t2 = timeit.timeit('sha224', setup='from __main__ import sha224', number=10000)
t3 = timeit.timeit('sha512', setup='from __main__ import sha512', number=10000)
print('Test sha1:\n{} ms\nTest sha224:\n{} ms\nTest sha512:\n{} ms'.format(t1, t2, t3))

# РЕЗУЛЬТАТЫ ЗАМЕРОВ:
# Test sha1:
# 0.940691611 ms
# Test sha224:
# 0.00014208599999998572 ms
# Test sha512:
# 0.00014176600000004314 ms