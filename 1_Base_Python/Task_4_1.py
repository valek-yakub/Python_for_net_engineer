"""
Обработать строку nat таким образом, чтобы в имени интерфейса вместо FastEthernet ,
было GigabitEthernet.
"""


def main():
    nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
    print(f"nat value before replace:\n\t'{nat}'")
    nat = nat.replace('FastEthernet', 'GigabitEthernet')
    print(f"nat value after replace:\n\t'{nat}'")


if __name__ == "__main__":
    main()