def fun(x, y):
    for a, b in x.items():
         y = y.replace(a, b)
    return y


protivop = "После весны всегда наступает лето"
d = {"После": "Новый", "весны": "учебный", "всегда": "год", "наступает": "всегда",
     "лето": "осенью"}
print(fun(d, protivop))
