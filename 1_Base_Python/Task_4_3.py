'''
Задание 4.3
Получить из строки config список VLANов вида:
['1', '3', '10', '20', '30', '100']
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def main():
    config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
    vlan_list = config.split()[-1].split(',')
    print(f"vlan's list: {vlan_list}")

if __name__ == '__main__':
    main()