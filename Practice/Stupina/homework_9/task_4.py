import random
import pickle


class Human:
    s_name = ('Иван', 'Петр', 'Аня', 'Оля', 'Александр', 'Маша', 'Артём')
    s_sur_1 = ('Иванов', 'Петров', 'Сидоров', 'Козлов', 'Попов', 'Волков')
    s_sur_2 = ('а', '')
    s_patr = ('овна', 'ович')
    s_city = ('г.Москва', 'д.Лопухи', 'г.Лондон', 'с.Простоквашино', 'г.Уссурийск', 'д.Малиновка', 'г. Париж')

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
        return random.choice(Human.s_name)

    @staticmethod
    def generator_surname():
        return random.choice(Human.s_sur_1)+random.choice(Human.s_sur_2)

    def generator_patr(self):
        return self.generator_name()+random.choice(Human.s_patr)

    @staticmethod
    def generator_city():
        return random.choice(Human.s_city)

    def __str__(self):
        return f'{self.name} {self.patronymic} {self.surname}, возраст: {self.age} рост: {self.stature} ' \
               f'вес: {self.wt}, место рождения: {self.pl_birth}; место проживания: {self.pl_resid}'


def fun_dump(name_f):
    man = [Human() for _ in range(10)]
    with open(name_f, 'wb') as f:
        pickle.dump(man, f, protocol=pickle.HIGHEST_PROTOCOL)
    print('Упаковано!')


if __name__ == "__main__":
    fun_dump('human')
