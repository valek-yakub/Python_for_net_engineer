'''
Задание 5.2a
Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.
Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16
Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30
Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:
Network:
10        0         1         0
00001010  00000000  00000001  00000000
Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
Проверить работу скрипта на разных комбинациях сеть/маска.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


NET_MASK = '0' * 32


def main():
    ip_addr, ip_net_mask_size = input("Введите адрес ip-сети: ").split('/')

    ip_net_mask = '1' * int(ip_net_mask_size) + NET_MASK[int(ip_net_mask_size):]
    ip_addr = ip_addr.split('.')
    ip_addr = f"{int(ip_addr[0]):08b}{int(ip_addr[1]):08b}" \
                  f"{int(ip_addr[2]):08b}{int(ip_addr[3]):08b}"
    ip_net_addr_binary = f"{int(ip_addr, 2) & int(ip_net_mask, 2):32b}"
    ip_net_addr = [f"{int(ip_net_addr_binary[:8], 2)}", f"{int(ip_net_addr_binary[8:16], 2)}",
                   f"{int(ip_net_addr_binary[16:24], 2)}", f"{int(ip_net_addr_binary[24:32], 2)}"]
    ip_net_mask = [ip_net_mask[:8], ip_net_mask[8:16], ip_net_mask[16:24], ip_net_mask[24:]]

    print(f"Network:\n"
          f"{ip_net_addr[0]:<10}{ip_net_addr[1]:<10}{ip_net_addr[2]:<10}{ip_net_addr[3]:<10}\n"
          f"{int(ip_net_addr[0]):08b}  {int(ip_net_addr[1]):08b}  "
          f"{int(ip_net_addr[2]):08b}  {int(ip_net_addr[3]):08b}\n"
          f"\nMask:\n"
          f"/{ip_net_mask_size}\n"
          f"{int(ip_net_mask[0], 2):<10}{int(ip_net_mask[1], 2):<10}"
          f"{int(ip_net_mask[2], 2):<10}{int(ip_net_mask[3], 2):<10}\n"
          f"{ip_net_mask[0]:<10}{ip_net_mask[1]:<10}{ip_net_mask[2]:<10}{ip_net_mask[3]:<10}\n")


if __name__ == '__main__':
    main()
