
d = {"Зимой" : "Щи", "летом" : "каша", "одним" : "пища", "цветом" : "наша"}
st_r = "Зимой и летом одним цветом"

print(f"Было: ", st_r)

for k,v in d.items():
    st_r = st_r.replace(k,v)
    print(k,v)

print(f"Стало: ", st_r)
