def chng(a, b):
    for key, value in b.items():
        templ = "{" + key + "}"
        a = a.replace(templ, str(value))
    return a


dic = {"name1": "Alex","name2": "Kate"}
templ = "Hello, {name1}! My name is {name2}."
print(chng(templ, dic))