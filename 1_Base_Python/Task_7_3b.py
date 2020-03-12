"""
Задание 7.3b
Сделать копию скрипта задания 7.3a.
Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def main():
    mac_info = []

    file_name = "CAM_table.txt"
    vlan_filter = input("Введите vlan: ")

    with open(f"{file_name}", "r") as mac_file:
        for line in mac_file.readlines():
            if "DYNAMIC" in line:
                line_list = line.rstrip('\n').split()
                line_list.pop(2)
                mac_info.append(line_list)

    for mac_line in sorted(mac_info, key=lambda x: x[0]):
        if mac_line[0] == vlan_filter or not vlan_filter:
            print(f"{mac_line[0]:<8}{mac_line[1]:<18}{mac_line[2]}")


if __name__ == '__main__':
    main()
