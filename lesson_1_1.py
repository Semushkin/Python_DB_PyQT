'''
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
'''

import platform
from subprocess import Popen, PIPE
from ipaddress import ip_address


param = '-n' if platform.system().lower() == 'windows' else '-c'
URLS = ['5.255.255.5', '173.194.222.94', '1.10.1.3']


def host_ping(ip_lst):
    for url in ip_lst:
        ip = ip_address(url)
        args = ['ping', param, '1', str(ip)]
        process = Popen(args, stdout=PIPE)
        data = process.wait()
        if data == 0:
            print(f'{ip}: Узел доступен')
        else:
            print(f'{ip}: Узел недоступен')

host_ping(URLS)
