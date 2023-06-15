dictionary = {"овощи": "пицца", "котлета": "мороженое", "компот": "кола"}
s = "Сегодня на ужин овощи, котлета, компот!"
print(f"Мама сказала: {s}")
for key, val in dictionary.items():
    s = s.replace(key, val)
print(f"Папа поправил: {s}")
