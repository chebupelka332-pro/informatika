from ipaddress import *


"""net = ip_network("10.8.248.131/255.255.224.0", 0)  # адрес сети
print(net)"""


"""for mask in range(33):  # маска сети
    net = ip_network(f'158.116.11.146/{mask}', 0)
    print(net, net.netmask)"""


"""for mask in range(33):  # маска сети или адрес одинаковы или нет
    net1 = ip_network(f'157.127.182.76/{mask}', 0)
    net2 = ip_network(f'157.127.190.80/{mask}', 0)
    if net1 != net2 and net1.netmask == net2.netmask:
        print(net1, net2)"""


"""net = ip_network('0.0.0.0/255.255.254.0')  # количество адресов
print(net.num_addresses - 2)"""


"""for mask in range(33):  # количество адресов с условием
    net = ip_network(f'175.122.80.13/{mask}', 0)
    print(net, net.num_addresses)"""


"""count = 0  # сочетания чего-либо в ip
net = ip_network('184.178.54.144/255.255.255.240')
for ip in net:
    if '111' in f'{ip:b}':
        count += 1
print(count)"""


count = 0
net = ip_network('10.48.96.0/255.255.240.0')
for ip in net:
    if f'{ip:b}'.count("1") > f'{ip:b}'.count('0'):
        count += 1
print(count)
