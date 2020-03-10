"""
Задание 4.2
Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def main():
    mac = "AAAA:BBBB:CCCC"
    print(f"mac value before change: {mac}")
    mac = '.'.join(mac.split(':'))
    print(f"mac value after change: {mac}")


if __name__ == '__main__':
    main()