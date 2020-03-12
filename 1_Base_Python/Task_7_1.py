'''
Задание 7.1
Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def main():
    with open("ospf.txt", 'r') as ospf_file:
        for ospf_route in ospf_file.readlines():
            ospf_route_data_list = ospf_route.split()
            print(
                f"Protocol: {ospf_route_data_list[0].replace('O', 'OSPF')}\n"
                f"Prefix: {ospf_route_data_list[1]}\n"
                f"AD/Metric: {ospf_route_data_list[2].strip('[]')}\n"
                f"Next-Hop: {ospf_route_data_list[4].strip(',')}\n"
                f"Last update: {ospf_route_data_list[5].strip(',')}\n"
                f"Outbound Interface: {ospf_route_data_list[6]}\n"
            )


if __name__ == '__main__':
    main()
