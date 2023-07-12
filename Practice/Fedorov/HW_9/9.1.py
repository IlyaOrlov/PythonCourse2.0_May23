import re
from pathlib import Path

current_path = str(Path.cwd())
need_path = current_path.replace("Fedorov\\HW_9", "") + "README.md"
pattern1 = r"git [a-z]{3,}.+"
pattern2 = r"[а-я].+"
commands1 = re.compile(pattern1)
repl_rus_simbols = re.compile(pattern2)
lst = set()
with open(need_path, encoding='utf-8') as myfile:
    text = myfile.readline()
    while text:
        i = commands1.search(text)
        if i:
            i = i.group(0).lower().replace("\"", "").replace(",", "").replace("(", "")
            if len(i) > 30:
                m = repl_rus_simbols.search(i)
                if m:
                    i = i.replace(m.group(0), "")
            lst.add(i)
        text = myfile.readline()

for i in lst:
    if i:
        print(i)
