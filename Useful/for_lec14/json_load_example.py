import json

with open('jsondump.txt', 'r') as f:
    res = json.load(f)

print(res)
# addr1 = res[0]['server1']['addr']
# port1 = res[0]['server1']['port']
# print(f'Connect to server1: {addr1}:{port1}')