import sys

'''
Задание 7.2a
Сделать копию скрипта задания 7.2.
Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def main():
    ignore = ['duplex', 'alias', 'Current configuration']

    try:
        config_file_name = sys.argv[1]
    except IndexError:
        print("You didn't input config file name.")
        return

    with open(f"{config_file_name}", "r") as config_file:
        for config_line in config_file:
            ignore_sentence = False

            for ignore_word in ignore:
                if config_line.find(ignore_word) >= 0:
                    ignore_sentence = True
                    break
            if config_line.startswith('!') or ignore_sentence:
                continue

            print(config_line, end="")


if __name__ == '__main__':
    main()