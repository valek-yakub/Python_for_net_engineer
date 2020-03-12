'''
Задание 6.3
В скрипте сделан генератор конфигурации для access-портов.
Сделать аналогичный генератор конфигурации для портов trunk.
В транках ситуация усложняется тем, что VLANов может быть много, и надо понимать,
что с ним делать.
Поэтому в соответствии каждому порту стоит список
и первый (нулевой) элемент списка указывает как воспринимать номера VLAN,
которые идут дальше:
	add - VLANы надо будет добавить (команда switchport trunk allowed vlan add 10,20)
	del - VLANы надо удалить из списка разрешенных (команда switchport trunk allowed vlan remove 17)
	only - на интерфейсе должны остаться разрешенными только указанные VLANы (команда switchport trunk allowed vlan 11,30)
Задача для портов 0/1, 0/2, 0/4:
- сгенерировать конфигурацию на основе шаблона trunk_template
- с учетом ключевых слов add, del, only
Код не должен привязываться к конкретным номерам портов. То есть, если в словаре
trunk будут другие номера интерфейсов, код должен работать.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ACCESS_TEMPLATE = [
    'switchport mode access', 'switchport access vlan',
    'spanning-tree portfast', 'spanning-tree bpduguard enable'
]

TRUNK_TEMPLATE = [
    'switchport mode trunk', 'switchport trunk encapsulation dot1q',
    'switchport trunk allowed vlan'
]


def main():
    access = {
        '0/12': '10',
        '0/14': '11',
        '0/16': '17',
        '0/17': '150'
    }
    trunk = {
            '0/1': ['add', '10', '20'],
            '0/2': ['only', '11', '30'],
            '0/4': ['del', '17']
        }
    action = {
        'add': ' add',
        'del': ' remove',
        'only': ''
    }

    # Generator for the access mode
    for intf, vlan in access.items():
        print('interface FastEthernet' + intf)
        for command in ACCESS_TEMPLATE:
            if command.endswith('access vlan'):
                print(' {} {}'.format(command, vlan))
            else:
                print(' {}'.format(command))

    # Generator for the trunk mode
    for intf, act_vlans in trunk.items():
        print('interface FastEthernet' + intf)
        for command in TRUNK_TEMPLATE:
            if command.endswith('allowed vlan'):
                print(f" {command}{action.get(act_vlans[0])} {','.join(act_vlans[1:])}")
            else:
                print(f" {command}")


if __name__ == '__main__':
    main()