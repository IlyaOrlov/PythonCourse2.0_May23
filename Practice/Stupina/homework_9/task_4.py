import random
import pickle


class Human:
    def __init__(self):
        self.name = self.generator_name()
        self.patronymic = self.generator_patr()
        self.surname = self.generator_surname()
        self.age = random.randint(18, 100)
        self.pl_resid = self.generator_city()
        self.pl_birth = self.generator_city()
        self.stature = random.randint(130, 200)
        self.wt = random.randint(40, 100)

    @staticmethod
    def generator_name():
        s = ('Иван', 'Петр', 'Аня', 'Оля', 'Александр', 'Маша', 'Артём')
        return random.choice(s)

    @staticmethod
    def generator_surname():
        s = ('Иванов', 'Петров', 'Сидоров', 'Козлов', 'Попов', 'Волков')
        s_ = ('а', '')
        return random.choice(s)+random.choice(s_)

    def generator_patr(self):
        s = ('овна', 'ович')
        return self.generator_name()+random.choice(s)

    @staticmethod
    def generator_city():
        s = ('г.Москва', 'д.Лопухи', 'г.Лондон', 'с.Простоквашино', 'г.Уссурийск', 'д.Малиновка', 'г. Париж')
        return random.choice(s)

    def __str__(self):
        return f'{self.name} {self.patronymic} {self.surname}, возраст: {self.age} рост: {self.stature} ' \
               f'вес: {self.wt}, место рождения: {self.pl_birth}; место проживания: {self.pl_resid}'


def fun_dump(name_f):
    man = [Human() for _ in range(10)]
    with open(name_f, 'wb') as f:
        pickle.dump(Human, f, protocol=pickle.HIGHEST_PROTOCOL)
        pickle.dump(man, f, protocol=pickle.HIGHEST_PROTOCOL)


def fun_load(name_f):
    with open(name_f, 'rb') as f:
        MyClass = pickle.load(f)
        ob = pickle.load(f)
        for i in ob:
            print(i)


fun_dump('human')
fun_load('human')
