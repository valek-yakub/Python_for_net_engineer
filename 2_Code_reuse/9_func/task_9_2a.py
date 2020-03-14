from pprint import pprint

"""
Задание 9.2a
Сделать копию функции generate_trunk_config из задания 9.2
Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


TRUNK_MODE_TEMPLATE = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

TRUNK_CONFIG = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}


def generate_trunk_config(intf_vlan_mapping, trunk_template):
    """
    Returns list of interfaces with trunk configuration.
    :param intf_vlan_mapping:
    :param trunk_template:
    :return:
    """

    returned_trunk_intfs = {}

    for intf, vlans in intf_vlan_mapping.items():
        returned_trunk_intfs.setdefault(intf, [])
        returned_trunk_intfs[intf].extend(trunk_template)
        returned_trunk_intfs[intf][
            returned_trunk_intfs[intf].index("switchport trunk allowed vlan")] += f" {','.join(map(str, vlans))}"

    return returned_trunk_intfs

def main():
    pprint(generate_trunk_config(TRUNK_CONFIG, TRUNK_MODE_TEMPLATE))


if __name__ == '__main__':
    main()
