import json


class UserJSONEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


class User:
    def __init__(self):
        self._name = 'name'
        self._age = 'age'

    def set_name(self, value):
        self._name = value

    def get_name(self):
        return self._name

    def set_age(self, value):
        self._age = value

    def get_age(self):
        return self._age

    def __repr__(self):
        return f"{self._name} {self._age} at {id(self)}"


user = User()
# Вариант 1: универсальный
res = json.dumps(user, cls=UserJSONEncoder)
# Вариант 2: простой
# res = json.dumps(repr(user))
print(res)
