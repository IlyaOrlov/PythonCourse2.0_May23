import random
import pickle

my_dictionary = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def create_human(count_human):
    lst = []
    while count_human >= len(lst):
        lst.append(Human())
    return lst


def human_in(count_human):
    lst = create_human(count_human)

    with open("human.data", "wb") as file:
        pickle.dump(lst, file, protocol=pickle.HIGHEST_PROTOCOL)


def human_out():
    with open("human.data", "rb") as file:
        humans = pickle.load(file)
    return humans


class Human:
    def __init__(self, name="", surname="", age="", town="", district="", street=""):
        self.name = name if name else self.random_simbols()
        self.surname = surname if surname else self.random_simbols()
        self.age = age if age else self.random_simbols()
        self.town = town if town else self.random_simbols()
        self.district = district if district else self.random_simbols()
        self.street = street if street else self.random_simbols()

    def about_me(self):
        print(f"Имя: {self.name} Фамилия: {self.surname}")

    @staticmethod
    def random_simbols():
        res = ""
        while len(res) < 5:
            res += random.choice(my_dictionary)
        return res


human_in(5)
print(human_out())
