from data.data import temp_dict
from data.data import loaded_test_data
import datetime
import json


def cls():
    '''
    screen cleaner
    '''
    print('\n'*100)

def chosen_a_name():
    '''part with title input'''
    var_title = input('Введіть назву запису: ')
    index = 0
    for index in var_title:
        if len(var_title) == 0:
            print('Недостатня кількість символів')
            var_title = input('Введіть назву запису: ')

        elif len(var_title) >= 50:
            print('Дуже багато символів')
            var_title = input('Введіть назву запису: ')

        elif len(var_title) <= 50:
            temp_dict.update({'title': var_title})

def chosen_a_descrip():
    '''part with descrip input'''
    var_description = input('Введіть описання: ')
    var_title = temp_dict.get('title')
    while True:
        if len(var_description) == 0:
            temp_dict.update({'description': var_title})
            break
        else:
            temp_dict.update({'description': var_description})
            break

def chosen_a_prio():
    '''part with priority input'''
    var_priority = int(input('Введыть пріорітет від 1 до 10 (10-максимальний пріоритет, 1-мінімальний): '))
    while True:
        if var_priority >= 1 and var_priority <= 10:
            temp_dict.update({'priority': var_priority})
            break
        else:
            print('Не вірні данні')
            var_priority = int(input('Введыть пріорітет від 1 до 10 (10-максимальний пріоритет, 1-мінімальний): '))

def chosen_a_datetime():
    '''part with datetime input'''
    print('Введыть час та дату запису')
    while True:
        year = int(input('Укажіть рік: '))
        month = int(input('Укажіть місяць: '))
        day = int(input('Укажіть день: '))
        hour = int(input('Укажіть годину: '))
        minutes = int(input('Укажіть минути: '))
        specific_time = datetime.datetime(year, month, day, hour, minutes)
        specific_time = str(specific_time)
        temp_dict.update({'due_date': specific_time})
        break

def chosen_a_done():
    '''part with done part'''
    var_done = False
    temp_dict.update({'done': var_done})
    print('Запис було создано')


