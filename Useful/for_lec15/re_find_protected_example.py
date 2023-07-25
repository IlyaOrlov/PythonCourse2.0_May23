import re

# __secret
#  _{1}[^_]\w+

lst = ["_name", "_surname", "salary", "__secret"]
p = re.compile("\A_{1}[^_]\w+")
res = []
for i in lst:
    res_lst = re.findall(p, i)
    res += res_lst

    # match_obj = re.match(p, i)
    # if match_obj:
    #     res.append(match_obj.group(0))

print(res)
