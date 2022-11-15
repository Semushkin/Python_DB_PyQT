'''
3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. Но в данном случае
результат должен быть итоговым по всем ip-адресам, представленным в табличном формате (использовать модуль tabulate).
Таблица должна состоять из двух колонок и выглядеть примерно так:

Reachable
10.0.0.1
10.0.0.2

Unreachable
10.0.0.3
10.0.0.4
'''

import platform
from subprocess import Popen, PIPE
from ipaddress import ip_address
from tabulate import tabulate


param = '-n' if platform.system().lower() == 'windows' else '-c'
COLUMNS = ['reachable', 'unreachable']
reachable = []
unreachable = []


def host_range_ping():
    try:
        ip_set = ip_address(input("Укажите начальный IP:\n"))
    except ValueError:
        print('Ошибка! Указан не верный формат IP адреса')
        return
    try:
        range_set = int(input("Укажите диапазон:\n"))
    except ValueError:
        print('Ошибка! Указан не верный диапазон')
        return
    print('----------------------------------------')
    result = {}
    for i in range(0, range_set):
        ip_target = str(ip_set + i)
        args = ['ping', param, '1', ip_target]
        process = Popen(args, stdout=PIPE, stderr=PIPE)
        data = process.wait()
        if data == 0:
            reachable.append(ip_target)
        else:
            unreachable.append(ip_target)
    result['reachable'] = reachable
    result['unreachable'] = unreachable
    print(tabulate(result, headers='keys'))


host_range_ping()
