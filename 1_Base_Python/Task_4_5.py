'''
Задание 4.5
Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.
Результатом должен быть список: ['1', '3', '8']
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def main():
    command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
    command2 = 'switchport trunk allowed vlan 1,3,8,9'
    com_1_2_intersection = sorted(list(
        set(command1.split()[-1].split(',')) &
        set(command2.split()[-1].split(','))
    ))
    print(f"Intersection between com1 and com2: {com_1_2_intersection}")



if __name__ == '__main__':
    main()