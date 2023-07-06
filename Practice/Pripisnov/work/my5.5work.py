def process_tabs(filename, option):
    with open(filename, 'r') as file:
        content = file.read()

    if option == 'collapse':
        content = content.replace('\t', ' ' * 4)
    elif option == 'expand':
        content = content.replace(' ' * 4, '\t')

    with open(filename, 'w') as file:
        file.write(content)


filename = 'myfile1.txt'
option = 'collapse'  # Или 'expand', в зависимости от желаемой операции

process_tabs(filename, option)
