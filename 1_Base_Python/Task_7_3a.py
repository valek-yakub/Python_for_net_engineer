'''
Задание 7.3a
Сделать копию скрипта задания 7.3.
Дополнить скрипт:
- Отсортировать вывод по номеру VLAN
В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9
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

    mac_info.sort(key=lambda x: x[0])
    for mac_line in mac_info:
        print(f"{mac_line[0]:<8}{mac_line[1]:<18}{mac_line[2]}")


if __name__ == '__main__':
    main()