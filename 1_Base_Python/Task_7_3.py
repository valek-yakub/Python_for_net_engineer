'''
Задание 7.3
Скрипт должен обрабатывать записи в файле CAM_table.txt.
Каждая строка, где есть MAC-адрес, должна быть обработана таким образом,
 чтобы на стандартный поток вывода была выведена таблица вида (показаны не все строки из файла):
 100    01bb.c580.7000   Gi0/1
 200    0a4b.c380.7000   Gi0/2
 300    a2ab.c5a0.7000   Gi0/3
 100    0a1b.1c80.7000   Gi0/4
 500    02b1.3c80.7000   Gi0/5
 200    1a4b.c580.7000   Gi0/6
 300    0a1b.5c80.7000   Gi0/7
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def main():
    mac_info = []

    file_name = "CAM_table.txt"

    with open(f"{file_name}", "r") as mac_file:
        for line in mac_file.readlines():
            if "DYNAMIC" in line:
                line_list = line.rstrip('\n').split()
                line_list.pop(2)
                mac_info.append(line_list)

    for mac_line in mac_info:
        print(f"{mac_line[0]:<8}{mac_line[1]:<18}{mac_line[2]}")


if __name__ == '__main__':
    main()