'''
Задание 6.2a
Сделать копию скрипта задания 6.2.
Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.
Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def check_ip_address(ip_address):
    """Func checks the typed 'ip address' by user is really ip address."""
    temp_ip_address_list = ip_address.split('.')
    if len(temp_ip_address_list) != 4:
        return False
    try:
        for i in temp_ip_address_list:
            if 255 < int(i) or int(i) < 0: return False
    except ValueError:
        return False
    else:
        return True

def main():
    ip_address = input("Введите IP адрес (формат 10.0.1.1): ")
    ip_address_list = ip_address.split('.')

    if not check_ip_address(ip_address):
        print("Invalid ip address!!!")
        return

    if '1' <= ip_address_list[0] <= '223':
        print(f"{ip_address} - unicast.")
    elif '224' <= ip_address_list[0] <= '239':
        print(f"{ip_address} - multicast.")
    elif ip_address == '255.255.255.255':
        print(f"{ip_address} - local broadcast.")
    elif ip_address == '0.0.0.0':
        print(f"{ip_address} - unassigned.")
    else:
        print(f"{ip_address} - unused.")


if __name__ == '__main__':
    main()