from pprint import pprint

"""
Задание 11.1
Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.
У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку.
Функция должна возвращать словарь, который описывает соединения между устройствами.
Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors
Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0
Функция должна вернуть такой словарь:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}
В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.
Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


cdp_output_filename = "sh_cdp_n_sw1.txt"


def parse_cdp_neighbors(command_output: str) -> dict:
    """
    Func processes 'show cdp neighbors' command output and returns dict, which contains
    info about port's neighborships.
    """
    list_command_output = command_output.strip().split('\n')
    current_device = list_command_output[0].split('>')[0]
    cdp_info_headers = "Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID"
    neighbors_list = [a.split() for a in list_command_output[list_command_output.index(cdp_info_headers)+1:]]
    return {(current_device,
             f"{neighbor_entity[1]}{neighbor_entity[2]}"):
                (neighbor_entity[0],
                 f"{neighbor_entity[-2]}{neighbor_entity[-1]}") for neighbor_entity in neighbors_list}


def main():
    with open(cdp_output_filename) as cdp_o_file:
         pprint(parse_cdp_neighbors(cdp_o_file.read()))


if __name__ == '__main__':
    main()