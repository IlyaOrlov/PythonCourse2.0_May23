import re
from pathlib import Path

current_path = str(Path.cwd())
need_path = current_path.replace("Fedorov\\HW_9", "") + "README.md"

with open(need_path, encoding='utf-8') as myfile:
    text = myfile.read()

pattern1 = r"git [a-z]{3,}.+"
pattern2 = r"[а-я].+"
commands1 = re.findall(pattern1, text)


all_commands = commands1
lst = set()
for i in all_commands:
    i = i.lower().replace("\"", "").replace(",", "").replace("(", "")
    if len(i) > 30:
        m = re.search(pattern2, i)
        if m:
            i = i.replace(m.group(0), "")
    lst.add(i)


for i in lst:
    print(i)
