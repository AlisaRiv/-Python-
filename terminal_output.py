""" модуль вывода в терминал """
from file_interface import get_file, get_record_list, edit_record, create_record, delete_record, RECORD_KEY_LIST

def print_menu(menu):
    """ вывод меню в терминал """
    print('---', menu['description'], '---')
    for item in menu['items']:
        print(item[0], item[1])

def print_list(index = -1, date = ''):
    """ вывести список заметок """
    data = get_file()
    record_list = get_record_list(data, index, date)
    print('|'.join([*map(lambda key: f' {key} ', RECORD_KEY_LIST)]))
    print('\n'.join(map(' | '.join, record_list)))

def get_field_value(help_string, current_str = ''):
    """ создание/редактирование поля """
    if len(current_str) > 0:
        print(f'Текущее значение: {current_str}')
    value = input(f'{help_string}: ')
    return current_str if len(current_str) > 0 and len(value) == 0 else value

def print_edit_mode(index):
    """ редактирование по id """
    data = get_file()
    record_list = get_record_list(data, index)
    if len(record_list) < 1:
        print(f'Запись с id: {index} не найдена, редактирование отменено.')
        return
    title = get_field_value('Введите заголовок запииси', record_list[0][1])
    body = get_field_value('Введите текст запииси', record_list[0][2])
    res = edit_record(data, index, title, body)
    if res < 0:
        print('Ошибка при сохранении данных.')

def print_create_mode():
    """ добавить новую запись """
    title = get_field_value('Введите заголовок запииси')
    body = get_field_value('Введите текст запииси')
    create_record(title, body)

def print_delete_mode(record_id):
    """ удалить запись по id"""
    data = get_file()
    record_list = get_record_list(data, record_id)
    if len(record_list) < 1:
        print(f'Запись с id: {record_id} не найдена, удаление невозможно.')
        return
    c = input(f'Для удаления записи с id: {record_id} введите 9: ')
    if c == '9':
        delete_record(record_id)
    else:
        print(f'Удаление записи с id: {record_id} отменено.')
