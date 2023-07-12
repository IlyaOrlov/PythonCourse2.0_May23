import json

addr1 = input('Введите адрес 1-го сервера ')
port1 = input('Введите порт 1-го сервера ')
addr2 = input('Введите адрес 2-го сервера ')
port2 = input('Введите порт 2-го сервера ')
my_config = {'server1': {'addr': addr1, 'port': port1}, 'server2': {'addr': addr2, 'port': port2}}

with open('jsondump.txt', 'w') as f:
    json.dump(my_config, f, sort_keys=True, indent=4)