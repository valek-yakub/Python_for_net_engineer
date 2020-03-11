'''
Задание 6.1
Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX.
Однако, в оборудовании cisco MAC-адреса используются в формате XXXX.XXXX.XXXX.
Создать скрипт, который преобразует MAC-адреса в формат cisco
и добавляет их в новый список mac_cisco
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def main():
    mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
    mac_list = []
    for mac_addr in mac:
        mac_list.append(mac_addr.replace(':', '.'))
    print(mac_list)

if __name__ == '__main__':
        main()