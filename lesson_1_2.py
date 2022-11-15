'''
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
'''


import platform
from subprocess import Popen, PIPE
from ipaddress import ip_address
from threading import Thread


param = '-n' if platform.system().lower() == 'windows' else '-c'


def ping_process(ip_target):
    args = ['ping', param, '1', ip_target]
    process = Popen(args, stdout=PIPE, stderr=PIPE)
    data = process.wait()
    if data == 0:
        print(f'{ip_target}: Узел доступен')
    else:
        print(f'{ip_target}: Узел недоступен')


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

    for i in range(0, range_set):
        ip_target = str(ip_set + i)
        Thread(target=ping_process, args=(ip_target, )).start()


host_range_ping()
