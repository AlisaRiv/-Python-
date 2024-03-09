""" модуль работы с файлами """

import datetime as dt

FILE_NAME = 'data_note.csv'
ID_COUNTER_FILE_NAME = 'index_counter.txt'
RECORD_LEN = 1
RECORD_KEY_LIST = ('id', 'title', 'body', 'dateCreate', 'dateUpdate')

def get_file():
    """ получить все заметки """
    with open(FILE_NAME, 'r', encoding='utf--8') as f:
        data = f.readlines()
        return data

def get_counter():
    """ получить текущий id """
    with open(ID_COUNTER_FILE_NAME, 'r', encoding='utf--8') as f:
        data = f.readlines()
        # print(data)
        return data[0]

def inc_counter():
    """ увеличить счетчик на 1 """
    c = int(get_counter()) + 1
    with open(ID_COUNTER_FILE_NAME, 'w', encoding='utf--8') as f:
        f.write(str(c))

def get_record_count(data):
    """ получить количество записей """
    return int(len(data) / RECORD_LEN) - 2

def string_parsing (raw):
    """ строка в список """
    field_value = raw.split(';')
    res = []
    field_count = len(RECORD_KEY_LIST)
    for i in range(field_count):
        value = field_value[i]
        res.append(value if i + 1 < field_count else value[:-1])
    return res

def get_record_list(data, record_id = -1, date = ''):
    """ получить список записей """
    record_count = get_record_count(data)
    if record_count < 1:
        return []
    all_record = map(string_parsing, data[2:])
    record = []
    if len(date) > 0:
        for item in all_record:
            if item[3] == date:
                record.append(item)
    elif record_id == -1:
        return all_record
    else:
        for item in all_record:
            if item[0] == record_id:
                record = [item]
    return record

def edit_record(data, record_id, title, body):
    """ редактирование записи по индексу """
    record_count = get_record_count(data)
    if record_count < 1:
        return -1
    index = -1
    record_list = [*get_record_list(data)]
    for i, item in enumerate(record_list):
        if item[0] == record_id:
            # print(i)
            index = i
    if index < 0:
        return -2
    date_create = record_list[index][3]
    date_update = str(dt.datetime.now())
    value = [f'{record_id};{title};{body};{date_create};{date_update}\n']
    start_el = 2 + index
    stop_el = start_el + 1
    data[start_el: stop_el] = value
    with open(FILE_NAME, 'w', encoding='utf--8') as f:
        f.write(''.join(data))
    return 0

def create_record(title, body):
    """ сохранить новую запись """
    d = dt.datetime.now()
    date_create = d.strftime('%Y-%m-%d')
    date_update = str(d)
    c = get_counter()
    record_id = int(c) + 1
    value = f'{record_id};{title};{body};{date_create};{date_update}\n'
    with open(FILE_NAME, 'a', encoding='utf--8') as f:
        f.write(value)
        inc_counter()

def delete_record(record_id):
    """Функция удаляет запись."""
    data = get_file()
    record_count = get_record_count(data)
    if record_count < 1:
        return -1
    index = -1
    record_list = [*get_record_list(data)]
    for i, item in enumerate(record_list):
        if item[0] == record_id:
            print(i)
            index = i
    if index < 0:
        return -2
    start_el = 2 + index
    stop_el = start_el + 1
    del data[start_el: stop_el]
    with open(FILE_NAME, 'w', encoding='utf--8') as f:
        f.write(''.join(data))
        return 0
