import re


res = []
with open("log_file.txt") as f:
    reg = re.compile("ERROR-\d+")
    for line in f:
        str_res = re.findall(reg, line)
        print(str_res)
        res += str_res
print(res)
