import re


file_path = 'Practice/README.md'

# Читаем содержимое файла
with open(file_path, 'r') as file:
    content = file.read()

# Определяем шаблон регулярного выражения для поиска команд Git с аргументами
pattern = r'git\s+\w+\s+'

# Ищем все совпадения в тексте файла
matches = re.findall(pattern, content)

# Выводим найденные команды
for match in matches:
    print(match.strip())
