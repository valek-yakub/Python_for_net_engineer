import sys

'''
Задание 7.2c
Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации
Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.
Проверить работу скрипта на примере файла config_sw1.txt.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def main():
    ignore = ['duplex', 'alias', 'Current configuration']

    try:
        config_file_name = sys.argv[1]
        cleared_config_file_name = sys.argv[2]
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