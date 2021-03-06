'''
Задание 4.4
Список vlans это список VLANов, собранных со всех устройств сети,
поэтому в списке есть повторяющиеся номера VLAN.
Из списка нужно получить уникальный список VLANов,
отсортированный по возрастанию номеров.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def main():
    vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
    uniq_vlans_list = sorted(list(set(vlans)))
    print(f"Vlan's list with unique values: {uniq_vlans_list}")


if __name__ == '__main__':
    main()