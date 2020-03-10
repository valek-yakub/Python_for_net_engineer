'''
Задание 4.6
Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''



def main():
    ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
    ospf_route_data_list = ospf_route.split()
    print(f"""\tProtocol: {ospf_route_data_list[0].replace("O", "OSPF")}
    Prefix: {ospf_route_data_list[1]}
    AD/Metric: {ospf_route_data_list[2].strip('[]')}
    Next-Hop: {ospf_route_data_list[4].strip(',')}
    Last update: {ospf_route_data_list[5].strip(',')}
    Outbound Interface: {ospf_route_data_list[6]}
    """)


if __name__ == '__main__':
    main()