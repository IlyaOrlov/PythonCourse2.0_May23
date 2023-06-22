
d = {"Зимой" : "Щи", "летом" : "каша", "одним" : "пища", "цветом" : "наша"}
str = "Зимой и летом одним цветом"

print(f"Было: ", str)

for k,v in d.items():
    str = str.replace(k,v)
    print((k,v))

print(f"Стало: ", str)
