import operator
from data.data import loaded_test_data
from data.data import temp_dict
from helpers.helpers import cls
import datetime
from time import strftime
import csv
import math


choose = {'a.': 'Створити новий запис (додати заплановану справу)',
          'b.': 'Знайти запис за частиною назви та переглянути її деталі',
          'c.': 'Знайти та помітити справу, як виконану',
          'd.': 'Знайти справу та змінити її пріоритет',
          'e.': 'Зайти та видалити справу',
          'f.': 'Переглянути всі заплановані справи (тільки назви) у порядку їхнього додавання',
          'g.': 'Переглянути всі заплановані справи (тільки назви) у порядку спадання пріоритету',
          'h.': 'Переглянути всі невиконані справи (тільки назви)',
          'i.': 'Переглянути виконані справи (тільки назви)',
          'j.': 'Переглянути прострочені справи (тільки назви)',
          'k.': 'Переглянути статистику (загальна кількість справ, кількість виконаних/невиконаних/прострочених справ)',
          'l.': 'Зберегти список справ як csv файл.',
          'm.': 'Завантажити тестові дані',
          'n.': 'Вийти'
          }

def start():
    for line in choose:
        print(line + ' ' + choose[line])

def if_chosen_a():
    ''' part of main function
    if user picked 'a' '''
    print('Створить новий запис (додати заплановану справу)')
    for dict in loaded_test_data:
        for key in dict:
            if key == 'id':
                iter_id = dict[key]
                temp_dict.update({'id': iter_id + 1})

def if_chosen_b():
    ''' part of main function
    if user picked 'b' '''
    my_input = input('Введіть назву: ')
    for element in loaded_test_data:
        for key, value in element.items():
            if str(value) == my_input:
                my_dict = element
                for key, value in my_dict.items():
                    print(key + ': ' + str(value))
                break

def if_chosen_c():
    ''' part of main function
    if user picked 'c' '''
    my_input = input('Введіть назву: ')
    while True:
        for element in loaded_test_data:
            for key, value in element.items():
                if str(value) == my_input and element['done'] == False:
                    done_value_changer = input('Бажаєте помітити справу я виконану? (y/n): ')
                    done_value_changer = done_value_changer.lower()
                    if done_value_changer == 'y':
                        element.update({'done': True})
                        my_dict = element
                        for key, value in my_dict.items():
                            print(key + ': ' + str(value))


                    elif done_value_changer == 'n':
                        print('Справа не була виконана')
                        quit()
                    else:
                        print('Не вірні данні')
        break

def if_chosen_d():
    ''' part of main function
    if user picked 'd' '''
    my_input = input('Введіть назву: ')
    while True:
        for element in loaded_test_data:
            for key, value in element.items():
                if str(value) == my_input:
                    prio_value_changer = int(input('Виберіть число на яке хочете змінити приорітет (від 1-10): '))
                    if prio_value_changer > element['priority'] or prio_value_changer < element['priority']:
                        element.update({'priority': prio_value_changer})
                        my_dict = element
                        for key, value in my_dict.items():
                            print(key + ': ' + str(value))
                        break

                    elif prio_value_changer == element['priority']:
                        print('Пріорітет не змінився')
                        quit()
                    else:
                        print('Не вірні данні')
        break

def if_chosen_e():
    ''' part of main function
    if user picked 'e' '''
    my_input = input('Введіть назву: ')
    while True:
        for element in loaded_test_data:
            for key, value in element.items():
                if str(value) == my_input:
                    verifier = input('Бажаєте видалити справу? (y/n): ')
                    verifier = verifier.lower()
                    if verifier == 'y':
                        loaded_test_data.remove(element)
                        print('Справа була видалена!')
                        for element in loaded_test_data:
                            for key, value in element.items():
                                print(key + ': ' + str(value))
                        break
                    elif verifier == 'n':
                        print('Справа не була видалена!')
                        quit()
                    else:
                        print('Не вірні данні')
        break

def if_chosen_f():
    ''' part of main function
    if user picked 'f' '''
    for element in loaded_test_data:
        print(element['title'])

def if_chosen_g():
    ''' part of main function
    if user picked 'g' '''
    sorted_list = sorted(loaded_test_data, key=lambda x: x['priority'])
    titles_list = [x['title'] for x in sorted_list]
    print(titles_list)

def if_chosen_h():
    ''' part of main function
    if user picked 'h' '''
    for element in loaded_test_data:
        for key, value in element.items():
            if element['done'] == False:
                print(element['title'])
            break

def if_chosen_i():
    ''' part of main function
    if user picked 'i' '''
    for element in loaded_test_data:
        for key, value in element.items():
            if element['done'] == True:
                print(element['title'])
            break

def if_chosen_j():
    ''' part of main function
    if user picked 'j' '''
    for element in loaded_test_data:
        for key, value in element.items():
            if element['done'] == False and element['due_date'] < str(datetime.datetime.now()):
                print(element['title'])
            break

def if_chosen_k():
    ''' part of main function
    if user picked 'k' '''
    temp_list_undone = []
    temp_list_done = []
    for element in loaded_test_data:
        for key, value in element.items():
            if element['done'] == False:
                temp_list_undone.append(element['done'])
            undone = len(temp_list_undone)
            break

        for key, value in element.items():
            if element['done'] == True:
                temp_list_done.append(element['done'])
            done = len(temp_list_done)
            break
    print('Ви маєте - ' + str(undone) + ' невиконаних й виконаних - ' + str(done))

def if_chosen_l():
    with open('test_data.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter='\n',
                                 quotechar='|', quoting = csv.QUOTE_MINIMAL)
        spamwriter.writerow(loaded_test_data)

    with open('test_data.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter = '\n', quotechar = '|')
        for row in spamreader:
            ', '.join(row)

def if_chosen_m():
    ''' part of main function
    if user picked 'm' '''
    for element in loaded_test_data:
        for key, value in element.items():
            print(key + ': ' + str(value))



