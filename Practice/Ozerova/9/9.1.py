import re


res = []
with open("readme.md", encoding="utf-8") as f:
    reg = re.compile("git\s+\w.*")
    for line in f:
        str_res = re.findall(reg, line)
        print(str_res)

