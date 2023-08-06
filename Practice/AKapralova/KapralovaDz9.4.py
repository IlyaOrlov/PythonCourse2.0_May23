import pickle
import random


class Human:
    def __init__(self, name, surname, age, residence):
        self.name = name
        self.surname = surname
        self.age = age
        self.residence = residence

    def __str__(self):
        return f"{self.name} {self.surname}, возраст: {self.age}, проживает в городе {self.residence}."


def create(num_instances):
    first_names = ["Анна", "Юлия", "Полина", "Олеся", "Татьяна"]
    last_names = ["Капралова", "Сидорова", "Смирнова", "Иванова", "Петрова"]
    residences = ["Нижний Новгород", "Екатеринбург", "Москва", "Иваново", "Кстово"]
    humans = []
    for i in range(num_instances):
        name = random.choice(first_names)
        surname = random.choice(last_names)
        age = random.randint(18, 25)
        residence = random.choice(residences)
        human = Human(name, surname, age, residence)
        humans.append(human)
    with open("human.data", "wb") as file:
        pickle.dump(humans, file)


def read():
    with open("human.data", "rb") as file:
        humans = pickle.load(file)
        for human in humans:
            print(human)


if __name__ == "__main__":
    create(5)
    read()
