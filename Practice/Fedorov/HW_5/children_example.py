DEFAULT = {
    'name': 'John',
    'surname': 'Doe',
    'children': []
}

people = []
num = input('num of people: ')
for i in range(int(num)):
    name = input('name: ') or DEFAULT.get('name')
    surname = input('surname: ') or DEFAULT.get('surname')
    children = list(DEFAULT.get('children'))
    child = None
    while child != '':
        child = input('child: ')
        if child:
            children.append(child)
    people.append({'name': name, 'surname': surname, 'children': children})

for i, each in enumerate(people, 1):
    print(f'{i}: {each}')
