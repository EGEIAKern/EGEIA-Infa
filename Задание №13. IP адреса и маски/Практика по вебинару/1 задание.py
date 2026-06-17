from ipaddress import *

for mask in range(33): #перебираю количество единиц в максе (от нуля до 32)
    net = ip_network(f'220.128.112.142/{mask}',0)
    print(net,net.netmask) #маска сети в полной записи

"""
220.128.96.0/19, но при добавлении в print net.netmask получаем 220.128.96.0/19 255.255.224.0
Ответ: 224
"""