import sys

'''
Задание 7.2
Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту
Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.
Между строками не должно быть дополнительного символа перевода строки.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def main():
    try:
        config_file_name = sys.argv[1]
    except IndexError:
        print("You didn't input config file name.")
        return

    with open(f"{config_file_name}", "r") as config_file:
        for config_line in config_file:
            if not config_line.startswith('!'):
                print(config_line, end="")


if __name__ == '__main__':
    main()