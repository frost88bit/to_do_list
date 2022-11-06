from data.data import *
from source.source import *
from helpers.helpers import *
import datetime
import json
from time import strftime
import csv
import os

def read_testdata_json():
    '''json loading function'''
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'data', "tasks.json")
    with open(file_path, 'r') as test_data1:
        loaded_test_data.extend(json.load(test_data1))

def write_testdata_json():
    '''json writing function'''
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'data', "tasks.json")
    with open(file_path, 'w') as test_data1:
        json.dump(loaded_test_data, test_data1)

print('Доступні функціі')
read_testdata_json()
start()
picker = input('Виберіть функцію, введіть відповідну букву: ')

while True:
    if picker == 'a':
        cls()
        if_chosen_a()
        chosen_a_name()
        chosen_a_descrip()
        chosen_a_prio()
        chosen_a_datetime()
        chosen_a_done()
        loaded_test_data.append(temp_dict)
        write_testdata_json()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'b':
        cls()
        if_chosen_b()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'c':
        cls()
        if_chosen_c()
        write_testdata_json()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'd':
        cls()
        if_chosen_d()
        write_testdata_json()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'e':
        cls()
        if_chosen_e()
        write_testdata_json()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'f':
        cls()
        if_chosen_f()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'g':
        cls()
        if_chosen_g()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'h':
        cls()
        if_chosen_h()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'i':
        cls()
        if_chosen_i()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'j':
        cls()
        if_chosen_j()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'k':
        cls()
        if_chosen_k()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'l':
        cls()
        if_chosen_l()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'm':
        cls()
        if_chosen_m()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'n':
        quit()

    else:
        start()
        picker = input('Виберіть функцію та введіть відповідну букву: ')


