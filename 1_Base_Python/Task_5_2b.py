
import sys

'''
Задание 5.2b
Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


NET_MASK = '0' * 32


def main():
    ip_addr, ip_net_mask_size = sys.argv[1].split('/')

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
