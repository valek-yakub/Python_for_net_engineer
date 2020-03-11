'''
Задание 5.2
Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24
Затем вывести информацию о сети и маске в таком формате:
Network:
10        1         1         0
00001010  00000001  00000001  00000000
Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
Проверить работу скрипта на разных комбинациях сеть/маска.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


NET_MASK = '0' * 32


def main():
    ip_net_addr, ip_net_mask_size = input("Введите адрес ip-сети: ").split('/')
    ip_net_mask = '1' * int(ip_net_mask_size) + NET_MASK[int(ip_net_mask_size):]
    ip_net_mask = [ip_net_mask[:8], ip_net_mask[8:16], ip_net_mask[16:24], ip_net_mask[24:]]
    ip_net_addr = ip_net_addr.split('.')

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
