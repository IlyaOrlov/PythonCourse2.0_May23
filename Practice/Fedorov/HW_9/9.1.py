import re
import os

current_path = os.path.dirname(os.path.abspath(__file__))
need_path = current_path.replace(r"Fedorov\HW_9", "") + "README.md"

with open(need_path, encoding='utf-8') as myfile:
    text = myfile.read()

#pattern = r"git [a-z]{3,8} -\w+"
pattern1 = r"git [a-z]{3,}.+"
#pattern2 = r"git [a-z]{3,10}"
#pattern3 = r"git [a-z]{3,8} --\w+-\w+"
#commands = re.findall(pattern, text)
commands1 = re.findall(pattern1, text)
#commands2 = re.findall(pattern2, text)
#commands3 = re.findall(pattern3, text)


all_commands = commands1
lst = set()
for i in all_commands:
    lst.add(i)
for i in lst:
    print(i)
