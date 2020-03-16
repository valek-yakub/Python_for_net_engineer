from pprint import pprint
from collections import defaultdict

"""
Задание 9.3a
Сделать копию функции get_int_vlan_map из задания 9.3.
Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1
В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }
У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.
Проверить работу функции на примере файла config_sw2.txt
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def intfs_config(config_filename: str) -> defaultdict:
    """Func separates intf configuration part from the config file"""
    all_interfaces = defaultdict(list)
    intf = "interface "
    key_write_config = False

    with open(config_filename) as test_file:
        current_intf = None
        for line in test_file.readlines():
            if line.startswith(intf[0]):
                current_intf = line[len(intf):].rstrip()
                key_write_config = True
            elif key_write_config and line.startswith(' switchport'):
                all_interfaces[current_intf].append(line.strip())
            elif line.startswith('!'):
                key_write_config = False

    return all_interfaces


def get_int_vlan_map(config_filename: str) -> (defaultdict, defaultdict):
    """
    Func distributes intfs and its configuration to 2 dicts by work mode.
    """

    # trunk = defaultdict(list)
    # access = defaultdict(int)

    trunk = {}
    access = {}

    all_intfs = intfs_config(config_filename)

    for intf, commands in all_intfs.items():
        if len(commands) == 3:
            trunk.setdefault(intf, [])
            trunk[intf].extend(map(int, sorted(commands)[1].split()[-1].split(',')))
        elif len(commands) == 2:
            access[intf] = int(sorted(commands)[0].split()[-1])
        elif len(commands) == 1:
            access[intf] = 1

    return access, trunk


def main():
    pprint(get_int_vlan_map("config_sw2.txt"))


if __name__ == '__main__':
    main()
