'''
Задание 5.3a
Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'
Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''


ACCESS_TEMPLATE = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]
TRUNK_TEMPLATE = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]


def main():

    intf_mode_dict = {
        'access': (ACCESS_TEMPLATE, "Введите номер VLAN: "),
        'trunk': (TRUNK_TEMPLATE, "Введите разрешенные VLANы: ")
    }

    interface_mode = input("Введите режим работы интерфейса (access/trunk): ").lower()
    type_num_intf = input("Введите тип и номер интерфейса: ")
    vlan_nums = input(intf_mode_dict.get(interface_mode)[1])

    intf_mode_temp = "\n".join(intf_mode_dict.get(interface_mode)[0]).format(vlan_nums)

    print(f"\ninterface {type_num_intf}\n"
          f"{intf_mode_temp}\n")


if __name__ == '__main__':
    main()