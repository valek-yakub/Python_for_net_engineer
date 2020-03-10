'''
Задание 4.7
Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def main():
    mac = 'AAAA:BBBB:CCCC'
    mac_elem_list = mac.split(':')
    print(f"Binary mac: {int(mac_elem_list[0], 16):b}"
          f"{int(mac_elem_list[1], 16):b}"
          f"{int(mac_elem_list[2], 16):b}")


if __name__ == '__main__':
    main()