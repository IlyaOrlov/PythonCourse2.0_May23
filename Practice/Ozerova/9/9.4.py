import random
import pickle


class Human:
    def __init__(self, name, surname, age, town, education, language):
        self.name = name
        self.surname = surname
        self.age = age
        self.town = town
        self.education = education
        self.language = language

    def __str__(self):
        return f'Меня зовут {self.name} {self.surname}, мне {self.age} лет, я проживаю в городе ' \
               f'{self.town}, у меня {self.education} образование и владею {self.language} ' \
               f'языками'

def new_human(f):
    new_name = ('Ксения', 'Кристина', 'Варвара', 'Арина', 'Аврора', 'Алена', 'Есения')
    new_surname = ('Озерова', 'Речкина', 'Иванова', 'Петрова', 'Сидорова', 'Гусева')
    new_town = ('Нижний Новгород', 'Якутск', 'Москва', 'Владивосток', 'Санкт-Петербург')
    new_education = ('Высшее', 'Среднее')

    h = []
    for _ in range(f):
        name = random.choice(new_name)
        surname = random.choice(new_surname)
        age = random.randint(18, 35)
        town = random.choice(new_town)
        education = random.choice(new_education)
        language = random.randint(2, 5)
        human_new = Human(name, surname, age, town, education, language)
        h.append(human_new)

    with open('human.data', 'wb') as file:
        pickle.dump(h, file)

def read_h():
    with open('human.data', 'rb') as file:
        h = pickle.load(file)
        for human_new in h:
            print(human_new)

if __name__ == '__main__':
    new_human(5)
    read_h()
