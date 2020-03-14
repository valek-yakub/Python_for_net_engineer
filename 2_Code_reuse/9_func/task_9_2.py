from pprint import pprint

"""
Задание 9.2
Создать функцию generate_trunk_config, которая генерирует конфигурацию для trunk-портов.
У функции должны быть такие параметры:
- intf_vlan_mapping: ожидает как аргумент словарь с соответствием интерфейс-VLANы такого вида:
    {'FastEthernet0/1': [10, 20],
     'FastEthernet0/2': [11, 30],
     'FastEthernet0/4': [17]}
- trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде списка команд (список trunk_mode_template)
Функция должна возвращать список команд с конфигурацией
на основе указанных портов и шаблона trunk_mode_template.
В конце строк в списке не должно быть символа перевода строки.
Проверить работу функции на примере словаря trunk_config.
Пример итогового списка (перевод строки после каждого элемента сделан для удобства чтения):
[
'interface FastEthernet0/1',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 10,20,30',
'interface FastEthernet0/2',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 11,30',
...]
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

    returned_trunk_intfs = []

    for intf, vlans in intf_vlan_mapping.items():
        returned_trunk_intfs.append(f"interface {intf}")
        returned_trunk_intfs.extend(trunk_template)
        returned_trunk_intfs[
            returned_trunk_intfs.index("switchport trunk allowed vlan")] += f" {','.join(map(str, vlans))}"

    return returned_trunk_intfs

def main():
    pprint(generate_trunk_config(TRUNK_CONFIG, TRUNK_MODE_TEMPLATE))


if __name__ == '__main__':
    main()
