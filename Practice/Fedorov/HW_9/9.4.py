import random
import pickle

my_dictionary = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


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


def human_in(count_human):
    lst = [Human() for _ in range(count_human)]
    with open("human.data", "wb") as file:
        pickle.dump(lst, file, protocol=pickle.HIGHEST_PROTOCOL)


def human_out():
    with open("human.data", "rb") as file:
        humans = pickle.load(file)
    return humans


human_in(5)
print(human_out())
