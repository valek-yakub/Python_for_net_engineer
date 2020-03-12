import sys

'''
Задание 7.2b
Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt
При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def main():
    cleared_config_file_name = "config_sw1_cleared.txt"
    ignore = ['duplex', 'alias', 'Current configuration']

    try:
        config_file_name = sys.argv[1]
    except IndexError:
        print("You didn't input config file name.")
        return

    with open(f"{config_file_name}", "r") as config_file,\
         open(f"{cleared_config_file_name}", "w") as clr_config_file:

        for config_line in config_file:
            ignore_sentence = False

            for ignore_word in ignore:
                if config_line.find(ignore_word) >= 0:
                    ignore_sentence = True
                    break
            if config_line.startswith('!') or ignore_sentence:
                continue

            clr_config_file.write(config_line)


if __name__ == '__main__':
    main()