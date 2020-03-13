from pprint import pprint

'''
Задание 9.1a
Сделать копию функции из задания 9.1.
Дополнить скрипт:
* ввести дополнительный параметр, который контролирует будет ли настроен port-security
 * имя параметра 'psecurity'
 * по умолчанию значение None
 * для настройки port-security, как значение надо передать список команд port-security (находятся в списке port_security_template)
Функция должна возвращать список всех портов в режиме access
с конфигурацией на основе шаблона access_mode_template и шаблона port_security_template, если он был передан.
В конце строк в списке не должно быть символа перевода строки.
Проверить работу функции на примере словаря access_config,
с генерацией конфигурации port-security и без.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


ACCESS_MODE_TEMPLATE = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

ACCESS_CONFIG = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}

PORT_SECURITY_TEMPLATE = [
    'switchport port-security maximum 2',
    'switchport port-security violation restrict',
    'switchport port-security'
]

def generate_access_config(intf_vlan_mapping, access_template,  psecurity_template=None):
    '''
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - список команд для порта в режиме access
    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    '''

    result_intf_access_conf = []

    for intf, vlan in intf_vlan_mapping.items():
        result_intf_access_conf.append(f"interface {intf}")
        result_intf_access_conf.extend(access_template)
        result_intf_access_conf[result_intf_access_conf.index('switchport access vlan')] += f" {vlan}"
        if psecurity_template:
            result_intf_access_conf.extend(psecurity_template)

    return result_intf_access_conf


def main():
    pprint(generate_access_config(ACCESS_CONFIG, ACCESS_MODE_TEMPLATE))
    pprint(generate_access_config(ACCESS_CONFIG, ACCESS_MODE_TEMPLATE, PORT_SECURITY_TEMPLATE))


if __name__ == '__main__':
    main()