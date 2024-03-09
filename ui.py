""" модуль пользовательского интерфейса """
import datetime as dt
from terminal_output import print_menu, print_list, print_edit_mode, print_create_mode, print_delete_mode

STRING_INPUT_INVITE = 'Ведите число: '
STRING_INPUT_ERROR = 'Неправильный ввод '
STRING_INPUT_INDEX = 'Ведите индекс: '
STRING_INPUT_REC_ID = 'Ведите ID записи: '
STRING_INPUT_DATE = 'Ведите дату (ГГГГ-ММ-ДД): '
STRING_INPUT_DATE_ERROR = 'Введенна некорректная дата или некоректный формат: '

MAIN_MENU = {
  'description': 'Приложение заметки!',
  'items': (
    (1, 'создать'),
    (2, 'полный список'),
    (3, 'выбрать список по дате'),
    (4, 'просмотр записи по id'),
    (5, 'редактировать по id'),
    (6, 'удалить по id'),
    (0, 'выйти'),
  )
}

def get_command_list(menu):
    """ возвращает список команд """
    return [*map(lambda item: str(item[0]), menu['items'])]

def get_command(menu):
    """ выбор пункта меню """
    print_menu(menu)
    command_list = get_command_list(menu)
    while True:
        command = input(STRING_INPUT_INVITE)
        if command not in list(command_list):
            print('!!!', STRING_INPUT_ERROR, '!!!', command, list(command_list))
        else:
            return int(command)

def get_date():
    """ получить дату """
    date_string = input(STRING_INPUT_DATE).split('-')
    date_res = ''
    try:
        year, month, day = [int(item) for item in date_string]
        d = dt.date(year, month, day)
        date_res = d.strftime('%Y-%m-%d')
    except ValueError:
        print(STRING_INPUT_DATE_ERROR)
    return date_res

def interface():
    """ главное меню """
    while True:
        command = get_command(MAIN_MENU)
        if command == 1:
            print_create_mode()
        elif command == 2:
            print_list()
        elif command == 3:
            date = get_date()
            print_list(date = date)
        elif command == 4:
            index = input(STRING_INPUT_INDEX)
            print_list(index = index)
        elif command == 5:
            index = input(STRING_INPUT_INDEX)
            print_edit_mode(index = index)
        elif command == 6:
            record_id = input(STRING_INPUT_REC_ID)
            print_delete_mode(record_id)
        elif command == 0:
            break
