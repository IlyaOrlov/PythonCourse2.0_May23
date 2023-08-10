import pickle
import random

class Human:
    def __init__(self, name, surname, age, residence):
        self.name = name
        self.surname = surname
        self.age = age
        self.residence = residence

def create_humans(num_humans):
    humans = []
    for _ in range(num_humans):
        name = random.choice(["John", "Alice", "Michael", "Emma"])
        surname = random.choice(["Smith", "Johnson", "Brown", "Wilson"])
        age = random.randint(18, 65)
        residence = random.choice(["New York", "London", "Paris", "Tokyo"])
        human = Human(name, surname, age, residence)
        humans.append(human)
    return humans

def serialize_humans(humans, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(humans, file)

def deserialize_humans(file_path):
    with open(file_path, "rb") as file:
        humans = pickle.load(file)
    return humans

# Создаем 3 экземпляра класса Human
humans = create_humans(3)

# Сериализуем и сохраняем экземпляры в файл human.data
serialize_humans(humans, "tak/human.data")

# Читаем и десериализуем содержимое файла human.data
deserialized_humans = deserialize_humans("tak/human.data")

# Выводим результат на печать
for human in deserialized_humans:
    print(f"Name: {human.name}")
    print(f"Surname: {human.surname}")
    print(f"Age: {human.age}")
    print(f"Residence: {human.residence}")
    print()
