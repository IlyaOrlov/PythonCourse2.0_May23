import pickle
import random

class Human:
    def __init__(self, name, surname, age, residence):
        self.name = name
        self.surname = surname
        self.age = age
        self.residence = residence

    def __str__(self):
        return f"{self.name} {self.surname}, {self.age} лет/года, живет в  {self.residence}"

def create_humans(num_instances):
    first_names = ["John", "Alice", "Michael", "Emily", "David", "Olivia"]
    last_names = ["Smith", "Johnson", "Brown", "Lee", "Wilson"]
    residences = ["New York", "Los Angeles", "Chicago", "San Francisco", "Seattle"]

    humans = []
    for _ in range(num_instances):
        name = random.choice(first_names)
        surname = random.choice(last_names)
        age = random.randint(18, 60)
        residence = random.choice(residences)
        human = Human(name, surname, age, residence)
        humans.append(human)

    with open("human.data", "wb") as file:
        pickle.dump(humans, file)

def read_humans():
    with open("human.data", "rb") as file:
        humans = pickle.load(file)
        for human in humans:
            print(human)

if __name__ == "__main__":
    create_humans(5)  # Создаем 5 экземпляров Human и сохраняем их в файл
    read_humans()     # Читаем файл и выводим содержимое на печать