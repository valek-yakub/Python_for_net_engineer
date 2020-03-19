from pprint import pprint
from collections import defaultdict

"""
Задание 9.4
Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком
У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.
Проверить работу функции на примере файла config_sw1.txt
При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.
Для проверки надо ли игнорировать строку, использовать функцию ignore_command.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


ignore = ['duplex', 'alias', 'Current configuration', '!']


def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)


def convert_config_to_dict(config_filename: str) -> dict:
    """
    Func receives configuration file,
    then that file's converted to the dict, which is returned.
    """

    sw_config_dict = {}
    current_key = None

    with open(config_filename) as sw_config:
        allowed_sw_config_commands = [allowed_command for allowed_command in sw_config.readlines()
                                      if not ignore_command(allowed_command, ignore)]

    for command in allowed_sw_config_commands:
        if not command.startswith(' '):
            current_key = command.strip()
            sw_config_dict.setdefault(current_key, [])
        else:
            sw_config_dict[current_key].append(command.strip())

    return sw_config_dict


def main():
    pprint(convert_config_to_dict("config_sw1.txt"))


if __name__ == '__main__':
    main()
