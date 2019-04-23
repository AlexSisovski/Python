# Программа для получения курсов валют USD, EURO, на заданную дату.
# Программа производит подключение по API Центрального Банка РФ www.cbr.ru
# Пользователь вводит необходимую дату и получает результат.
#
# Автор: Александр Сысовский, e-mail: alexsisovski@gmail.com
# Ver: 0.1

import requests
import datetime

def get_date():
    i = 0
    while i == 0:
        d = input('Введите дату в формате ddmmyyyy, на которую требуется получить курс: ')
        try:
            d_req = datetime.date(int(d[4:8]), int(d[2:4]), int(d[:2]))
            i = 1
            return d_req.strftime("%d/%m/%Y")
        except ValueError:
            print('\nОШИБКА! Некорректная дата!')

    
def get_result():
    result = {'USD': 0, 'EUR': 0}    
    print('\n...Выполняется запрос к базе данных Банка России...\n')
    try:
        r = requests.get("http://www.cbr.ru/scripts/XML_daily.asp?date_req=12/12/2015")
        s = str(r.text)
    except:
        print('...Ошибка выполнения запроса...\n')
        return result

    pattern = 'Доллар США</Name><Value>'
    usd_pos_in = s.find(pattern)
    if usd_pos_in != -1:
        usd_pos_out = s.find('</Value>', usd_pos_in + len(pattern))
        result['USD'] = s[usd_pos_in + len(pattern) : usd_pos_out]
    else:
        result['USD'] = 'Отсутствует курс на заданную дату'
        
    pattern = 'Евро</Name><Value>'
    eur_pos_in = s.find(pattern)
    if eur_pos_in != -1:
        eur_pos_out = s.find('</Value>', eur_pos_in + len(pattern))
        result['EUR'] = s[eur_pos_in + len(pattern) : eur_pos_out]
    else:
        result['EUR'] = 'Отсутствует курс на заданную дату'        
        
    print(result)

print('\n|=======================================================|')
print('|      УТИЛИТА ПОЛУЧЕНИЯ ИНФОРМАЦИИ О КУРСАХ ВАЛЮТ      |')
print('|=======================================================|\n')

# ОСНОВНОЙ КОД ЗАКОММЕНТИРУЕМ
# ПРОАНАЛИЗИРУЕМ ТОЛЬКО ФУНКЦИЮ ПОЛУЧЕНИЯ РЕЗУЛЬТАТОВ ПАРСИНГА
# ИСПОЛЬЗУЕМ МОДУЛИ cProfile и timeit

# response = 0
# while response != 'q':
    # date_req = get_date()
    # BASE_URL = "http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + date_req
    # result = get_result(BASE_URL)
      
    # print('Курсы валют на дату', date_req + ':')
    # for key, value in result.items():
    # print(' ', key + ':', value)
           
    # response = input('\nДля продолжения нажмите любую клавишу, для заврешения нажмите q: ')


import cProfile
cProfile.run('get_result()')

import timeit
test = timeit.timeit('get_result()', setup='from __main__ import get_result', number=1)
print(test)

if __name__ == '__main__':
    main()

